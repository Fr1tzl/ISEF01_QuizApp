from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import AccessMixin

from .models import Kurs, Frage, RichtigOderFalsch, Ergebnis, MeldungMCFragen, MeldungRFFragen
from .forms import TestSelectForm
from .forms import MeldungMCFrageForm
from .forms import MeldungRFFrageForm

import random
from django.db.models import Count
from django.db.models import Sum

from urlparams.redirect import param_redirect #
from django.contrib import messages
from django.shortcuts import redirect

# views


class AuthListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    permission_denied_message = 'Keine Berechtigung'

class AuthDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    permission_denied_message = 'Keine Berechtigung'

class AuthCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    permission_denied_message = 'Keine Berechtigung'
	
class AuthUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    permission_denied_message = 'Keine Berechtigung'

class AuthDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    permission_denied_message = 'Keine Berechtigung'

class KursHome(AuthListView): 
    model = Kurs
    template_name = 'kurs/kurs_home.html'
    permission_required = ('quiz.view_kurs')

class KursCreate(AuthCreateView):
    model = Kurs
    template_name = 'kurs/kurs_create.html'
    fields = '__all__'
    success_url = reverse_lazy('kurs_start')
    permission_required = ('quiz.add_kurs')

class KursDetail(AuthDetailView):
    model = Kurs
    template_name = 'kurs/kurs_detail.html'
    permission_required = ('quiz.view_kurs')

class KursUpdate(AuthUpdateView):
    model = Kurs
    template_name = 'kurs/kurs_update.html'
    fields = '__all__'
    permission_required = ('quiz.change_kurs')
   	
class KursDelete(AuthDeleteView):
    model = Kurs
    template_name = 'kurs/kurs_delete.html'
    success_url = reverse_lazy('kurs_start')
    permission_required = ('quiz.delete_kurs')
	
class FrageHome(AuthListView): 
    model = Frage
    template_name = 'frage/frage_home.html'
    permission_required = ('quiz.view_frage')
    def get_queryset(self):
        return Frage.objects.filter(freigegeben = True)
	
class FrageNichtFreigegeben(AuthListView): 
    model = Frage
    template_name = 'frage/frage_unapproved.html'
    permission_required = ('quiz.view_frage')
	
    def get_queryset(self):
        return Frage.objects.raw('select * from quiz_frage where freigegeben = False')
	
class FrageCreate(AuthCreateView):
    model = Frage
    template_name = 'frage/frage_create.html'
    #fields = '__all__'
    fields = ['name','kurs','antwort1','antwort1richtig','antwort2','antwort2richtig','antwort3','antwort3richtig','antwort4','antwort4richtig']
    success_url = reverse_lazy('frage_start')
    permission_required = ('quiz.add_frage')
	
class FrageDetail(AuthDetailView):
    model = Frage
    template_name = 'frage/frage_detail.html'
    permission_required = ('quiz.view_frage')

class FrageUpdate(AuthUpdateView):
    model = Frage
    template_name = 'frage/frage_update.html'
    fields = '__all__'
    permission_required = ('quiz.change_frage')
	
class FrageDelete(AuthDeleteView):
    model = Frage
    template_name = 'frage/frage_delete.html'
    success_url = reverse_lazy('frage_start')
    permission_required = ('quiz.delete_frage')
	
class RichtigOderFalschHome(AuthListView): 
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_home.html'
    permission_required = ('quiz.view_richtigoderfalsch')
    def get_queryset(self):
        return RichtigOderFalsch.objects.filter(freigegeben = True)
	
class RichtigOderFalschNichtFreigegeben(AuthListView): 
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_unapproved.html'
    permission_required = ('quiz.view_richtigoderfalsch')
	
    def get_queryset(self):
        return Frage.objects.raw('select * from quiz_richtigoderfalsch where freigegeben = False')
	
class RichtigOderFalschCreate(AuthCreateView):
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_create.html'
    fields = ['name','kurs','behauptungrichtig']
    success_url = reverse_lazy('richtigoderfalsch_start')
    permission_required = ('quiz.add_richtigoderfalsch')
	
