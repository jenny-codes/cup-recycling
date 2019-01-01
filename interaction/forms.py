from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import CupUser, Cup, Group
from IPython import embed

class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CupUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
    @transaction.atomic
    def save(self, commit=True):
        print('forms/save')
        user = super().save(commit=False)
        user.is_customer = True
        group = Group.objects.get(name='Customers')
        if commit:
            user.save()
            group.user_set.add(user)
        return user

class BusinessSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CupUser
        fields = ('title','username', 'password1', 'password2', 'email', 'phone_number', 'address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_business = True
        group = Group.objects.get(name='Business')       
        if commit:
            user.save()
            group.user_set.add(user)
        return user


""" Business-related forms start """
class BusinessRequestCupsForm(forms.Form):
    cups_needed = forms.IntegerField(label='需要杯子的數量')

class BusinessReceiveCupsForm(forms.Form):
    cup_received = forms.IntegerField(label='收到杯子的 ID')

class BusinessAssignCupsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BusinessAssignCupsForm, self).__init__(*args, **kwargs) 
        self.fields['cup_id'] = forms.IntegerField(min_value=1, widget = forms.HiddenInput())
        self.fields['customer'] = forms.ChoiceField(choices=self.build_customer_selection())
        
    def build_customer_selection(self):
        customers = []
        for customer in CupUser.objects.filter(is_customer = True):
            customers.append((customer.id, customer.name))
        return customers

""" Business-related forms end """

# FIX
class CupUserChangeForm(UserChangeForm):
    class Meta:
        model = CupUser
        fields = ('username', 'email')

    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )
