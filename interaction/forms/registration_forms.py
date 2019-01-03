from interaction.forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
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

# FIX
class CupUserChangeForm(UserChangeForm):
    class Meta:
        model = CupUser
        fields = ('username', 'email')