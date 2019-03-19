from rest_framework_jwt.settings import api_settings

def jwt_payload_handler(user):
    """
    Custom JWT Token Creator
    """
    return {
                'id': user.id,
                'firstName': user.first_name,
                'lastName': user.last_name,
                'email': user.email
            }

def jwt_response_payload_handler(token, user=None, request=None):
    """ Return Verified Token """

    return {
        'token': token
    }