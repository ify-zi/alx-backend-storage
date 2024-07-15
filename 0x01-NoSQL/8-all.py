#!/usr/bin/env python3
"""
    Module that uses mongo db to view te records in python
"""

import pymongo


def list_all(mongo_collection):
    """list all the records from collection"""
    doc_list = []
    for doc in mongo_collection.find():
        doc_list.append(doc)

    return doc_list
