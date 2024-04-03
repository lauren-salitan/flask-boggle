# from unittest import TestCase
# from app import app
# from flask import session
# from boggle import Boggle
# d


# class FlaskTests(TestCase):

#     def setUp(self):
#         """Stuff to do before every test."""
#         self.client = app.test_client()
#         app.config['TESTING'] = True

#     def test_homepage(self):
#         """Make sure homepage displays."""
#         with self.client:
#             response = self.client.get('/')
#             self.assertIn('board', session)
#             self.assertIn(b'<table>', response.data)
from unittest import TestCase
from app import app
from flask import session

class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_homepage(self):
        """Make sure homepage displays and board is in session."""
        with self.client as client:
            response = client.get('/')
            self.assertIn('board', session)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'word-form', response.data)
