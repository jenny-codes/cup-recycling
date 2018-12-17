from django.shortcuts import render, get_object_or_404
from interaction.models import *

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


from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from .forms import CustomerSignUpForm, BusinessSignUpForm
from django.shortcuts import get_object_or_404, render
from .decorators import customer_required, business_required

class CustomerSignUpView(CreateView):
    model = CupUser
    form_class = CustomerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class BusinessSignUpView(CreateView):
    model = CupUser
    form_class = BusinessSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'business'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedCupsByCustomerListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Cup
    template_name ='customer_cups.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Cup.objects.filter(carrier=self.request.user).filter(status__exact='o')


# @login_required
# @business_required 
# def take_quiz(request, pk):
#     quiz = get_object_or_404(Quiz, pk=pk)
#     student = request.user.student

#     # body of the view...

#     return render(request, 'classroom/students/take_quiz_form.html', {
#         'quiz': quiz,
#         'question': question,
#         'form': form,
#         'progress': progress
#     })