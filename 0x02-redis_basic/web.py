#!/usr/bin/env python3
"""
Module for Implementing an expiring web cache and tracker
"""

from functools import wraps
import redis
import requests

redis_ = redis.Redis()


def count_requests(method):
    """Function for counting requests"""
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper

@count_requests
def get_page(url: str) -> str:
    """Function that gets URL to obtain HTML content"""
    req = requests.get(url)
    return req.text
