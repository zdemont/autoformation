// Set a dataFrame
val df = spark.read.parquet(eventsPath)

// Grouping
df.groupBy("event_name")
df.groupBy("geo.state", "geo.city")


// Grouping data methods
val eventCountsDF = df.groupBy("event_name").count()
val avgStatePurchasesDF = df.groupBy("geo.state").avg("ecommerce.purchase_revenue_in_usd")
val cityPurchaseQuantitiesDF = df.groupBy("geo.state", "geo.city").sum("ecommerce.total_item_quantity")

// Built-in aggregate functions 
import org.apache.spark.sql.functions.sum

val statePurchasesDF = df.groupBy("geo.state").agg(
    sum("ecommerce.total_item_quantity").alias("total_purchases")
)

// Built-in multi aggregates functions 
import org.apache.spark.sql.functions.{avg, approx_count_distinct}

val stateAggregatesDF = df.groupBy("geo.state").agg(
    avg("ecommerce.total_item_quantity").alias("avg_quantity"),
    approx_count_distinct("user_id").alias("distinct_users")
)


// LAB 
import org.apache.spark.sql.functions.{sum, avg}
val trafficDF = df.groupBy("traffic_source").agg(
    sum("revenue").alias("total_rev"),
    avg("revenue").alias("avg_rev")
)

// Sort by a column and limit rows
val topTrafficDF = trafficDF.groupBy(col("total_rev").desc)
    .limit(3)

