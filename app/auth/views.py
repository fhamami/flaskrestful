from . import auth_blueprint

from flask.views import MethodView
from flask import Blueprint, make_response, request, jsonify
from app.models import User

class RegistrationView(MethodView):
    """ This class register a new user """

    def post(self):
        """ handle POST request for this view. url ---> /auth/register """

        # query to see if the user already exists
        user = User.query.filter_by(email=request.data['email']).first()

        if not user:
            # there is no user so we'll try to register them
            try:
                post_data = request.data
                # register the user
                email = post_data['email']
                password = post_data['password']
                user = User(email=email, password=password)
                user.save()

                response = {
                    'message': 'you registered succcessfully. please log in'
                }
                # return a response notifying the user that they registered successfully
                # 201 Created, The request has been fulfilled, resulting in the creation of a new resource
                return make_response(jsonify(response)), 201
            except Exception as e:
                # an error occured, therefore return a string message containing the error
                response = {
                    'message': str(e)
                }
                # 401 Unauthorized, when authentication is required and has failed or has not yet been provided
                return make_response(jsonify(response)), 401
        else:
            # there is an existing user. we don't want to register users twice
            # return a message to the user telling them that they already exist
            response = {
                'message': 'User already exists. Please login'
            }

            # 202 Accepted, The request has been accepted for processing, but the processing has not been completed.
            return make_response(jsonify(response)), 202

class LoginView(MethodView):
    """This class-based view handles user login and access token generation."""

    def post(self):
        """Handle POST request for this view. Url ---> /auth/login"""
        try:
            # Get the user object using their email (unique to every user)
            user = User.query.filter_by(email=request.data['email']).first()

            # Try to authenticate the found user using their password
            if user and user.password_is_valid(request.data['password']):
                # Generate the access token. This will be used as the authorization header
                access_token = user.generate_token(user.id)
                if access_token:
                    response = {
                        'message': 'You logged in successfully.',
                        'access_token': access_token.decode()
                    }
                    return make_response(jsonify(response)), 200
            else:
                # User does not exist. Therefore, we return an error message
                response = {
                    'message': 'Invalid email or password, Please try again'
                }
                return make_response(jsonify(response)), 401

        except Exception as e:
            # Create a response containing an string error message
            response = {
                'message': str(e)
            }
            # Return a server error using the HTTP Error Code 500 (Internal Server Error)
            return make_response(jsonify(response)), 500

# Define the API resource
registration_view = RegistrationView.as_view('registration_view')
login_view = LoginView.as_view('login_view')

# Define the rule for the registration url --->  /auth/register
# Then add the rule to the blueprint
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST'])

# Define the rule for the registration url --->  /auth/login
# Then add the rule to the blueprint
auth_blueprint.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST']
)
