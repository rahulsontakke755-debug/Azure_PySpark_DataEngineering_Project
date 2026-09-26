from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Bronze_Ingestion").getOrCreate()

# Source and Bronze paths
source_path = "abfss://source@storagenamerahul8860.dfs.core.windows.net/student_data/"
bronze_path = "abfss://bronze@storagenamerahul8860.dfs.core.windows.net/delta/"

# Read CSV files
df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(source_path)
)

# Basic validation
print("Source Record Count:", df.count())
print("Columns:", df.columns)

# Write data to Bronze as Delta
(
    df.write
    .format("delta")
    .mode("overwrite")
    .save(bronze_path + "learner_data")
)

print("Bronze ingestion completed successfully.")
