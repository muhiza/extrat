import os
import unittest

from flask import abort, url_for
from flask_testing import TestCase

from app import hello


class TestBase(TestCase):
	"""
	Test that homepage is accessible without login
	"""

class TestViews(TestBase):
	def test_homepage_view(self):
	"""
	Test that homepage is accessible without login
	"""
		response = self.client.get(url_for('app.hello'))


if __name__ == '__main__':
	unittest.main()
