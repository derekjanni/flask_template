class User(object):
    def __init__(
        self,
        id,
	**kwargs
    ):
        self.id = user_id
        self._fist_name = kwargs.get('first_name')
	self._last_name = kwargs.get('last_name')
	self._city = kwargs.get('city')

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
	return self._last_name

    @property
    def city(self):
	return self._city

    def to_dict(self):
	return {
	   'id': self.id,
           'first_name': self.first_name,
	   'last_name': self.last_name,
	   'city': self.city
	}
