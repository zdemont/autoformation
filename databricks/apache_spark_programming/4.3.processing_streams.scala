// Set default shuffle partitions to number of cores on your cluster (not required, but runs faster) 
spark.conf.set("spark.sql.shuffle.partitions", sc.defaultParallelism)

