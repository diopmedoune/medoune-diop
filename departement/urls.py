from django.urls import path, include
from  rest_framework import routers

from departement import views
from .api import ProfesseurViewSet


router = routers.SimpleRouter()
router.register('professeurs', ProfesseurViewSet, basename='profs')

urlpatterns = [
    path('form1/', views.create_departement, name='html_form'),
    path('form2/', views.add_departement, name='django_html_form'),
    path('add-prof/', views.add_professor, name='add_prof'),
    path('profs/', views.show_all_prof, name='show_all_profs'),
    path('depts/', views.show_all_depts, name='show_all_depts'),
    path('', views.home, name='home'),

    # API
    path('api/', include(router.urls)),
]


