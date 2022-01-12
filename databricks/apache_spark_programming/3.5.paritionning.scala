val df = spark.read.parquet(eventsPath)

// Get partitions and cores 
df.rdd.getNumPartitions
println(spark.sparkContext.defaultParallelism)

// Repartition DataFrame
val repartitionedDF = df.repartition(8)
repartitionedDF.rdd.getNumPartitions

// Coalesce
val coalesceDF = df.coalesce(8)
coalesceDF.rdd.getNumPartitions

// Configure default shuffle partitions 
spark.conf.get("spark.sql.shuffle.partitions")
spark.conf.set("spark.sql.shuffle.partitions", "8")

// Adaptive Query Execution 
spark.conf.get("spark.sql.adaptive.enabled")