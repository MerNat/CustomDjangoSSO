from rest_framework_jwt.settings import api_settings

def jwt_payload_handler(user):
    """
    Custom JWT Token Creator
    """
    return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }