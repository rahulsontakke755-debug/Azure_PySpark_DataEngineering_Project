from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("CDF_MERGE").getOrCreate()
from delta.tables import DeltaTable

target_path = "abfss://gold@storagenamerahul8860.dfs.core.windows.net/delta/fact_placement"

source_path = "abfss://silver@storagenamerahul8860.dfs.core.windows.net/delta/placement_incremental"

source_df = spark.read.format("delta").load(source_path)

target_table = DeltaTable.forPath(spark, target_path)

# MERGE / UPSERT
(
    target_table.alias("target")
    .merge(
        source_df.alias("source"),
        "target.placement_id = source.placement_id"
    )
    .whenMatchedUpdateAll()
    .whenNotMatchedInsertAll()
    .execute()
)

# Enable Change Data Feed
spark.sql(f"""
ALTER TABLE delta.`{target_path}`
SET TBLPROPERTIES (
    delta.enableChangeDataFeed = true
)
""")

# Read Change Data Feed
cdf_df = (
    spark.read
    .format("delta")
    .option("readChangeFeed", "true")
    .option("startingVersion", 0)
    .load(target_path)
)

cdf_df.select(
    "placement_id",
    "_change_type",
    "_commit_version",
    "_commit_timestamp"
).show(truncate=False)

print("MERGE/Upsert and Change Data Feed processing completed.")
