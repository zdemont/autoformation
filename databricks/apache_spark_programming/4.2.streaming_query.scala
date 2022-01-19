// Build straming DataFrames
val schema = "device STRING, ecommerce STRUCT<purchase_revenue_in_usd: DOUBLE, total_item_quantity: BIGINT, unique_items: BIGINT>, event_name STRING, event_previous_timestamp BIGINT, event_timestamp BIGINT, geo STRUCT<city: STRING, state: STRING>, items ARRAY<STRUCT<coupon: STRING, item_id: STRING, item_name: STRING, item_revenue_in_usd: DOUBLE, price_in_usd: DOUBLE, quantity: BIGINT>>, traffic_source STRING, user_first_touch_timestamp BIGINT, user_id STRING"

val df = spark.readStream
  .schema(schema)
  .option("maxFilesPerTrigger", 1)
  .parquet(eventsPath)

df.isStreaming


// Requet dataframe like normal dataframe
import org.apache.spark.sql.functions.{col, approx_count_distinct, count}

val emailTrafficDF = df.filter(col("traffic_source") === "email")
  .withColumn("mobile", col("device").isin("iOS", "Android"))
  .select("user_id", "event_timestamp", "mobile")


// Write streaming query results
import org.apache.spark.sql.streaming.Trigger

val checkpointPath = workingDir + "/email_traffic/checkpoint"
val outputPath = userhome + "/email_traffic/output"

val devicesQuery = emailTrafficDF.writeStream
  .outputMode("append")
  .format("parquet")
  .queryName("email_traffic_s")
  .trigger(Trigger.ProcessingTime("1 second"))
  .option("checkpointLocation", checkpointPath)
  .start(outputPath)


// Monitor Streaming query
devicesQuery.id
devicesQuery.status
devicesQuery.awaitTermination(5)
devicesQuery.stop()

