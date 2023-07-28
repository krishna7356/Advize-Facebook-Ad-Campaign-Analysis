# Advize: Facebook Ad Campaign Analysis


## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture Diagram](#architecture-diagram)
- [Data Source](#data-source)
- [Cleaning Process](#cleaning-process)
- [Transformation Process](#transformation-process)
- [Analysis and Insights](#analysis-and-insights)
- [Results](#results)

## Introduction

Welcome to Advize, a Facebook Ad Campaign Analysis project aimed at providing valuable insights into Facebook ad campaigns. This project utilizes AWS services like Lambda, Glue, Athena, and S3 to clean, transform, and analyze Facebook ads data.

## Project Overview

Advize is a data-driven project designed to help advertisers and marketers analyze the performance of their Facebook ad campaigns. By leveraging AWS Glue and Athena, the project automates the process of data cleaning, transformation, and analysis, empowering users to make informed decisions.

## Features

- Automated data cleaning using Lambda function
- Efficient data transformation with AWS Glue
- Seamless data analysis with Athena and SQL queries
- Pre-built analysis templates for various metrics
- Visualization options for clear data representation
- Scalable and cost-effective cloud-based solution

## Installation

The project can be installed and set up following these steps:

1. Clone the repository:
```
git clone https://github.com/your-username/advize-facebook-ad-analysis.git
```
## Architecture Diagram

![image](https://github.com/krishna7356/Advize-Facebook-Ad-Campaign-Analysisn-Analysis/blob/main/diagram%60.jpeg)

## Usage

To use Advize for Facebook Ad Campaign Analysis, follow these steps:

1. Upload the raw Facebook ads data CSV file to the 'fb-ads-raw-data' S3 bucket.
2. The Lambda function will be triggered automatically to clean the data and store it in the 'fb-ads-cleaned-data' bucket.
3. Run the AWS Glue script to transform the cleaned data and store it in the 'reporting-analysis-fb-ads-data' bucket.
4. Set up the Glue Crawler to catalog the transformed data in the AWS Glue Data Catalog.
5. Use Amazon Athena to perform SQL queries and analyze the data in the Glue Data Catalog.

## Data Source

The raw data for this project is sourced from Facebook ad campaigns and is expected to be in CSV format.

## Cleaning Process

The Lambda function 'clean_facebook_ads_data' is responsible for data cleaning. It performs the following operations:

- Limit the data to the first 760 rows
- Convert date columns to the correct date format
- Convert campaign_id and fb_campaign_id columns to integers

## Transformation Process

The AWS Glue script 'facebook_ads_data_transform.py' is responsible for data transformation. It applies the following transformations:

- Extract week of the year and month information from the reporting_start column
- Round the impressions column to 2 decimal places

## Analysis and Insights

With the data transformed and available in the AWS Glue Data Catalog, users can use Amazon Athena to perform various analyses on the Facebook ad campaigns. Some possible analyses include:

- Performance Metrics Analysis
- Campaign Segmentation Analysis
- Time Series Analysis
- Cost Analysis
- Geographic Analysis
- Engagement Analysis

## Results

Advize aims to provide comprehensive insights into Facebook ad campaign performance, helping advertisers optimize their campaigns for better results.
