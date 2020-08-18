from django.http import HttpResponse
from django.shortcuts import render
from .models import companyform
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        f_name = request.POST['name']
        f_email = request.POST['email']
        f_comments = request.POST['comments']
        c = User.objects.filter(username=f_email)
        user = User.objects.create_user(username = f_email, email = f_email, comments = f_comments)
        comp.save()
        c_email = request.user.username
        c = Company.objects.get(email = c_email)
        company = company(username = f_email, email = f_email, comments = f_comments)
        company.save()
    else:
        return render(request,'index.html')