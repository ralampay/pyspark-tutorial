from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "ReadTextFileExample")

# Read the text file into an RDD
rdd = sc.textFile("example.txt")

# Display the contents of the RDD
print("Contents of the file:")
print(rdd.collect())

# Perform transformations on the RDD
# map: Count the number of words in each line
word_counts = rdd.map(lambda line: len(line.split()))

# filter: Returns only True conditions
spark_lines = rdd.filter(lambda line: "Spark" in line)

# Display word counts for each line
print("Word counts per line:")
print(word_counts.collect())

# Display spark_lines
print("Lines containing 'Spark':")
print(spark_lines.collect())

# Stop the SparkContext
sc.stop()
