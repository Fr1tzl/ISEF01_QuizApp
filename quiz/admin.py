from django.contrib import admin
from .models import Kurs,Frage,RichtigOderFalsch,Ergebnis,MeldungMCFragen,MeldungRFFragen

# Register your models here.

admin.site.register(Kurs)
admin.site.register(Frage)
admin.site.register(RichtigOderFalsch)
admin.site.register(Ergebnis)
admin.site.register(MeldungMCFragen)
admin.site.register(MeldungRFFragen)