class RichtigOderFalschDetail(AuthDetailView):
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_detail.html'
    permission_required = ('quiz.view_richtigoderfalsch')

class RichtigOderFalschUpdate(AuthUpdateView):
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_update.html'
    fields = '__all__'
    permission_required = ('quiz.change_richtigoderfalsch')
	
class RichtigOderFalschDelete(AuthDeleteView):
    model = RichtigOderFalsch
    template_name = 'richtigoderfalsch/richtigoderfalsch_delete.html'
    success_url = reverse_lazy('richtigoderfalsch_start')
    permission_required = ('quiz.delete_richtigoderfalsch')
	
class ErgebnisHome(AuthListView): 
    model = Ergebnis
    template_name = 'ergebnis/ergebnis_home.html'
    permission_required = ('quiz.view_ergebnis')

class ErgebnisDetail(AuthListView): 
    model = Ergebnis
    template_name = 'ergebnis/ergebnis_detail.html'
    permission_required = ('quiz.view_ergebnis')
	
class ErgebnisTopPunkte(AuthListView): 
    model = Ergebnis
    template_name = 'ergebnis/ergebnis_toppunkte.html'
    fields = '__all__'
    permission_required = ('quiz.view_ergebnis')

    def get_queryset(self):
        return Ergebnis.objects.filter().order_by('-punkte')[:10]
		
class ErgebnisTopGroupByPunkte(AuthListView): 
    model = Ergebnis
    template_name = 'ergebnis/ergebnis_topgroupbypunkte.html'
    fields = '__all__'
    permission_required = ('quiz.view_ergebnis')

    def get_queryset(self):
        return Ergebnis.objects.raw('select id, benutzername, sum(punkte) as punkte from quiz_ergebnis group by benutzername order by punkte DESC')

class ErgebnisTopMCGroupByPunkte(AuthListView): 
    model = Ergebnis
    template_name = 'ergebnis/ergebnis_topmcgroupbypunkte.html'
    fields = '__all__'
    permission_required = ('quiz.view_ergebnis')

    def get_queryset(self):
        return Ergebnis.objects.raw('select id, benutzername, sum(punkte) as punkte from quiz_ergebnis where testmodus="mc" group by benutzername order by punkte DESC') 
		
class ErgebnisTopRFGroupByPunkte(AuthListView): 
    model = Ergebnis
    template_name = 'ergebnis/ergebnis_toprfgroupbypunkte.html'
    fields = '__all__'
    permission_required = ('quiz.view_ergebnis')

    def get_queryset(self):
        return Ergebnis.objects.raw('select id, benutzername, sum(punkte) as punkte from quiz_ergebnis where testmodus="rf" group by benutzername order by punkte DESC')

class ErgebnisMCTopPunkte(AuthListView): 
    model = Ergebnis
    template_name = 'ergebnis/ergebnis_mctoppunkte.html'
    fields = '__all__'
    permission_required = ('quiz.view_ergebnis')

    def get_queryset(self):
        return Ergebnis.objects.filter(testmodus='mc').order_by('-punkte')[:10]

class ErgebnisRFTopPunkte(AuthListView): 
    model = Ergebnis
    template_name = 'ergebnis/ergebnis_rftoppunkte.html'
    fields = '__all__'
    permission_required = ('quiz.view_ergebnis')

    def get_queryset(self):
        return Ergebnis.objects.filter(testmodus='rf').order_by('-punkte')[:10]

class ErgebnisDetail(AuthDetailView):
    model = Ergebnis
    template_name = 'ergebnis/ergebnis_detail.html'
    permission_required = ('quiz.view_ergebnis')
	
class MeldungMCFragenHome(AuthListView): 
    model = MeldungMCFragen
    template_name = 'meldungmcfrage/meldungmcfragen_home.html'
    permission_required = ('quiz.view_meldungmcfragen')

class MeldungMCFragenDetail(AuthDetailView): 
    model = MeldungMCFragen
    template_name = 'meldungmcfrage/meldungmcfragen_detail.html'
    permission_required = ('quiz.view_meldungmcfragen')
	
