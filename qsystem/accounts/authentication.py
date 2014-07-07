from accounts.models import User

class Authentication():
	"""docstring for Authentication"""
	def __init__(self, request):
		self._request = request
	def get_user(self):
		"""
		If uid in cookie exist and match with db, return corresponding user 
		else return None
		"""
		uid = request.get_signed_cookie('uid', default = None)
		if uid == None:
			return None
		try:
			user = User.objects.get(email=_request.get_signed_cookie('email'))
		except:
			return None
		return user

	def set_cookie(self,response, user):
		"""
		Set user's email as cookie in response
		"""
		response.set_signed_cookie('uid', "mgnhjkl@163.com", max_age = 3600)

	def is_login(self):
		"""
		If a request contians a user login infomation, return True
		Else return False
		"""
		user = get_user
		if user == None:
			return False
		else:
			return True



		