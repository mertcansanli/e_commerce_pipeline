import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *


#Orders

@dlt.view(name="trans_orders")

def trans_orders():
    return(
        spark.readStream.format("delta")\
            .load("/Volumes/workspace/bronze/bronzevolume/ecommerce_dataset/data")\
            .withColumn("Order_Date", to_date(col("order_date"),"M/d/yy"))\
            .withColumn("Quantity", column("quantity").cast(IntegerType()))\
            .withColumn("Sales", col("sales").cast(DoubleType()))\
            .withColumn("Returned", col("returned?").cast(StringType()))\
            .withColumn("Delivered_on_time", col("delivered_on_time?").cast(StringType()))\
            .withColumn("modifiedDate",current_timestamp())\
            .drop("_rescued_data")
            
    )

dlt.create_streaming_table("silver_orders")

dlt.create_auto_cdc_flow(
    target="silver_orders",
    source="trans_orders",
    keys=["order_id"],
    sequence_by="modifiedDate",
    stored_as_scd_type="2"

)

#data quality roles

rules_orders = {
    "order_id_not_null": "order_id IS NOT NULL",
    "sales_positive": "sales >= 0",
    "quantity_positive": "quantity > 0"
}

@dlt.table(name="silver_orders_clean")
@dlt.expect_all_or_drop(rules_orders)
def silver_orders_clean():
    return dlt.read_stream("silver_orders")
