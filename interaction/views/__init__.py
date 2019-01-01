from interaction.models import Cup, CupUser, Record
from django.views.generic import CreateView, ListView

# Template 相關
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

# Login 權限相關
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from interaction.decorators import customer_required, business_required

# Debugging
from IPython import embed