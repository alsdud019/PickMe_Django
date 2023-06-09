from rest_framework import serializers
from restrictIng.models import restrictList,ingredeintList
from restrictIng.models import imgpost

class restrticListSerializer(serializers.ModelSerializer):
    class Meta:
        model=restrictList
        fields=('restrict_name_ko','restrict_name_en','restrict_country','restrict_regulate_type','restrict_limit')

class PostSerializer(serializers.ModelSerializer):
    #image=serializers.ImageField(use_url=True)
    class Meta:
        model=imgpost
        fields='__all__'

class ingKoNameTypeSelializer(serializers.ModelSerializer):
    ingredient_name=serializers.CharField(source="ingredient_ko_name")
    class Meta:
        model=ingredeintList
        fields=('ingredient_name','restrict_type')

class restrictKoNameLimitSelializer(serializers.ModelSerializer):
    ingredient_name=serializers.CharField(source="ingredient_ko_name")
    class Meta:
        model=ingredeintList
        fields=('ingredient_name','restrict_limit')

class totalKoSelializer(serializers.Serializer):
    all_ingredient=ingKoNameTypeSelializer(many=True)
    restrict_ingredient=restrictKoNameLimitSelializer(many=True)

class ingEnNameTypeSelializer(serializers.ModelSerializer):
    ingredient_name=serializers.CharField(source="ingredient_en_name")
    class Meta:
        model=ingredeintList
        fields=('ingredient_name','restrict_type')

class restrictEnNameLimitSelializer(serializers.ModelSerializer):
    ingredient_name=serializers.CharField(source="ingredient_en_name")
    class Meta:
        model=ingredeintList
        fields=('ingredient_name','restrict_limit')    

class totalEnSelializer(serializers.Serializer):
    all_ingredient=ingEnNameTypeSelializer(many=True)
    restrict_ingredient=restrictEnNameLimitSelializer(many=True)
