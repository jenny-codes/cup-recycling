from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import CupUser, Cup, Group

class CustomerSignUpForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta(UserCreationForm.Meta):
        model = CupUser
        fields = ('username', 'email', 'password', 'phone_number')
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        group = Group.objects.get(name='Customers')
        group.add(user)
        user.save()
        customer = customer.objects.create(user=user)
        customer.interests.add(*self.cleaned_data.get('interests'))
        return user

class BusinessSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CupUser
        fields = ('username', 'email', 'password', 'phone_number', 'address')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_business = True
        group = Group.objects.get(name='Business')
        group.add(user)        
        return user

# FIX
class CupUserChangeForm(UserChangeForm):

    class Meta:
        model = CupUser
        fields = ('username', 'email')