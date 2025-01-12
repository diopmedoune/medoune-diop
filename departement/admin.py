from django.contrib import admin
from .models import DepartementModel, ProfesseurModel

@admin.register(DepartementModel)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ("nom_departement", "mail_departement")


admin.site.register(ProfesseurModel)