class MeldungMCFragenDelete(AuthDeleteView):
    model =  MeldungMCFragen
    template_name = 'meldungmcfrage/meldungmcfragen_delete.html'
    success_url = reverse_lazy('meldungmcfragen')
    permission_required = ('quiz.delete_meldungmcfragen')
	
class MeldungMCFragenUpdate(AuthUpdateView):
    model = MeldungMCFragen
    template_name = 'meldungmcfrage/meldungmcfragen_update.html'
    fields = '__all__'
    permission_required = ('quiz.change_meldungmcfragen')
	
class MeldungMCFragenUpdateNichtGelesen(AuthListView): 
    model = MeldungMCFragen
    template_name = 'meldungmcfrage/meldungmcfragen_unread.html'
    fields = '__all__'
    permission_required = ('quiz.view_meldungmcfragen')

    def get_queryset(self):
        return MeldungMCFragen.objects.raw('select id, frage, nachricht, benutzername, frageid_id, kursid_id, kursname, gelesen FROM quiz_meldungmcfragen where gelesen = "0"')
		
class MeldungRFFragenHome(AuthListView): 
    model = MeldungRFFragen
    template_name = 'meldungrffrage/meldungrffragen_home.html'
    permission_required = ('quiz.view_meldungrffragen')

class MeldungRFFragenDetail(AuthDetailView): 
    model = MeldungRFFragen
    template_name = 'meldungrffrage/meldungrffragen_detail.html'
    permission_required = ('quiz.view_meldungrffragen')
	
class MeldungRFFragenDelete(AuthDeleteView):
    model =  MeldungRFFragen
    template_name = 'meldungrffrage/meldungrffragen_delete.html'
    success_url = reverse_lazy('meldungrffragen')
    permission_required = ('quiz.delete_meldungrffragen')
	
class MeldungRFFragenUpdate(AuthUpdateView):
    model = MeldungRFFragen
    template_name = 'meldungrffrage/meldungrffragen_update.html'
    fields = '__all__'
    permission_required = ('quiz.change_meldungrffragen')

class MeldungRFFragenUpdateNichtGelesen(AuthListView): 
    model = MeldungRFFragen
    template_name = 'meldungrffrage/meldungrffragen_unread.html'
    fields = '__all__'
    permission_required = ('quiz.view_meldungrffragen')

    def get_queryset(self):
        return MeldungRFFragen.objects.raw('select id, frage, nachricht, benutzername, frageid_id, kursid_id, kursname, gelesen FROM quiz_meldungrffragen where gelesen = "0"')

@login_required(login_url='/accounts/login/')
def index(request):
    """View function for home page of site."""

    num_kurs = Kurs.objects.all().count()
    num_mcfrage = Frage.objects.all().count()
    num_rffrage = RichtigOderFalsch.objects.all().count()


    context = {
        'num_kurs': num_kurs,
        'num_mcfrage': num_mcfrage,
        'num_rffrage': num_rffrage
    }

    return render(request, 'index.html', context=context)

@login_required(login_url='/accounts/login/')	
def MCTestSelect(request):
  if request.method == "POST":
    form = TestSelectForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data.get("kurs")
        questioncount = form.cleaned_data.get("questioncount")
        mcfragenanzahlkurs=Frage.objects.filter(kurs = data.id, freigegeben = True).count()
        print(data.id)
        print(data.name)
        print(questioncount)
        print(mcfragenanzahlkurs)
        context = {
            'modulid':data.id,
            'modulname':data.name,
            'questioncount':questioncount
        }
        if mcfragenanzahlkurs < 1:
           print("keine Fragen verfügbar für",data.name)
           messages.error(request, 'Es sind keine Fragen für %s verfügbar'%data.name)
           messages.error(request, form.errors)
        else:
           return param_redirect(request, 'mctest_start', data.id, questioncount)
	  
  else:
      form = TestSelectForm()
  return render(request, 'mctest/mctest_select.html', {'form': form})
  
