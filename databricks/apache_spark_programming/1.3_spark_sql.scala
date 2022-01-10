// run a sql query
val query = """"
SELECT name, price
FROM products
WHERE price < 200
ORDER BY price 
""""

val budgetDF = spark.sql(query)

budgetDF.show() 
display(budgetDF) // Same then the prec line


// Create a dataframe 
val productsDF = spark.table("products")
display(productsDF)

productsDF.printSchema()
productsDF.schema // Same then the prec line


// write the same query with DataFrame transformation 
val budgetDF = productsDF
    .select("name", "price")
    .where("price < 200")
    .orderBy("price")

// Trigger computation with DataFrame actions
budgetDF.columns
budgetDF.count()
budgetDF.take(2) // SELECT 2 rows from dataframe


// Create tmp table from dataframes
budgetDF.createOrReplaceTempView("budget") 