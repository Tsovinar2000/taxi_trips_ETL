#!/usr/bin/python
"""BigQuery I/O PySpark example."""
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName('spark-bigquery-demo-for-taxi-trips') \
    .getOrCreate()

# Use the Cloud Storage bucket for temporary BigQuery export data used
# by the connector.
bucket = "chicago-taxi-trips-bucket_2023"
spark.conf.set('temporaryGcsBucket', bucket)

# Load data from BigQuery.
taxi_trips = spark.read.format('bigquery') \
    .option('table', 'bigquery-public-data:chicago_taxi_trips.taxi_trips') \
    .load()
taxi_trips.createOrReplaceTempView('taxi_trips')


# Perform word count.
fares_for_rides = spark.sql(
    ''' SELECT
  EXTRACT(DAYOFWEEK
  FROM
    trip_start_timestamp) AS day,
    MAX(fare) AS maximum_fare,
  COUNT(1) AS rides
FROM
  `taxi_trips`
WHERE
  trip_seconds >= 600
GROUP BY
  day
ORDER BY
  day ''')
fares_for_rides.show()
fares_for_rides.printSchema()

# Saving the data to BigQuery
fares_for_rides.write.format('bigquery') \
    .option('table', 'taxi_trips_dataset.taxi_trips_output') \
    .save()
