// Read from CSV files
val usersCsvPath = "/mnt/training/ecommerce/users/users-500k.csv"

val usersDF = spark.read()
    .option("sep", "\t")
    .option("header", true)
    .option("inferSchema", true)
    .csv(usersCsvPath)

usersDF.printSchema()
//  |-- user_id: string (nullable = true)
//  |-- user_first_touch_timestamp: long (nullable = true)
//  |-- email: string (nullable = true)

//  manually define schema with StructType
//  StructField(String name, DataType dataType, boolean nullable, Metadata metadata)
import org.apache.spark.types.{LongType, StringType, StructType, StructField}

val userDefinedSchema = StructType(Seq(
    StructField("user_id", StringType, true)
    StructField("user_first_touch_timestamp", LongType, true)
    StructField("email", StringType, true)
))

// Use custom schema
val userDF = spark.read()
    .option("sep", "\t")
    .option("header", true)
    .schema(userDefinedSchema)
    .csv(usersCsvPath)


// DDL Schema
val DDLSchema = "user_id string, user_first_touch_timestamp long, email string"

val usersDF = spark.read
    .option("sep", "\t")
    .option("header", true)
    .schema(DDLSchema)
    .csv(usersCsvPath)


// Read from JSON files
val eventsJsonPath = "/mnt/training/ecommerce/events/events-500k.json"

val eventsDF = spark.read
    .option("inferSchema", true)
    .json(eventsJsonPath)


// Write Dataframes to files
// Parquet
val usersOutputPath = workingDir + "/users.parquet"

userDF.write
    .option("compression", "snappy")
    .mode("overwrite")
    .parquet(usersOutputPath)


// Delta
val eventsOutputPath = workingDir + "delta/events"

eventsDF.write
    .format("delta")
    .mode("overwrite")
    .save(eventsOutputPath)


// Save as table
eventsDF.write
    .mode("overwrite")
    .saveAsTable("events_s")

