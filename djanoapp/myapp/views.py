from django.shortcuts import render
import datetime
from django.template import loader
from myapp.functions.functions import handle_uploaded_file
from myapp.forms import StudentForm
from myapp.forms import EmployeeForm
from django.http import HttpResponse

from myapp.models import Employee
def emp1(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
        return render(request,'index2.html',{'form':form})

def losipr(request):
    template =loader.get_template('losipr.html')
    return render(request,"losipr.html")


def index11(request):
    if request.method == 'POST':
        student = StudentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File Uploaded succesfully")
    else:
        student= StudentForm()
        return render(request,'index2.html',{'form':student})


def index(request):
    template= loader.get_template('index.html')
    return render(request,'index.html')

def mi(request):
    template= loader.get_template('mi.html')
    return render(request,'mi.html')
def index1(request):
    template = loader.get_template('index1.html')
    return render(request,"index1.html")
def oppo(request):
    template = loader.get_template('oppo.html')
    return render(request,"oppo.html")
def vivo(request):
    template = loader.get_template('vivo.html')
    return render(request,"vivo.html")
def find(request):
    template = loader.get_template("find.html")
    return render(request,"find.html")
def find1(request):
    a=int(request.GET.get('num',None))
    if a%2==0:
        html="<html><body><h3>even is %s.</h3></body></html>"%a
    else:
        html="<html><body><h3>odd is %s.</h3></body></html>"%a
    return HttpResponse(html)
def find2(request):
    a = int(request.GET.get('num1', None))
    b = int(request.GET.get('num2', None))
    c=a+b
    # html="<html><body><h2>The sum is %s</h2></body></html>"%c
    return HttpResponse(html)


def hello(request):
    return HttpResponse("<h2>Hello,Welcome to django </h2>")
def gm(request):
    return HttpResponse("<h1> Good Morning Shubham</h1>")
def gn(request1):
    return HttpResponse("<h2> Good night Subham Singh</h2>")
def indexdate(request):
    now = datetime.datetime.now()
    html= "<html><body><h3> Now time is %s</h3></body></html>"%now
    return HttpResponse(html)
def eveodd(request):
    num =11
    if num%2==0:
        message="<html><body><h2> The number %s is even </h2></body></html>"%num
        return HttpResponse(message)
    else:
        message = "<html><body><h2> The number %s is odd </h2></body></html>" % num
        return HttpResponse(message)

def setsession(request):
    request.session['sname'] = 'star'
    request.session['semail'] = 'shubhamashish1000@gmail.com'
    return HttpResponse("session is set")
def getsession1(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname+ " " +studentemail)
def setcookie(request):
    response=HttpResponse("Cookie set")
    response.set_cookie('java-tutorial','javapoint.com')
    return response
def getcookie(request):
    tutorial=request.COOKIES['java-tutorial1']
    return HttpResponse("java-tutorials @:"+ tutorial)
