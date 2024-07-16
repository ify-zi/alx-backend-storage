#!/usr/bin/env python3
"""
    Module that classify an Nginx log
"""

from pymongo import MongoClient


if __name__ == "__main__":
    def get_doc(doc: dict) -> int:
        """ function definition """
        client = MongoClient('mongodb://127.0.0.1:27017')
        docs = client.logs.nginx
        return docs.count_documents(doc)

    def get_ip():
        """function definition"""
        client = MongoClient()
        docs = client.logs.nginx
        agg = [
                {'$group': {"_id": "$ip", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}},
                {"$limit": 10}
                ]
        return list(docs.aggregate(agg))

    stat = {"path": "/status"}
    print(f"{get_doc({})} logs")
    print(f"Methods:")
    print(f"\tmethod GET: {get_doc({'method': 'GET' })}")
    print(f"\tmethod POST: {get_doc({'method': 'POST'})}")
    print(f"\tmethod PUT: {get_doc({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {get_doc({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {get_doc({'method': 'DELETE'})}")
    print(f"{get_doc(stat)} status check")
    print("Ips:")
    p = get_ip()
    for i in p:
        print("\t{}: {}".format(i['_id'], i['count']))
