#!/usr/bin/python3
"""Initializes the package"""
from models.engine.file_storage import Filestorage
storage = Filestorage()
storage.reload()
