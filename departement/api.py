from .models import ProfesseurModel
from .serializers import  ProfesseurSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


class ProfesseurViewSet(ReadOnlyModelViewSet):
    serializer_class = ProfesseurSerializer
    
    def get_queryset(self):
        return ProfesseurModel.objects.all()
    
