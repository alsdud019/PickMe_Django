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

class ingNameTypeSelializer(serializers.ModelSerializer):
    class Meta:
        model=ingredeintList
        fields=('ingredient_ko_name','restrict_type')

class restrictNameLimitSelializer(serializers.ModelSerializer):
    class Meta:
        model=ingredeintList
        fields=('ingredient_ko_name','restrict_limit')

class totalSelializer(serializers.Serializer):
    all_ingredient=ingNameTypeSelializer(many=True)
    restrict_ingredient=restrictNameLimitSelializer(many=True)
