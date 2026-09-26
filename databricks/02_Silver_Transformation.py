from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, upper, row_number
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("Silver_Transformation").getOrCreate()

# Bronze and Silver paths
bronze_path = "abfss://bronze@storagenamerahul8860.dfs.core.windows.net/delta/learner_data"
silver_path = "abfss://silver@storagenamerahul8860.dfs.core.windows.net/delta/learner_data"

# Read Bronze Delta data
df = spark.read.format("delta").load(bronze_path)

# Data cleaning and transformation
df_clean = (
    df
    .withColumn("learner_id", trim(col("learner_id")))
    .withColumn("learner_name", trim(col("learner_name")))
    .withColumn("gender", upper(trim(col("gender"))))
    .withColumn("course", trim(col("course")))
    .withColumn("centre_id", trim(col("centre_id")))
    .withColumn("status", upper(trim(col("status"))))
)

# Remove duplicate learners
window_spec = Window.partitionBy("learner_id").orderBy(col("learner_id"))

df_silver = (
    df_clean
    .withColumn("row_num", row_number().over(window_spec))
    .filter(col("row_num") == 1)
    .drop("row_num")
)

# Data quality check
print("Silver Record Count:", df_silver.count())

# Write Silver Delta data
(
    df_silver.write
    .format("delta")
    .mode("overwrite")
    .save(silver_path)
)

print("Silver transformation completed successfully.")
