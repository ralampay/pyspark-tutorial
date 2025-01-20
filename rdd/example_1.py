from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "ParallelizeExample")

# Data to parallelize
data = [1, 2, 3, 4, 5]

# Create RDD with default partitions
rdd = sc.parallelize(data)

# Check number of partitions
print("Number of partitions:", rdd.getNumPartitions())

# Collect and display data
print("Data in RDD:", rdd.collect())

# Stop SparkContext
sc.stop()
