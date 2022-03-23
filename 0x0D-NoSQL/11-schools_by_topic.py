#!/usr/bin/env python3
""" Return the list of school having a specific topic """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    return a specific topic
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
