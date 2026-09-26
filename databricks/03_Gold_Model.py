from pyspark.sql import SparkSession
from pyspark.sql.functions import col, broadcast

spark = SparkSession.builder.appName("Gold_Model").getOrCreate()

silver_base = "abfss://silver@storagenamerahul8860.dfs.core.windows.net/delta/"

gold_base = "abfss://gold@storagenamerahul8860.dfs.core.windows.net/delta/"

learners = spark.read.format("delta").load(silver_base + "learners")
centres = spark.read.format("delta").load(silver_base + "centres")
attendance = spark.read.format("delta").load(silver_base + "attendance")
training = spark.read.format("delta").load(silver_base + "training")
assessment = spark.read.format("delta").load(silver_base + "assessment")
placement = spark.read.format("delta").load(silver_base + "placement")

dim_learner = learners.select("learner_id","learner_name","gender","course","centre_id","status"
).dropDuplicates(["learner_id"])

dim_centre = centres.select("centre_id","centre_name"
).dropDuplicates(["centre_id"])

fact_attendance = (attendance.join(broadcast(dim_learner.select("learner_id", "course")),"learner_id","left"))

fact_training = (training.join(broadcast(dim_learner.select("learner_id", "course")),"learner_id","left"))

fact_assessment = (assessment.join(broadcast(dim_learner.select("learner_id", "course")),"learner_id","left"))

fact_placement = ( placement.join(broadcast(dim_learner.select("learner_id", "course")),"learner_id","left"))

dim_learner.write.format("delta").mode("overwrite").save(gold_base + "dim_learner")

dim_centre.write.format("delta").mode("overwrite").save(gold_base + "dim_centre")

fact_attendance.write.format("delta").mode("overwrite").save(gold_base + "fact_attendance")

fact_training.write.format("delta").mode("overwrite").save(gold_base + "fact_training")

fact_assessment.write.format("delta").mode("overwrite").save(gold_base + "fact_assessment")

fact_placement.write.format("delta").mode("overwrite").save(gold_base + "fact_placement")

print("Gold layer created successfully.")
