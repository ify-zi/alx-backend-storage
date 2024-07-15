#!/usr/bin/env python3
"""
    Module return inserts a new record into the collection
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """function definition"""
    obj_id = mongo_collection.insert_one(kwargs)
    return obj_id.inserted_id
