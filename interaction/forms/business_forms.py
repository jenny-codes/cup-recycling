from interaction.forms import * 

class BusinessRequestCupsForm(forms.Form):
    cups_needed = forms.IntegerField(label='需要杯子的數量')

class BusinessReceiveCupsForm(forms.Form):
    cup_received = forms.IntegerField(label='收到杯子的 ID')

    def cup_is_elligible_to_return(self, cup):
        newest_record = Record.objects.filter(cup=cup).last()
        if newest_record:
            if not newest_record.destination:
                return True
        return False 

    def clean_cup_received(self):
        data = self.cleaned_data['cup_received']
        cup_received = Cup.objects.filter(id=data).first()

        # 如果杯子存在並且 Record 中有此杯子還未歸還的紀錄
        if bool(cup_received) and self.cup_is_elligible_to_return(cup_received):
            return cup_received
        else:
            raise forms.ValidationError("沒有這個杯子！重新輸入")

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