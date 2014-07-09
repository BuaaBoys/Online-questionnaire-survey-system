from accounts.models import User
from django.core import signing

class Authentication():
	"""docstring for Authentication"""
	def __init__(self, request):
		self._request = request

	def get_user(self):
		"""
		If uid in cookie exist and match with db, return corresponding user 
		else return None
		"""
		dumped_uid = self._request.get_signed_cookie('uid', default = None)
		if dumped_uid == None:
			return None
		uid = signing.loads(dumped_uid, key = "mgnhjkl@163.com")
		try:
			user = User.objects.get(email=uid)
		except:
			return None
		return user

	def set_cookie(self, response, user):
		"""
		Set user's email as cookie in response
		"""
		uid = signing.dumps(user.email, key = "mgnhjkl@163.com")
		response.set_signed_cookie("uid", uid, max_age = 3600)

	def is_login(self):
		"""
		If a request contians a user login infomation, return True
		Else return False
		"""
		user = self.get_user()
		if user == None:
			return False
		else:
			return True

	'''
	def set_filled(self):
		"""
		Set a mark in cookie when user filled a questionnaire
		"""
		response.set_signed_cookie("filled", 1, max_age = (365*24*3600)))

	def is_filled(self):
		"""
		If the user has filled the questionnaire
		"""
	'''


		