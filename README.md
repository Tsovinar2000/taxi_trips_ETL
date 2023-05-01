
# Chicago Taxi Trips Pipeline

This project is designed to provide an efficient and reliable data pipeline for analyzing Chicago taxi trips data. The data pipeline collects, processes, and stores data from Chicago's taxi trips to help identify what is the maximum fares for rides lasting 10 minutes or more?

## Schema

This architecture includes the following components:

**Data source:** I user public dataset from BigQuery : https://console.cloud.google.com/marketplace/product/city-of-chicago-public-data/chicago-taxi-trips?project=chicago-taxi-trips-385215


**Data ingestion:** I extract data from a public dataset into my own BigQuery project using the Google Cloud Console.

**Processing:** For transforms and batch processes the data I used  a combination of serverless and batch processing technologies : Dataflow, Dataproc and Apache Spark. 

**Data storage:** After batch processing data is stroed in data warehouse. I used BigQuery, for further analysis and reporting.

**Analytics and reporting:** For this component I used Looker Studio.

![App Screenshot](https://www.linkpicture.com/q/Screen-Shot-2023-04-30-at-6.16.09-PM.png)

## Demonstration dashboard
https://lookerstudio.google.com/reporting/3166d643-6874-4856-8a50-f1b1f078722d

![App Screenshot](https://www.linkpicture.com/q/Screen-Shot-2023-05-01-at-6.15.23-PM.png)


