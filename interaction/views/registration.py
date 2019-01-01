from interaction.views import * 
from django.views.generic import CreateView
from interaction.forms.registration_forms import CustomerSignUpForm, BusinessSignUpForm

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
        return redirect("business-manage-cups")

class CustomerSignUpView(CreateView):
    model = CupUser
    form_class = CustomerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        print('get_context_data')
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print('form_valid')
        user = form.save()
        login(self.request, user)
        return redirect("customer-view-cups")

def login_success(request):
    if request.user.is_customer:
        return redirect("customer-view-cups")
    elif request.user.is_business:
        return redirect("business-manage-cups")
    else:
        return redirect("/")