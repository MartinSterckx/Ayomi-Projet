from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.decorators import csrf
from .forms import UserCreationForm  
def home(request):
    return render(request,"connection/home.html")



def informations(request):
	return render(request, "connection/informations.html")




def register_user(request):
	if request.method == 'POST':
	    form = UserCreationForm(request.POST)
	    if form.is_valid():
	        form.save()
	        return HttpResponseRedirect('/informations.html')

	else:
		form = UserCreationForm()
	return render(request, 'registration/login.html', {'form': form})