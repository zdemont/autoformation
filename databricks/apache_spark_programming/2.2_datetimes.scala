// Set Dataframe 
import org.apache.spark.sql.functions.col
val df = spark.read.parquet(eventsPath).select(col("user_id"), col("event_timestamp").alias("timestamp"))


// Cast to timestamp
// Methode 1 
val timestampDF = df.withColumn("timestamp", (col("timestamp") / 1e6).cast("timestamp"))
// Methode 2
import org.apache.spark.sql.types.TimestampType
val timestampDF = df.withColumn("timestamp", (col("timestamp") / 1e6).cast(TimestampType))

// date format
import org.apache.spark.sql.types.TimestampType
val timestampDF = df.withColumn("timestamp", (col("timestamp") / 1e6).cast(TimestampType))

// Extract datetime attribute from timestamp
// Year (Other methods : month, dayofweek, minutes, seconde, etc ...)
import org.apache.spark.sql.functions.{year, month, dayofweek, minute, second}

val datetimeDF = timestampDF.withColumn("year", year(col("timestamp")))
  .withColumn("month", month(col("timestamp")))
  .withColumn("dayofweek", dayofweek(col("timestamp")))
  .withColumn("minute", minute(col("timestamp")))
  .withColumn("second", second(col("timestamp")))   


// Convert to date 
// to_date
import org.apache.spark.sql.functions.to_date
val dateDF = timestampDF.withColumn("date", to_date(col("timestamp")))

// Mainpulate Datetimes 
// date_add
import org.apache.spark.sql.functions.date_add

val plus2DF = timestampDF.withColumn("plus_two_days", date_add(col("timestamp"), 2))

