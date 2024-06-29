
from django.shortcuts import render # type: ignore
from django.http import HttpResponse

def wish(request):
    
    return render(request, 'Index.html')

#def wish(request):
#    message='<h1>Hi Buddy how are you</h1>'
#   return HttpResponse(message)






# Create your views here.s
# #http://127.0.0.1:8000/wise 
#HTTP Response
