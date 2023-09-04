

from django import  forms


class ChoiceForm(forms.Form):
    game = forms.CharField(choices=[("d","dice"),('r','rnd_num'), ("c","монетка")])
    count = forms.IntegerField(max_value=1, min_value=64)

