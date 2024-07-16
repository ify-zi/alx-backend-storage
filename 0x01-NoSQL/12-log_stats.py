#!/usr/bin/env python3
"""
    Module that classify an Nginx log
"""

from pymongo import MongoClient


if __name__ == "__main__":
    def get_doc(doc: dict)-> int:
        """ function definition """
        client = MongoClient('mongodb://127.0.0.1:27017')
        docs = client.logs.nginx
        return docs.count_documents(doc)
    
    stat = {"path": "/status"}
    print(f"{get_doc({})} logs")
    print(f"Methods:")
    print(f"\tmethod GET: {get_doc({'method': 'GET' })}")
    print(f"\tmethod POST: {get_doc({'method': 'POST'})}")
    print(f"\tmethod PUT: {get_doc({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {get_doc({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {get_doc({'method': 'DELETE'})}")
    print(f"{get_doc(stat)} status check")
