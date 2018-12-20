from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import CupUser, Cup, Group
from IPython import embed

class CustomerSignUpForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )
    email = forms.EmailField(label = "Email")
    phone_number = forms.CharField(label="Phone number")

    class Meta(UserCreationForm.Meta):
        model = CupUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
        
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
        fields = ('title','username', 'email', 'phone_number', 'address')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_business = True
        group = Group.objects.get(name='Business')       
        if commit:
            user.save()
            group.user_set.add(user)
        return user

# FIX
class CupUserChangeForm(UserChangeForm):

    class Meta:
        model = CupUser
        fields = ('username', 'email')