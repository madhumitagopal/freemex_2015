from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def init(request):
    t = get_template('login.html')
    html = t.render(Context())
    return HttpResponse(html)

'''def init(request):

	if request.user.is_authenticated():
		return mainpage(request)#,'main/logged.html',{"username":request.user.username})
	else:
		return render(request,'startpage/start.html')
from django.contrib.auth.decorators import login_required '''

def call_to_register(request):
    t = get_template('register.html')
    html = t.render(Context())
    return HttpResponse(html)
def register(request)
    username = request.POST['email']
    password = request.POST['password']
    phone_no=request.POST['phone_number']
