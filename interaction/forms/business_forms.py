from interaction.forms import * 

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