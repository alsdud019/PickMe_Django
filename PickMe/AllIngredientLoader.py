import requests
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE','PickMe.settings')
import django
django.setup()
from restrictIng.models import allIngredientList

for i in range(1,207):
    url='https://apis.data.go.kr/1471000/CsmtcsIngdCpntInfoService/getCsmtcsIngdCpntInfoService?serviceKey=da6yY52o3ERSZU9AJC9FjiIpdnDsq3CAOfrFx3BPAt5IQbdxNd%2Boi5c6nmfvivvtiLpDZQpoc93KX4%2FOkeef7A%3D%3D&pageNo='+str(i)+'&numOfRows=100&type=json'

    response=requests.get(url)
    contents=response.text

    json_ob=json.loads(contents)
    body=json_ob['body']['items']

    result=[]
    for dic in body:   
        Ingredient_obj={
            'Ingr_ko_name':dic['INGR_KOR_NAME'],
            'Ingr_en_name':dic['INGR_ENG_NAME'],
        }
        result.append(Ingredient_obj)

    for ingredient in result:
        print("add: "+ingredient['Ingr_ko_name'])
        allIngredientList(
            ingredient_ko_name=ingredient['Ingr_ko_name'],
            ingredient_en_name=ingredient['Ingr_en_name']).save()
