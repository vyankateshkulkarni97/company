from django.shortcuts import render , HttpResponse # python 67 video
from.models import Student 
# Create your views here.
# views:-
    # -class based view
    # - Function based views


    # error 404( page not found) 404 is:- client side error
    # 200 (ok/success)
    # 5XX :- server side error
    # 500 :- internal server Error :- side error
    # 301 :- redirect
# def welcome(request):
    # print(request.GET.get("name"))
    # print(request.GET)
    # studs =Student.objects.get(id=7)
    # print(request.__dict__) # dict print
    
    # studs =list(Student.objects.values("name"))
    # print(studs)
    # final_studs = list(map(lambda X:X["name"],studs))
    # return HttpResponse(f"Welcome to the django application...!{final_studs}")

# python 68 video 18/12/22
    # print(request.method) # GET
    # print(request.user)
    
def welcome(request):
    return render(request,"home.html")

    
# query params :- Query parameter
 