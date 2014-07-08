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
		print uid
		try:
			user = User.objects.get(email=uid)
		except:
			return None
		print user
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



		