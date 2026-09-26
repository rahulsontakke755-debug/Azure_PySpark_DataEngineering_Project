from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName("Event_Hubs_Streaming").getOrCreate()

# Event Hub configuration
eventhub_namespace = "rahul-eventhub-ns"
eventhub_name = "learner-events"

# Read Event Hub connection string from Databricks Secret Scope
connection_string = dbutils.secrets.get(scope="eventhub-secrets",key="databricks-listen")

kafka_options = {
    "kafka.bootstrap.servers": f"{eventhub_namespace}.servicebus.windows.net:9093",
    "subscribe": eventhub_name,
    "kafka.security.protocol": "SASL_SSL",
    "kafka.sasl.mechanism": "PLAIN",
    "kafka.sasl.jaas.config":
        f'kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="{connection_string}";',
    "startingOffsets": "latest"}

# Read streaming events from Event Hubs
event_stream = (spark.readStream.format("kafka").options(**kafka_options).load())

# Event schema
event_schema = StructType([
    StructField("learner_id", StringType(), True),
    StructField("event_type", StringType(), True),
    StructField("course", StringType(), True),
    StructField("centre_id", StringType(), True),
    StructField("event_date", StringType(), True)
])

# Parse JSON event data
parsed_events = (
    event_stream
    .selectExpr("CAST(value AS STRING) AS json_value")
    .select(from_json(col("json_value"), event_schema).alias("data"))
    .select("data.*"))

# Bronze Delta streaming path
bronze_path = "abfss://bronze@storagenamerahul8860.dfs.core.windows.net/delta/eventhub_learners"
checkpoint_path = "abfss://bronze@storagenamerahul8860.dfs.core.windows.net/checkpoints/eventhub_learners"

# Write Event Hub events to Bronze Delta
query = (
    parsed_events.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_path)
    .start(bronze_path))
query.awaitTermination()
