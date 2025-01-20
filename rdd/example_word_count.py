from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "Wordcount")

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
rdd = sc.parallelize(words).map(lambda word: (word, 1))

# Count occurrences of each word
word_counts = rdd.reduceByKey(lambda x, y: x + y)

print(word_counts.collect())
