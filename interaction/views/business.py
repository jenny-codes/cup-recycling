from interaction.views import * 
from interaction.forms import BusinessRequestCupsForm, BusinessReceiveCupsForm, BusinessAssignCupsForm

class BusinessCupListView(LoginRequiredMixin, ListView):
    """列出店家的租借杯紀錄，可以跟 admin 要求杯子、將杯子拿給顧客、拿回杯子"""
    model = Cup
    template_name = 'business_record.html'
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        """ when a business assigns a cup to a user, create a Record and update Cup model"""
        form = BusinessAssignCupsForm(request.POST)
        if form.is_valid():
            cup = Cup.objects.filter(id=form.cleaned_data['cup_id'])
            customer = CupUser.objects.get(id=form.cleaned_data['customer'])
            record = Record(cup=cup.first(), source=request.user, user=customer)
            record.save()
            cup.update(carrier = customer, status = 'o', carrier_type = 'u')

        return HttpResponseRedirect(reverse('business-manage-cups')) 

    def get_queryset(self):
        return Cup.objects.filter(carrier=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(BusinessCupListView, self).get_context_data(**kwargs)
        form = BusinessAssignCupsForm()
        context['form'] = form
        context["n_cups"] = Cup.objects.filter(carrier=self.request.user).count()
        return context

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