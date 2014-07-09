from accounts.authentication import Authentication
from investmanager.models import Questionnaire
from results.models import Result

def manage_proc(request):
	auth = Authentication(request)
	user = auth.get_user()
	pub_questionnaires = Questionnaire.objects.filter(author = user)
	filled_questionnaires = Result.objects.filter(participant_id = user.email)
	return {"created_num": len(pub_questionnaires), "filled_num": len(filled_questionnaires),}
