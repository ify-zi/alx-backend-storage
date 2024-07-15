#!/usr/bin/env python3
"""
    Module that uses python to manipulation the update function
"""


def update_topics(mongo_collection, name, topics):
    """function definition of mongodb manip."""
    filt = {'name': name}
    u_query = {"$set": {'topics': topics}}
    new_doc = mongo_collection.update_many(filt, u_query)
    return
