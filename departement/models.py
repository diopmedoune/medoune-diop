from django.db import models

class DepartementModel(models.Model):
    nom_departement = models.CharField(max_length=50)
    mail_departement = models.EmailField(max_length=254)
    numero_departement = models.CharField(max_length=50)
    description_departement = models.TextField()
    
    def __str__(self):
        return f"{self.nom_departement}"

    class Meta:
        db_table = "departement"
        verbose_name_plural = "Departements"

class ProfesseurModel(models.Model):
    nom_prof = models.CharField(max_length=50, verbose_name='Nom complet du professeur')
    contact_prof = models.CharField(max_length=50, verbose_name='Contact professeur')
    date_d_adhesion = models.DateField(verbose_name="Date d'adhésion")

    chef_departement = models.ManyToManyField(DepartementModel, blank=True)

    def __str__(self):
        return f"{self.nom_prof}"
    
    class Meta:
        db_table = "professeur"
        verbose_name_plural = 'Professeurs'

