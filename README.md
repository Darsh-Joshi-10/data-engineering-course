# Data Engineering: Zero to Job-Ready

Hands-on data engineering course: Python, SQL, pipelines, cloud, and a portfolio capstone, built module by module.

This repo holds the code for every video in the course. Each video ends with working code committed here.

**Watch the course:** [Data Engineering playlist on YouTube](https://www.youtube.com/playlist?list=PLNitbFlQOHLI)

## Who this is for

People who want to become data engineers and learn by building. Basic programming familiarity helps, and Module 1 refreshes the Python you'll actually use.

## How to follow along

1. Watch the video and **type the code along with me**. Don't copy-paste from this repo. It's for checking your work *after*.
2. Build your own `data-engineering-course` repo on your GitHub as you go. By the end it's your portfolio.
3. Do the homework in each video's `exercises/` folder, then commit and push.

## Course roadmap

53 videos are planned across 9 modules. Modules are released in order, so the later ones are still outlines.

| Module | Topic | Videos | Status |
|--------|-------|--------|--------|
| [0. Course Intro & Roadmap](module-00-intro/) | What data engineering is, where this course is going, and the free tools you'll need. | 3 | In progress |
| [1. Python for Data Engineering](module-01-python/) | The 20% of Python data engineers use 80% of the time, then your first end-to-end ETL script. | 7 | Up next |
| [2. Databases & SQL](module-02-databases-sql/) | SQL from SELECT to window functions, how to model data, and running PostgreSQL yourself. | 7 | Planned |
| [3. Data Warehousing](module-03-data-warehousing/) | How analytical systems differ from transactional ones, and how to model data for them. | 6 | Planned |
| [4. ETL / ELT & Orchestration](module-04-etl-orchestration/) | Moving and transforming data on a schedule with Airflow and dbt. | 7 | Planned |
| [5. Big Data & Distributed Systems](module-05-big-data/) | Why one machine isn't enough, and how Spark and Kafka handle data at scale. | 7 | Planned |
| [6. Cloud Fundamentals](module-06-cloud/) | Storage, security, and managed data services in the cloud. | 6 | Planned |
| [7. Data Quality, Testing & DevOps](module-07-quality-testing-devops/) | Making pipelines trustworthy: checks, tests, CI/CD, and monitoring. | 5 | Planned |
| [8. Capstone & Career](module-08-capstone-career/) | One portfolio-grade project from design to deployment, then the job hunt. | 5 | Planned |

## What each module covers

### [Module 0: Course Intro & Roadmap](module-00-intro/)

What data engineering is, where this course is going, and the free tools you'll need.

- 0.1 [What is Data Engineering? (vs Data Science vs Data Analyst)](https://youtu.be/nCy4RJDH0LE)
- 0.2 [Full Course Roadmap & How to Follow Along](https://youtu.be/YSOrBgQTUSM)
- 0.3 Tools You'll Need (All Free)

### [Module 1: Python for Data Engineering](module-01-python/)

The 20% of Python data engineers use 80% of the time, then your first end-to-end ETL script.

- 1.1 Python Refresher: Only What Data Engineers Actually Use
- 1.2 Working with Files: CSV, JSON, Excel
- 1.3 APIs and Web Scraping Basics
- 1.4 Pandas Deep Dive, Part 1
- 1.5 Pandas Deep Dive, Part 2
- 1.6 Error Handling, Logging, and Config Files
- 1.7 Your First ETL Script, End to End

### [Module 2: Databases & SQL](module-02-databases-sql/)

SQL from SELECT to window functions, how to model data, and running PostgreSQL yourself.

- 2.1 SQL Crash Course: SELECT to JOINs
- 2.2 Window Functions & CTEs
- 2.3 Normalization vs Denormalization
- 2.4 PostgreSQL Setup Deep Dive
- 2.5 Indexing & Query Optimization
- 2.6 NoSQL Intro: MongoDB
- 2.7 Mini-Project: Build a Small Analytics Database

### [Module 3: Data Warehousing](module-03-data-warehousing/)

How analytical systems differ from transactional ones, and how to model data for them.

- 3.1 OLTP vs OLAP
- 3.2 Star Schema vs Snowflake Schema
- 3.3 Slowly Changing Dimensions
- 3.4 Cloud Warehouse Walkthrough (BigQuery, Snowflake, or Redshift)
- 3.5 Partitioning & Clustering
- 3.6 Project: Design a Warehouse for E-Commerce Data

### [Module 4: ETL / ELT & Orchestration](module-04-etl-orchestration/)

Moving and transforming data on a schedule with Airflow and dbt.

- 4.1 ETL vs ELT Explained
- 4.2 Apache Airflow Setup with Docker
- 4.3 DAGs, Operators, and Sensors
- 4.4 Scheduling, Retries, and Backfills
- 4.5 dbt Fundamentals, Part 1
- 4.6 dbt Fundamentals, Part 2
- 4.7 Project: Full Airflow + dbt Pipeline

### [Module 5: Big Data & Distributed Systems](module-05-big-data/)

Why one machine isn't enough, and how Spark and Kafka handle data at scale.

- 5.1 Why Distributed Computing? (Horizontal Scaling)
- 5.2 HDFS and Object Storage (S3) Concepts
- 5.3 Apache Spark Intro & Architecture
- 5.4 Spark SQL & DataFrames
- 5.5 Kafka: Producers, Consumers, and Topics
- 5.6 Streaming vs Batch Processing
- 5.7 Project: Spark Job on a Real Dataset

### [Module 6: Cloud Fundamentals](module-06-cloud/)

Storage, security, and managed data services in the cloud.

- 6.1 Cloud Overview: AWS vs GCP vs Azure
- 6.2 Cloud Storage: S3 / GCS
- 6.3 IAM and Security Basics
- 6.4 Cloud Data Services (Glue, EMR, or Equivalents)
- 6.5 Cost Optimization Basics
- 6.6 Project: Deploy Your Pipeline to the Cloud

### [Module 7: Data Quality, Testing & DevOps](module-07-quality-testing-devops/)

Making pipelines trustworthy: checks, tests, CI/CD, and monitoring.

- 7.1 Data Quality Checks & Great Expectations
- 7.2 Unit and Integration Testing for Pipelines
- 7.3 CI/CD for Data Pipelines
- 7.4 Git Best Practices
- 7.5 Monitoring & Alerting (Alerts, Dead-Letter Queues)

### [Module 8: Capstone & Career](module-08-capstone-career/)

One portfolio-grade project from design to deployment, then the job hunt.

- 8.1 Capstone Part 1: Architecture Design
- 8.2 Capstone Part 2: Build
- 8.3 Capstone Part 3: Deploy & Document
- 8.4 Resume & Portfolio Tips for Data Engineering Roles
- 8.5 Interview Prep: Common Data Engineering Interview Questions

## Repo structure

```
data-engineering-course/
├── .gitignore
├── README.md                 <- you are here
├── module-00-intro/
│   └── README.md
├── module-01-python/
│   └── README.md
├── module-02-databases-sql/
│   └── README.md
├── module-03-data-warehousing/
│   └── README.md
├── module-04-etl-orchestration/
│   └── README.md
├── module-05-big-data/
│   └── README.md
├── module-06-cloud/
│   └── README.md
├── module-07-quality-testing-devops/
│   └── README.md
├── module-08-capstone-career/
│   └── README.md
```

Each module has its own folder and README. Each video's code goes in a `video-X.Y-name/` subfolder inside its module.

## Setup

You'll need Python 3.10 or newer and Git. Full setup is covered in Module 0 and video 1.1.

## Author

Made by [YOUR NAME]. Questions or feedback? Open an issue or leave a comment on the video.
