#!/usr/bin/env python3
"""
    Module that classify an Nginx log
"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx
total = collection.count_documents({})
get_count = collection.count_documents({"method": "GET"})
post_count = collection.count_documents({"method": "POST"})
put_count = collection.count_documents({"method": "PUT"})
patch_count = collection.count_documents({"method": "PATCH"})
delete_count = collection.count_documents({"method": "DELETE"})
stat_count = collection.count_documents({"path": "/status"})

print(f"{total} logs\nMethods:\n\tmethod GET:{get_count}\n\t\
method POST: {post_count}\n\t\
method PUT: {put_count}\n\t\
method PATCH: {patch_count}\n\t\
method DELETE: {delete_count}\n\
{stat_count} status check")
