from pyspark import SparkContext

data = [("apple", 3), ("banana", 2), ("apple", 4), ("banana", 5), ("orange", 7)]

# Initialize SparkContext
sc = SparkContext("local", "ReduceByKeyExample")

# Create an RDD from the sales data
rdd = sc.parallelize(data)

# Use reduceByKey to sum the values for each key
reduced_rdd = rdd.reduceByKey(lambda x, y: x + y)

# Collect and display the results
print("Reduced data:")
print(reduced_rdd.collect())

# Stop SparkContext
sc.stop()

