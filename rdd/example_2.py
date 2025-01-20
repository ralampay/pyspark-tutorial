
from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "ParallelizeExample")

# Data to parallelize
data = [1, 2, 3, 4, 5]

# Parallelize with 3 partitions
rdd = sc.parallelize(data, numSlices=3)

# Inspect partitions
print("Number of partitions:", rdd.getNumPartitions())
print("Partitioned data (w/ glom()):", rdd.glom().collect())
print("Partitioned data (without glom()):", rdd.collect())

sc.stop()
