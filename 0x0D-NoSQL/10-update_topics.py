#!/usr/bin/env python3
""" hanges all topics of a school document based on the name """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ Change school topics
    """
    return mongo_collection.update_many({
        "name": name
    },
    {
        "$set": {
            "topics": topics
        }
    })
