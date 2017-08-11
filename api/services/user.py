from flask_template.api.objects.user import User
def get_user(id, **kwargs):
    """
    Basic get function to return a JSON object of the user details passed in
    """
    return User(id, **kwargs)