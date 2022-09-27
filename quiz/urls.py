from django.urls import path
from .views import KursHome
from .views import KursCreate
from .views import KursDetail
from .views import KursUpdate
from .views import KursDelete

from .views import FrageHome
from .views import FrageNichtFreigegeben
from .views import FrageCreate
from .views import FrageDetail
from .views import FrageUpdate
from .views import FrageDelete
from .views import RichtigOderFalschHome
from .views import RichtigOderFalschNichtFreigegeben
from .views import RichtigOderFalschCreate
from .views import RichtigOderFalschDetail
from .views import RichtigOderFalschUpdate
from .views import RichtigOderFalschDelete
from .views import ErgebnisHome
from .views import ErgebnisTopPunkte
from .views import ErgebnisTopGroupByPunkte
from .views import ErgebnisMCTopPunkte
from .views import ErgebnisTopMCGroupByPunkte
from .views import ErgebnisRFTopPunkte
from .views import ErgebnisTopRFGroupByPunkte
from .views import ErgebnisDetail
from .views import index
from .views import MCTestSelect
from .views import RFTestSelect
from .views import MeldungMCFrageSelect
from .views import MeldungRFFrageSelect
from .views import MCTestStart
from .views import RFTestStart
from .views import LadeMCFragen
from .views import LadeRFFragen
from .views import MeldungMCFragenHome
from .views import MeldungMCFragenDetail
from .views import MeldungMCFragenUpdate
from .views import MeldungMCFragenDelete
from .views import MeldungMCFragenUpdateNichtGelesen
from .views import MeldungRFFragenHome
from .views import MeldungRFFragenDetail
from .views import MeldungRFFragenUpdate
from .views import MeldungRFFragenDelete
from .views import MeldungRFFragenUpdateNichtGelesen


urlpatterns = [
	 path('', index, name='index'),
     path('kurs', KursHome.as_view(), name='kurs_start'),
	 path('frage', FrageHome.as_view(), name='frage_start'),
	 path('frage/nichtfreigegeben', FrageNichtFreigegeben.as_view(), name='frage_nichtfreigegeben'),
     path('richtigoderfalsch', RichtigOderFalschHome.as_view(), name='richtigoderfalsch_start'),
     path('richtigoderfalsch/nichtfreigegeben', RichtigOderFalschNichtFreigegeben.as_view(), name='richtigoderfalsch_nichtfreigegeben'),
     path('ergebnis', ErgebnisHome.as_view(), name='ergebnis_start'),
     path('ergebnistoppunkte', ErgebnisTopPunkte.as_view(), name='ergebnis_toppunkte'),
     path('ergebnistopgroupbypunkte', ErgebnisTopGroupByPunkte.as_view(), name='ergebnis_topgroupbypunkte'),
     path('ergebnismctoppunkte', ErgebnisMCTopPunkte.as_view(), name='ergebnis_mctoppunkte'),
     path('ergebnistopmcgroupbypunkte', ErgebnisTopMCGroupByPunkte.as_view(), name='ergebnis_topmcgroupbypunkte'),
     path('ergebnisrftoppunkte', ErgebnisRFTopPunkte.as_view(), name='ergebnis_rftoppunkte'),
     path('ergebnistoprfgroupbypunkte', ErgebnisTopRFGroupByPunkte.as_view(), name='ergebnis_toprfgroupbypunkte'),	 
	 path('mctest', MCTestSelect, name='mctest_select'),
     path('rftest', RFTestSelect, name='rftest_select'),
	 path('mctest/<arg1>', MCTestStart, name='mctest_start'),
	 path('mctest/<arg1>/<arg2>', MCTestStart, name='mctest_start'),
     path('rftest/<arg1>', RFTestStart, name='rftest_start'),
     path('rftest/<arg1>/<arg2>', RFTestStart, name='rftest_start'),
	 path('kurs/neu/', KursCreate.as_view(), name='neuer_kurs'),
	 path('frage/neu/', FrageCreate.as_view(), name='neue_frage'),
     path('richtigoderfalsch/neu/', RichtigOderFalschCreate.as_view(), name='richtigoderfalsch_neue_frage'),
	 path('kurs/<int:pk>/', KursDetail.as_view(), name='kurs_detail'),
	 path('frage/<int:pk>/', FrageDetail.as_view(), name='frage_detail'),
     path('richtigoderfalsch/<int:pk>/', RichtigOderFalschDetail.as_view(), name='richtigoderfalsch_detail'),
     path('ergebnis/<int:pk>/', ErgebnisDetail.as_view(), name='ergebnis_detail'),
	 path('kurs/<int:pk>/update/', KursUpdate.as_view(), name='kurs_update'),
	 path('frage/<int:pk>/update/', FrageUpdate.as_view(), name='frage_update'),
     path('richtigoderfalsch/<int:pk>/update/', RichtigOderFalschUpdate.as_view(), name='richtigoderfalsch_update'),
	 path('kurs/<int:pk>/delete/', KursDelete.as_view(), name='kurs_delete'),
	 path('frage/<int:pk>/delete/', FrageDelete.as_view(), name='frage_delete'),
     path('richtigoderfalsch/<int:pk>/delete/', RichtigOderFalschDelete.as_view(), name='richtigoderfalsch_delete'),
     path('ajax/lade-mcfragen/', LadeMCFragen, name='ajax_lade_mcfragen'), 
     path('ajax/lade-rffragen/', LadeRFFragen, name='ajax_lade_rffragen'), 
     path('meldungmcfrage', MeldungMCFrageSelect, name='meldungmcfrage_select'),
	 path('meldungmcfragen', MeldungMCFragenHome.as_view(), name='meldungmcfragen'),
	 path('meldungmcfragenungelesen', MeldungMCFragenUpdateNichtGelesen.as_view(), name='meldungmcfragen_ungelesen'),
     path('meldungmcfragen/<int:pk>/', MeldungMCFragenDetail.as_view(), name='meldungmcfragen_detail'),
	 path('meldungmcfragen/<int:pk>/update/', MeldungMCFragenUpdate.as_view(), name='meldungmcfragen_update'),
	 path('meldungmcfragen/<int:pk>/delete/', MeldungMCFragenDelete.as_view(), name='meldungmcfragen_delete'),
     path('meldungrffrage', MeldungRFFrageSelect, name='meldungrffrage_select'),
	 path('meldungrffragen', MeldungRFFragenHome.as_view(), name='meldungrffragen'),
     path('meldungrffragen/<int:pk>/', MeldungRFFragenDetail.as_view(), name='meldungrffragen_detail'),
	 path('meldungrffragen/<int:pk>/update/', MeldungRFFragenUpdate.as_view(), name='meldungrffragen_update'),
	 path('meldungrffragen/<int:pk>/delete/', MeldungRFFragenDelete.as_view(), name='meldungrffragen_delete'),
	 path('meldungrffragenungelesen', MeldungRFFragenUpdateNichtGelesen.as_view(), name='meldungrffragen_ungelesen'),
]