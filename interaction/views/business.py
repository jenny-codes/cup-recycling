from interaction.views import * 

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