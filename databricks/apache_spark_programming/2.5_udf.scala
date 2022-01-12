val salesDF = spark.read.parquet(salesPath)


// Define a function
def firstLetterFunction (email: String): String = {
  email(0).toString
}

//  Create and apply UDF
val firstLetterUDF = udf(firstLetterFunction _)

import org.apache.spark.sql.functions.col
display(salesDF.select(firstLetterUDF(col("email"))))


// Register UDF to use in SQL
salesDF.createOrReplaceTempView("sales")

spark.udf.register("sql_udf", firstLetterFunction _)

// %sql
// SELECT sql_udf(email) AS firstLetter FROM sales