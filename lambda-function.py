import json
import boto3
import uuid
import io
import pandas as pd
from datetime import datetime


def lambda_handler(event, context):
    
    bucket_name = 'fb-ads-raw-data'
    destination_folder = 'fb-ads-cleaned-data'
    
    
    s3_client = boto3.client('s3')

    response = s3_client.list_objects(Bucket=bucket_name)

    # Extract the object keys using list comprehension
    object_keys = "data.csv"
    
    data = s3_client.get_object(Bucket=bucket_name, Key=object_keys)
    
    facebook_data = pd.read_csv(data['Body'])
    
    facebook_data_cleaned = facebook_data.iloc[:760]
    facebook_data_cleaned['reporting_start'] = pd.to_datetime(facebook_data['reporting_start'],format='%d/%m/%Y').dt.normalize()
    facebook_data_cleaned['reporting_end'] = pd.to_datetime(facebook_data['reporting_end'],format='%d/%m/%Y').dt.normalize()
    facebook_data_cleaned[['campaign_id','fb_campaign_id']]= facebook_data_cleaned[['campaign_id','fb_campaign_id']].astype(str).astype(int)
    
    # print(facebook_data_cleaned.info())
    
    unique_id = str(uuid.uuid4())[:8]  # Using the first 8 characters of the UUID

    # Get the current date and use it in the filename
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Now, let's save the processed DataFrame to a new CSV file in memory
    csv_buffer = io.StringIO()
    facebook_data_cleaned.to_csv(csv_buffer, index=False)
    
    destination_object_key = destination_folder + f'{unique_id}_{current_date}.csv'
    
    # Upload the new CSV file to the destination folder in the S3 bucket
    s3_client.put_object(Bucket=destination_folder, Key=destination_object_key, Body=csv_buffer.getvalue())
    
    
    
    
    
    return {
        'statusCode': 200
    }
