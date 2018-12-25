from interaction.models import Cup, CupUser, Record
from django.views.generic import CreateView, ListView
from interaction.forms import CustomerSignUpForm, BusinessSignUpForm, BusinessRequestCupsForm, BusinessReceiveCupsForm

# Template 相關
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
 

# Login 權限相關
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from interaction.decorators import customer_required, business_required

def index(request):

    context = {}

    return render(request, 'index.html', context=context)

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

class CustomerRecordListView(LoginRequiredMixin, ListView):
    """列出使用者的租借杯紀錄"""
    model = Record
    template_name ='customer_record.html'
    context_object_name = 'checked_out_records' # default is 'record_list'
    paginate_by = 10
    
    def get_queryset(self):
        return Record.objects.filter(user=self.request.user).order_by('loaned_out_at')

    # def get_context_data(self, **kwargs):
    #     context = super(CustomerRecordListView, self).get_context_data(**kwargs)
    #     cups_returned = Record.objects.filter(source=self.request.user).order_by('timestamp')
    #     context['returned_records'] = cups_returned
    #     return context

class BusinessCupListView(LoginRequiredMixin, ListView):
    """列出店家的租借杯紀錄，可以跟 admin 要求杯子、將杯子拿給顧客、拿回杯子"""
    model = Cup
    template_name = 'business_record.html'
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        """ when a business assigns a cup to a user, create a Record and update Cup model"""
        if request.POST['user_id'].isdigit() and int(request.POST['user_id']) > 0:
            user = CupUser.objects.get(id=int(request.POST['user_id']))
            if user and user.is_customer:
                cup = Cup.objects.filter(id=request.POST['cup_id'])
                record = Record(cup=cup.first(), source=request.user, user=user)
                record.save()
                cup.update(carrier = user, status = 'o', carrier_type = 'u')
            else:
                print('輸入錯誤：這個 ID 沒有人，或不是顧客喔')
        else:
            print('輸入錯誤：只能輸入正整數哦')

        return HttpResponseRedirect(reverse('business-manage-cups')) 

    def get_queryset(self):
        return Cup.objects.filter(carrier=self.request.user)

    # def get_context_data(self, **kwargs):
    #     context = super(BusinessCupListView, self).get_context_data(**kwargs)
    #     cup_list = Cup.objects.filter(carrier=self.request.user)
    #     context['cup_list'] = cup_list
    #     return context

@business_required
def request_cups(request):
    if request.method == 'POST':
        # def in forms.py
        form = BusinessRequestCupsForm(request.POST)
        if form.is_valid():
            n_cups = int(form.cleaned_data['cups_needed'])
            Cup.objects.batch_create(carrier=request.user, size=n_cups)  
            return HttpResponseRedirect(reverse('business-manage-cups'))          

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BusinessRequestCupsForm()
        return render(request, 'business_request_cups.html', {'form': form})

@business_required
def distribute_cups(request):
    if request.method == 'POST':
        #def in forms.py
        form = BusinessReceiveCupsForm(request.POST)
        if form.is_valid():
            cup_received = Cup.objects.get(id=form.cleaned_data['cup_received'])
            Cup.objects.batch_create(carrier=request.user, size=n_cups)  
            return HttpResponseRedirect(reverse('business-manage-cups'))          

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BusinessRequestCupsForm()
        return render(request, 'business_request_cups.html', {'form': form})

@business_required
def receive_cups(request):
    """ when busiess receives a cup, update Record & Cup models """
    if request.method == 'POST':
        #def in forms.py
        form = BusinessReceiveCupsForm(request.POST)
        if form.is_valid():
            cup_received = Cup.objects.filter(id=form.cleaned_data['cup_received'])
            if cup_received.count() != 0:
                cup_received.update(carrier = request.user, status = 'a', carrier_type = 'b' )
                record = Record.objects.filter(cup=cup_received)
                if record.count() != 0:
                    record.update(destination = request.user) 
            return HttpResponseRedirect(reverse('business-manage-cups'))          

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BusinessReceiveCupsForm()
        return render(request, 'business_receive_cups.html', {'form': form})


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