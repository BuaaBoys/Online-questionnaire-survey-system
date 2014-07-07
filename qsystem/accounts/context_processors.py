from django.template import loader, RequestContext
from accounts.authentication import Authentication

def custom_auth(request):
	"""
	Return user infomation
	"""
	authentication = Authentication(request)
	user = authentication.get_user()
	if user != None:
		user_context = {"email" : user.email, "login" : 'true' }
	else:
		user_context = {"email" : "", "login" : 'false'}
	return {
		'custom_user' : user_context,
	}