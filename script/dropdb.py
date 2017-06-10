from .restful.app import db

def setUp(self):
    """ set up test varibles """

    self.app = create_app(config_name="testing")
    # initialize the test client

    with self.app.app_context():
        # create all tables
        db.session.close()
        db.drop_all()
