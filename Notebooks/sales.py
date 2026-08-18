from pyspark.sql import SparkSession

data = [
    (1, "Laptop", 50000),
    (2, "Phone", 30000)
]

df = spark.createDataFrame(
    data,
    ["id", "product", "amount"]
)

df.write.mode("overwrite").saveAsTable(
    "default.sales_data"
)

print("Data Loaded Successfully")
