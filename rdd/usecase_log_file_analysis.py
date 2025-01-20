from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "LogFileAnalysis")

# Step 1: Load log files into an RDD
log_rdd = sc.textFile("logs/*.log")  # Load all log files in the folder

# Step 2: Filter logs for 'ERROR' level
error_logs = log_rdd.filter(lambda line: "[ERROR]" in line)

# Step 3: Correctly extract the error message
# First split to remove the timestamp part, then split again to remove the log level.
error_messages = error_logs.map(lambda line: line.split("] [")[-1].split("]")[-1].strip())

# Step 4: Count occurrences of each error message
error_counts = error_messages.map(lambda msg: (msg, 1)).reduceByKey(lambda x, y: x + y)

# Step 5: Repartition for load balancing (optional, if partitions are uneven)
repartitioned_rdd = error_counts.repartition(4)

# Step 6: Inspect partition data
partition_data = repartitioned_rdd.glom().collect()
print("Partitioned data:")
for idx, partition in enumerate(partition_data):
    print(f"Partition {idx}: {partition}")

# Step 7: Collect and display the final result
final_result = error_counts.collect()
print("Error message counts:")
for message, count in final_result:
    print(f"{message}: {count}")

# Stop the SparkContext
sc.stop()
