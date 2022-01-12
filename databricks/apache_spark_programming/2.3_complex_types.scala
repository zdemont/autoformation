val df = spark.read.parquet(salesPath)

// Utilisation d'explode : qui permet de gerer les colonnes [{}]
val detailsDF = df.withColumn("items", explode(col("items") ))
  .select("email", "items.item_name")
  .withColumn("details", split(col("item_name"), " "))


// Utilisation de array_contains et element_at
// element_at : extraire les elements d'un tableau à partir d'une position
val mattressDF = detailsDF.filter(array_contains(col("details"), "Mattress"))
  .withColumn("size", element_at(col("details"), 2))
  .withColumn("quality", element_at(col("details"), 1))

val pillowDF = detailsDF.filter(array_contains(col("details"), "Pillow"))
  .withColumn("size", element_at(col("details"), 1))
  .withColumn("quality", element_at(col("details"), 2))


// Utilisation d'unionByName qui permet l'union de deux dataframes en colonnes 
// en fonction des colonnes
val unionDF = mattressDF.unionByName(pillowDF)
  .drop("details")


// Utilisation de collect_set qui permet de regrouper en fonction dans une array les elements
val optionDF = unionDF.groupBy("email")
  .agg(
      collect_set(col("size")).alias("size options"),
      collect_set(col("quality").alias("quality options"))
  )
