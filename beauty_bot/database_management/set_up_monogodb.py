from pymongo import MongoClient
import json

DB_IP = "35.194.174.101"  # 35.194.174.101
DB_PORT = 27017  # default MongoDB port
DB_NAME = "beautybot"  # use the collection


class DataBase(object):
    def drop_db(self, client, db_name):
        client.drop_database(db_name)

    def remove_all_documents(self, collection):
        print("removing all documents...")
        result = collection.delete_many({})
        print(result.deleted_count)

    def create_pixnet(self, collection_pixnet, content):
        title = content['title']
        if "唇" in title:
            category = "lips"
        else:
            category = "other"
        article = {
            "article_id": content["article_id"],
            "title": title,
            "category": category,
            "tags": content['tags']
        }
        collection_pixnet.insert_one(article).inserted_id

    def create_collection_pixnet(self, collection_pixnet):
        self.remove_all_documents(collection_pixnet)
        with open("makeup.json") as json_data:
            for article in json_data:
                try:
                    j_content = json.loads(article)
                    content = {
                        "title": j_content["title"],
                        "tags": j_content['tags'],
                        "article_id": j_content['article_id']
                    }
                    print(content['title'])
                    self.create_pixnet(collection_pixnet, content)
                except KeyError as e:
                    print("KeyError" + str(e))


def main():
    client = MongoClient(DB_IP, DB_PORT)
    """
    # Put Data into monogodb
    db = DataBase()
    collection_pixnet = client[DB_NAME]["pixnet"]
    db.create_collection_pixnet(collection_pixnet)
    print(collection_pixnet.count())
    # Delete all data
    # drop_db(client, DB_NAME)
    """
    collection_pixnet = client[DB_NAME]["pixnet"]
    print(collection_pixnet.count())

    for article in collection_pixnet.find({"category": "lips", "title": {"$regex": "霧"}}):
        print(article)

if __name__ == '__main__':
    main()
