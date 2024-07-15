#!/usr/bin/env python3
"""
    Module uses find() to query collection
"""


def schools_by_topic(mongo_collection, topic):
    """Function definition"""
    obj = mongo_collection.find({'topics': topic})
    return obj
