from django.db import models
from django.urls import reverse

# Create your models here.

class Kurs(models.Model):
    name = models.CharField(max_length=50,help_text='Geben Sie den Namen des Kurses ein')
    beschreibung = models.CharField(max_length=255,help_text='Geben Sie die Beschreibung des Kurses ein')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kurs_detail', args=[str(self.id)])

class Frage(models.Model):
    name = models.CharField(max_length=255,blank=False,help_text='Geben Sie hier die Frage ein')
    kurs = models.ForeignKey(Kurs,null=True,blank=False,on_delete=models.CASCADE,help_text='Wählen Sie den Kurs, welchem die Frage zugewiesen wird')
    antwort1 = models.CharField(max_length=255,blank=False,null=True,help_text='Geben Sie die Antwort1 der Frage ein')
    antwort1richtig = models.BooleanField(default=False,help_text='Geben Sie an ob Antwort1 richtig ist',verbose_name="Antwort1 richtig?")
    antwort2 = models.CharField(max_length=255,blank=False,null=True,help_text='Geben Sie die Antwort2 der Frage ein')
    antwort2richtig = models.BooleanField(default=False,help_text='Geben Sie an ob Antwort2 richtig ist',verbose_name="Antwort2 richtig?")
    antwort3 = models.CharField(max_length=255,blank=True,null=True,help_text='Geben Sie die Antwort3 der Frage ein (optional)')
    antwort3richtig = models.BooleanField(default=False,help_text='Geben Sie an ob Antwort3 richtig ist',verbose_name="Antwort3 richtig?")
    antwort4 = models.CharField(max_length=255,blank=True,null=True,help_text='Geben Sie die Antwort4 der Frage ein (optional)')
    antwort4richtig = models.BooleanField(default=False,help_text='Geben Sie an ob Antwort4 richtig ist',verbose_name="Antwort4 richtig?")
    freigegeben=models.BooleanField(default=False,help_text='Frage freigeben?',verbose_name="Frage freigeben")
	
    def __str__(self):
        return self.name
		
    def get_absolute_url(self):
        return reverse('frage_detail', args=[str(self.id)])

class RichtigOderFalsch(models.Model):
    name = models.CharField(max_length=255,blank=False,help_text='Geben Sie hier die Frage ein')
    kurs = models.ForeignKey(Kurs,null=True,blank=False,on_delete=models.CASCADE,help_text='Wählen Sie den Kurs, welchem die Frage zugewiesen wird')
    behauptungrichtig = models.BooleanField(default=False,verbose_name="Behauptung wahr?")
    freigegeben=models.BooleanField(default=False,help_text='Frage freigeben?',verbose_name="Frage freigeben")
	
    def __str__(self):
        return self.name
		
    def get_absolute_url(self):
        return reverse('richtigoderfalsch_detail', args=[str(self.id)])

class Ergebnis(models.Model):
    testmodus = models.CharField(max_length=20,blank=False)
    benutzername = models.CharField(max_length=50,blank=False)
    kursid = models.CharField(max_length=5,blank=False)
    kursname = models.CharField(max_length=50,blank=False)
    zeitsekunden = models.IntegerField(blank=False)
    datum = models.DateField(auto_now_add=True)
    punkte = models.IntegerField(blank=False)
    fragentotal = models.IntegerField(blank=False)
    fragenkorrekt = models.IntegerField(blank=False)
    fragenfalsch = models.IntegerField(blank=False)
	
    def __str__(self):
        return self.benutzername
		
    def get_absolute_url(self):
        return reverse('ergebnis_detail', args=[str(self.id)])
		
class MeldungMCFragen(models.Model):

    kursname = models.CharField(max_length=50,blank=False)
    kursid = models.ForeignKey(Kurs,null=True,blank=False,on_delete=models.CASCADE)
    frageid = models.ForeignKey(Frage,null=True,blank=False,on_delete=models.CASCADE)
    frage = models.CharField(max_length=255,blank=False)
    nachricht = models.CharField(max_length=500,blank=False)
    benutzername = models.CharField(max_length=50,blank=False)
    gelesen=models.BooleanField(default=False)
	
    def __str__(self):
        return self.frage
		
    def get_absolute_url(self):
        return reverse('meldungmcfragen_detail', args=[str(self.id)])

	
class MeldungRFFragen(models.Model):

    kursname = models.CharField(max_length=50,blank=False)
    kursid = models.ForeignKey(Kurs,null=True,blank=False,on_delete=models.CASCADE)
    frageid = models.ForeignKey(RichtigOderFalsch,null=True,blank=False,on_delete=models.CASCADE)
    frage = models.CharField(max_length=255,blank=False)
    nachricht = models.CharField(max_length=500,blank=False)
    benutzername = models.CharField(max_length=50,blank=False)
    gelesen=models.BooleanField(default=False)
	
    def __str__(self):
        return self.frage
		
    def get_absolute_url(self):
        return reverse('meldungrffragen_detail', args=[str(self.id)])