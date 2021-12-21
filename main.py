import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("localhost", 30102)
# client.admin.command('enableSharding', 'taxi')

# client.admin.command('shardCollection', 'taxi.london', key={"start_latitude": "hashed"})
# client.admin.command('shardCollection', 'taxi.rides', key={"start_latitude": "hashed"})

LONDON_CSV_PATH = "./data/london.csv"
RIDES_CSV_PATH = "./data/rides.csv"

def import_csv_to_mongo(csv_path, client, collection_name, doc_name):
    
    db = client[collection_name]
    doc = db[doc_name]
    df = pd.read_csv(csv_path)
    data = doc.insert_many(df.to_dict("records"))
    
if __name__ == "__main__":
    # import_csv_to_mongo(LONDON_CSV_PATH, client, "taxi", "london")
    import_csv_to_mongo(RIDES_CSV_PATH, client, "taxi", "rides")