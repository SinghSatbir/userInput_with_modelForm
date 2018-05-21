from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from user_app.forms import NewUserForm
from user_app.models import User


def index(request):
    template = loader.get_template('user_app/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def form_view(request):
    template = loader.get_template('user_app/forms.html')
    form_object = NewUserForm()
    if request.method == 'POST':
        form_object = NewUserForm(request.POST)
        if form_object.is_valid():
            form_object.save(commit=True)
            return index(request)
    context = {
        'form_full': form_object
    }
    return HttpResponse(template.render(context, request))


def user_view(request):
    template = loader.get_template('user_app/users.html')
    context = {
        'user_set': User.objects.all()
    }
    return HttpResponse(template.render(context, request))
