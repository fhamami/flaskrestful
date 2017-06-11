import unittest
from flask import current_app
from flask_testing import TestCase
from app import create_app

class TestDevelopmentConfig(unittest.TestCase):
    def create_app(self):
        create_app.config.from_object('DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(current_app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            current_app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://urestful:marimakan@172.17.0.2/restful'
        )

class TestTestingConfig(unittest.TestCase):
    def create_app(self):
        create_app.config.from_object('TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['DEBUG'])
        self.assertTrue(
            current_app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://urestful:marimakan@172.17.0.2/restful_test_db'
        )
