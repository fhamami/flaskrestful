# import unittest
#
# class TestDevelopmentConfig(unittest.TestCase):
#     def create_app(self):
#         app.config.from_object('instance.config.DevelopmentConfig')
#         return app
#
#     def test_app_is_development(self):
#         self.assertTrue(current_app.config['DEBUG'] is True)
#         self.assertFalse(current_app is None)
#         self.assertTrue(
#             app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://urestful:marimakan@172.17.0.2/restful'
#         )