@login_required(login_url='/accounts/login/')	
def RFTestSelect(request):
  if request.method == "POST":
    form = TestSelectForm(request.POST)
    if form.is_valid():

        data = form.cleaned_data.get("kurs")
        questioncount = form.cleaned_data.get("questioncount")
        rffragenanzahlkurs=RichtigOderFalsch.objects.filter(kurs = data.id, freigegeben = True).count()
        print(data.id)
        print(data.name)
        print(questioncount)
        print(rffragenanzahlkurs)
        context = {
            'modulid':data.id,
            'modulname':data.name,
            'questioncount':questioncount
        }
        if rffragenanzahlkurs < 1:
           print("keine Fragen verfügbar für",data.name)
           messages.error(request, 'Es sind keine Fragen für %s verfügbar'%data.name)
           messages.error(request, form.errors)
        else:
           return param_redirect(request, 'rftest_start', data.id, questioncount)
	  
  else:
      form = TestSelectForm()
  return render(request, 'rftest/rftest_select.html', {'form': form})

@login_required(login_url='/accounts/login/')	
def MeldungMCFrageSelect(request):
  if request.method == "POST":
    form = MeldungMCFrageForm(request.POST)
    if form.is_valid():
        kurs = form.cleaned_data.get("kurs")
        frage = form.cleaned_data.get("frage")
        nachricht = form.cleaned_data.get("nachricht")
        print(kurs)
        print(kurs.id)
        print(frage.id)
        print(frage)
        print(nachricht)
        reg = MeldungMCFragen(kursname=kurs.name, kursid=kurs, frageid=frage, frage=frage.name, nachricht=nachricht, benutzername=request.user.username )
        reg.save()
        return render(request,'index.html')

  else:
      form = MeldungMCFrageForm()
  return render(request, 'meldungmcfrage/meldungmcfrage.html', {'form': form})
  
@login_required(login_url='/accounts/login/')	
def MeldungRFFrageSelect(request):
  if request.method == "POST":
    form = MeldungRFFrageForm(request.POST)
    if form.is_valid():
        kurs = form.cleaned_data.get("kurs")
        frage = form.cleaned_data.get("frage")
        nachricht = form.cleaned_data.get("nachricht")
        print(kurs)
        print(kurs.id)
        print(frage.id)
        print(frage)
        print(nachricht)
        regrf = MeldungRFFragen(kursname=kurs.name, kursid=kurs, frageid=frage, frage=frage.name, nachricht=nachricht, benutzername=request.user.username )
        regrf.save()
        return render(request,'index.html')

  else:
      form = MeldungRFFrageForm()
  return render(request, 'meldungrffrage/meldungrffrage.html', {'form': form})

def LadeMCFragen(request):
    kurs_id = request.GET.get('kurs')
    fragen = Frage.objects.filter(kurs=kurs_id, freigegeben = True).order_by('name')
    return render(request, 'meldungmcfrage/meldungmcfrage_dropdownlist.html', {'fragen': fragen})

def LadeRFFragen(request):
    kurs_id = request.GET.get('kurs')
    fragen = RichtigOderFalsch.objects.filter(kurs=kurs_id, freigegeben = True).order_by('name')
    return render(request, 'meldungrffrage/meldungrffrage_dropdownlist.html', {'fragen': fragen})

