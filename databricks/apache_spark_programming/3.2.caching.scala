// DO NOT RUN ON SHARED CLUSTER - CLEARS YOUR CACHE AND YOUR COWORKER'S
// spark.catalog.clearCache()


// Set dataframe
val eventsJsonPath = "/mnt/training/ecommerce/events/events-1m.json"

val df = spark.read
  .option("inferSchema", true)
  .json(eventsJsonPath)


// Store in the cache
 df.cache() 


// Remove cache
df.unpersist()


// Cache table for RDD name
df.createOrReplaceTempView("Pageviews_DF_Scala")
spark.catalog.cacheTable("Pageviews_DF_Scala")

