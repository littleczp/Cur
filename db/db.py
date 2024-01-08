"""
数据库
"""
import enum

from pymongo import MongoClient


class Collection(str, enum.Enum):
    TASK = "task"


class DBInstance:
    _instance: Collection = None

    @staticmethod
    def with_collection(collection_name: Collection):
        instance = DBInstance()
        instance._instance = MongoClient("mongodb://localhost:27017/")['task'][collection_name]
        return instance._instance
