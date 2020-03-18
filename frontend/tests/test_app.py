import unittest
from flask import abort, url_for
from flask_testing import TestCase
import pytest
import app

class TestViews(TestCase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
