val salesDF = spark.read.parquet(salesPath)
val usersDF = spark.read.parquet(usersPath)
val eventsDF = spark.read.parquet(eventsPath)


val convertedUsersDF = salesDF
    .select("email")
    .distinct()
    .withColumn("converted", lit(true))



val conversionsDF = convertedUsersDF
    .join(usersDF, Seq("email"), "outer")
    .filter(col("email").isNotNull)
    .na.fill(false)


val cartsDF = eventsDF
    .withColumn("items", explode(col("items")))
    .groupBy("user_id").agg(
        collect_set("items.item_id").alias("cart")
    )


val emailCartsDF = conversionsDF.join(cartsDF, Seq("user_id"), "left")


val abandonedCartsDF = emailCartsDF
  .filter(col("converted") === false)
  .filter(col("cart").isNotNull)


val abandonedItemsDF = abandonedCartsDF
  .withColumn("items", explode(col("cart")))
  .groupBy("items").count()
  .sort("items")