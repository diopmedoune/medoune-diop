from rest_framework import serializers
from  .models import DepartementModel, ProfesseurModel

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartementModel
        fields = '__all__'


class ProfesseurSerializer(serializers.ModelSerializer):
    chef_departement = serializers.SerializerMethodField()
    class Meta:
        model = ProfesseurModel
        fields = '__all__'

    def get_chef_departement(self, instance):
        queryset = instance.chef_departement
        serializer = DepartementSerializer(queryset , many=True)

        return serializer.data