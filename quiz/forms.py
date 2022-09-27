from django import forms
from .models import Kurs, Frage, RichtigOderFalsch

COUNT_CHOICE= [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('10', '10'),
    ('15', '15'),
    ('20', '20')
    ]

class TestSelectForm(forms.Form):
    kurs = forms.ModelChoiceField(queryset=Kurs.objects.all(),required=True)
    questioncount = forms.IntegerField(label='Wähle die maximale Anzahl der Fragen?', widget=forms.Select(choices=COUNT_CHOICE))
	
class MeldungMCFrageForm(forms.Form):
    kurs = forms.ModelChoiceField(queryset=Kurs.objects.all(),required=True)								 
    frage = forms.ModelChoiceField(queryset=Frage.objects.all(),required=True)
    nachricht = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={"rows":5, "cols":100}))

	
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['frage'].queryset = Frage.objects.none()
        if 'kurs' in self.data:
            try:
                kurs_id = int(self.data.get('kurs'))
                self.fields['frage'].queryset = Frage.objects.filter(kurs=kurs_id, freigegeben = True).order_by('name')
            except (ValueError, TypeError):
                pass 

class MeldungRFFrageForm(forms.Form):
    kurs = forms.ModelChoiceField(queryset=Kurs.objects.all(),required=True)								 
    frage = forms.ModelChoiceField(queryset=RichtigOderFalsch.objects.all(),required=True)
    nachricht = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={"rows":5, "cols":100}))

	
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['frage'].queryset = RichtigOderFalsch.objects.none()
        if 'kurs' in self.data:
            try:
                kurs_id = int(self.data.get('kurs'))
                self.fields['frage'].queryset = RichtigOderFalsch.objects.filter(kurs=kurs_id, freigegeben = True).order_by('name')
            except (ValueError, TypeError):
                pass 