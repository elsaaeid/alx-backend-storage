#!/usr/bin/env python3
"""
Module with a function that inserts a new document in a collection.
"""


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document in a collection.
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
