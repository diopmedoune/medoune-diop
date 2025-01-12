from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

admin.site.site_header = 'EPT'
admin.site.site_title = 'EPT Admin Panel'
admin.site.index_title = 'EPT DEPARTMENTS GESTION'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("departement.urls")),
    re_path('.*', TemplateView.as_view(template_name="404.html")), # [a-zA-Z] // ligne tjrs à la fin
]
