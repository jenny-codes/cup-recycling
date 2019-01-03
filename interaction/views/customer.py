from interaction.views import * 
from interaction.forms.registration_forms import CustomerSignUpForm

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