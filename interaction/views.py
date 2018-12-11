from django.shortcuts import render, get_object_or_404
from interaction.models import Cup, Business, User, Machine

# from django.views import generic

# function_based login restriction
# from django.contrib.auth.decorators import login_required
# @login_required

# class_based login restriction
# from django.contrib.auth.mixins import LoginRequiredMixin
# class MyView(LoginRequiredMixin, View):

def index(request):

    context = {}

    return render(request, 'index.html', context=context)