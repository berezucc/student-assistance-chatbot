from scraper import beginScraper
from syncKendra import syncKendra
import os
from dotenv import load_dotenv

bucket_name = os.getenv("S3_BUCKET_NAME")
kendra_data_source_id = os.getenv("KENDRA_DATA_SOURCE_ID")
kendra_index_id = os.getenv("KENDRA_INDEX_ID")
beginScraper(bucket_name)
syncKendra(kendra_data_source_id,kendra_index_id)
