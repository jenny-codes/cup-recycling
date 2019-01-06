""" cuprecycling URL Configuration """
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from interaction.views import registration

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='/interaction/', permanent=True)),   # home page
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('interaction/', include('interaction.urls')),
    path('login-success/', registration.login_success, name='login_success'),
    path('accounts/signup/intro/', registration.signup_intro, name='signup_intro'),
    path('accounts/signup/customer/', registration.CustomerSignUpView.as_view(), name='customer_signup'),
    path('accounts/signup/business/', registration.BusinessSignUpView.as_view(), name='business_signup'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)