@login_required(login_url='/accounts/login/')	  
def MCTestStart(request, arg1, arg2):
    kurs=Kurs.objects.filter(id = arg1)
    for k in kurs:
        kursname=k.name
        kursbeschreibung=k.beschreibung
    print(kurs)
    print(kursbeschreibung)
    qcount=int(arg2)
    global mcfragenrandom
	
    if request.method == 'POST':
        print(request.POST)

        mcfragen=mcfragenrandom
        mcfragenanzahl=len(mcfragen)
		
        punkte=0
        falsch=0
        korrekt=0
        total=0
		
        for f in mcfragen:
            total+=1
            answers=(request.POST.getlist(f.name))
            answercount=len(answers)
            boolantwort1=bool(False)
            boolantwort2=bool(False)
            boolantwort3=bool(False)
            boolantwort4=bool(False)

            if '1' in str(answers):
                boolantwort1=bool(True)
            if '2' in str(answers):
                boolantwort2=bool(True)
            if '3' in str(answers):
                boolantwort3=bool(True)
            if '4' in str(answers):
                boolantwort4=bool(True)

            if bool(boolantwort1) is bool(f.antwort1richtig) and bool(boolantwort2) is bool(f.antwort2richtig) and bool(boolantwort3) is bool(f.antwort3richtig) and bool(boolantwort4) is bool(f.antwort4richtig):
                punkte+=1
                korrekt+=1
            else:
                falsch+=1

        punkte=korrekt*1
        prozent = punkte/(total*1) *100
        context = {
            'punkte':punkte,
            'mcfragenanzahl':mcfragenanzahl,
            'time': request.POST.get('timer'),
            'korrekt':korrekt,
            'falsch':falsch,
            'prozent':prozent,
            'total':total
        }
        reg = Ergebnis(testmodus='mc', benutzername=request.user.username, kursid=arg1, kursname=kursname, zeitsekunden=request.POST.get('timer'), datum=['%d-%m-%Y'], punkte=punkte, fragentotal=mcfragenanzahl, fragenkorrekt=korrekt, fragenfalsch=falsch )
        reg.save()
        return render(request,'mctest/mctest_result.html',context)
    else:
        print(arg1)
        print(arg2)
		
        mcfragen=Frage.objects.filter(kurs = arg1, freigegeben = True)
        randompool= list(mcfragen)
        random.shuffle(randompool)
        mcfragenrandom=randompool[:qcount]
        mcfragenanzahl=len(mcfragenrandom)
        context = {
            'mcfragen':mcfragenrandom,
            'kursname':kursname,
			'kursbeschreibung':kursbeschreibung
        }
        return render(request,'mctest/mctest_start.html',context)
		
		
@login_required(login_url='/accounts/login/')	  
def RFTestStart(request, arg1, arg2):
    kurs=Kurs.objects.filter(id = arg1)
    for k in kurs:
        kursname=k.name
        kursbeschreibung=k.beschreibung
    print(kurs)
    print(kursbeschreibung)
    qcount=int(arg2)
    global rffragenrandom

    if request.method == 'POST':
        print(request.POST)

        rffragen=rffragenrandom
        rffragenanzahl=len(rffragen)

        punkte=0
        falsch=0
        korrekt=0
        total=0

        for rf in rffragen:
            total+=1
            answers=request.POST.get(rf.name)
            boolantwort=bool(False)

            if '1' in str(answers):
                boolantwort=bool(True)
            if '2' in str(answers):
                boolantwort=bool(False)
            print(boolantwort)

            print("Richige Antwort")
            print(rf.behauptungrichtig)


#

            if bool(boolantwort) is bool(rf.behauptungrichtig):
                punkte+=1
                korrekt+=1
            else:
                falsch+=1

        punkte=korrekt*1
        prozent = punkte/(total*1) *100
        context = {
            'punkte':punkte,
            'rffragenanzahl':rffragenanzahl,
            'time': request.POST.get('timer'),
            'korrekt':korrekt,
            'falsch':falsch,
            'prozent':prozent,
            'total':total
        }
        reg = Ergebnis(testmodus='rf', benutzername=request.user.username, kursid=arg1, kursname=kursname, zeitsekunden=request.POST.get('timer'), datum=['%d-%m-%Y'], punkte=punkte, fragentotal=rffragenanzahl, fragenkorrekt=korrekt, fragenfalsch=falsch )
        reg.save()
        return render(request,'rftest/rftest_result.html',context)
    else:
        print(arg1)
        print(arg2)		

        rffragen=RichtigOderFalsch.objects.filter(kurs = arg1, freigegeben = True)
        randompool= list(rffragen)
        random.shuffle(randompool)
        rffragenrandom=randompool[:qcount]
        rffragenanzahl=len(rffragenrandom)
		
        context = {
			'rffragen':rffragenrandom,
            'kursname':kursname,
			'kursbeschreibung':kursbeschreibung
        }
        return render(request,'rftest/rftest_start.html',context)