from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Auto_Loader").getOrCreate()

# Source, schema and checkpoint paths
source_path = "abfss://source@storagenamerahul8860.dfs.core.windows.net/incoming/"
schema_path = "abfss://bronze@storagenamerahul8860.dfs.core.windows.net/schema/auto_loader/"
checkpoint_path = "abfss://bronze@storagenamerahul8860.dfs.core.windows.net/checkpoints/auto_loader/"
bronze_path = "abfss://bronze@storagenamerahul8860.dfs.core.windows.net/delta/auto_loader_learners"

# Auto Loader stream
df_stream = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", schema_path)
    .option("cloudFiles.inferColumnTypes", "true")
    .option("header", "true")
    .load(source_path)
)

# Write new files to Bronze Delta
query = (
    df_stream.writeStream
    .format("delta")
    .option("checkpointLocation", checkpoint_path)
    .outputMode("append")
    .trigger(availableNow=True)
    .start(bronze_path)
)

query.awaitTermination()

print("Auto Loader ingestion completed successfully.")
