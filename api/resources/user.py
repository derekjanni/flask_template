# Custom parsing
parser = reqparse.RequestParser()
parser.add_argument('first_name', type=unicode, help="User's first name")
parser.add_argument('last_name', type=unicode, help="User's last name")
parser.add_argument('city', type=unicode, help="User's home city")

class UserResource(Resource):

    def get(self, user_id):
        """
	Return a JSON representation of the user

        **Example request**:
        .. sourcecode:: http
            GET /user/<user_id>
        **Example response**:
        .. sourcecode:: http
            HTTP/1.1 200 OK
            Vary: Accept
	    {
		'id': 123,
		'first_name': 'Derek',
		'last_name': 'Janni',
		'city': 'Portland'
	    }

        :status 404: User not found - "This should never happen"
        :status 400: Bad info passed in, e.g. id is cast as an integer
        """
        args = utils.parse_args(parser)
        first_name = args.get('first_name')
	last_name = args.get('last_name')
	city = args.get('city')
	
	additional_info = {
	   'first_name': first_name,
	   'last_name': last_name,
	   'city': city
	}

        try:
            return user_service.get_user(id, **additional_info)

	except AttributeError as e:
	    abort(404, message='Bad data input: {0}'.format(str(e)))


