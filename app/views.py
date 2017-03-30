from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views import View


############################## Views for Registering a user with no social media profile ############################### 
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
 
    return render(request, 'registration/register.html', {'form': form})
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )


############################################# View for logging out ######################################################


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
# @login_required
# def home(request):
#     return render(request, 'home.html',{ 'user': request.user })

################################################# Home View ###########################################################

class HomeView(View):

    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'home.html', {'user': request.user })

################################################ Geolocating #########################################################

class Mylocation(View):

    @method_decorator(login_required)
    def get(self, request):
        pass