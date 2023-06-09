#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""...
...
...
...
"""
from models.base_model import BaseModel
from datetime import datetime
import pep8
import unittest


class TestBaseModel(unittest.TestCase):
    """...
    ...
    ...
    """
    def test_pep8_of_base_model(self):
        """...
        ...
        ...
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_base_model_id_is_string(self):
        """...
        ...
        ...
        """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_base_model_created_at_is_datetime(self):
        """...
        ...
        ...
        """
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_base_model_updated_at_is_datetime(self):
        """...
        ...
        ...
        """
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)
