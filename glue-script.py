import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
  
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
fb_campagin = glueContext.create_dynamic_frame_from_options(connection_type= "s3",connection_options={"paths":['s3://fb-ads-cleaned-data/']},
                                                           format="csv",format_options={"withHeader":True})
from pyspark.sql.functions import * 
fb_campagin_transformed = ApplyMapping.apply(frame=fb_campagin,
                                            mappings=[("ad_id","string","ad_id","int"),
                                                      ("reporting_start","string","reporting_start","timestamp"),
                                                      ("reporting_end","string","reporting_end","timestamp"),
                                                      ("campaign_id","string","campaign_id","int"),
                                                      ("fb_campaign_id","string","fb_campaign_id","int"),
                                                      ("age","string","age","string"),
                                                      ("gender","string","gender","string"),
                                                      ("interest1","string","interest1","int"),
                                                      ("interest2","string","interest2","int"),
                                                      ("interest3","string","interest3","int"),
                                                      ("impressions","string","impressions","float"),
                                                      ("clicks","string","clicks","int"),
                                                      ("spent","string","spent","float"),
                                                      ("total_conversion","string","total_conversion","float"),
                                                      ("approved_conversion","string","approved_conversion","float")],
                                             transformation_ctx="fb_campagin_transformed")
fb_campagin_transformed = fb_campagin_transformed.withColumn("reporting_start",to_date(col("reporting_start"),"yyyy-MM-dd"))
fb_campagin_transformed = fb_campagin_transformed.withColumn("reporting_end",to_date(col("reporting_end"),"yyyy-MM-dd"))
fb_campagin_transformed = fb_campagin_transformed.withColumn('impressions', round(fb_campagin_transformed['impressions'],2))

fb_campagin_transformed = fb_campagin_transformed.withColumn('campagin_weekOfYear', weekofyear('reporting_start'))

fb_campagin_transformed = fb_campagin_transformed.withColumn('campagin_month', month(fb_campagin_transformed['reporting_start']))
fb_campagin_parquet = glueContext.getSink(
  path="s3://reporting-analysis-fb-ads-data/",
  connection_type="s3",
  updateBehavior="UPDATE_IN_DATABASE",
  compression="snappy",
  enableUpdateCatalog=True,
  transformation_ctx="fb_campagin_parquet",
)
fb_campagin_parquet.setCatalogInfo(
  catalogDatabase="demo", catalogTableName="fb-ads-data"
)
fb_campagin_parquet.setFormat("glueparquet")
fb_campagin_parquet.writeFrame(fb_campagin_transformed)
job.commit()