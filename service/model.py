# coding: utf-8

# service/model.py

import datetime
from typing import List


class Blog:
    def __init__(self, name: str):
        self.name = name
        self.posts : List[Post]


class Post:
    def __init__(self, title: str, date: datetime.datetime):
        self.title = title
        self.date = date
        self.tags: List[Tag]


class Tag:
    def __init__(self, desc: str):
        self.desc = desc
        self.posts : List[Post]
