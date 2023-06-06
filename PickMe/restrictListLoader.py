import requests
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE','PickMe.settings')
import django
django.setup()
from restrictIng.models import restrictList

def loadjson(url):
    response=requests.get(url)
    contents=response.text

    json_ob = json.loads(contents)

    body = json_ob['body']['items']

    result=[]
    for dic in body:
        if(dic['COUNTRY_NAME']=='한국'):
            # print(dic['COUNTRY_NAME'])
            restrictlist_country=dic['COUNTRY_NAME']
            # print(restrictlist_country)  
        else:
            continue
        # restrictlist_id=dic['CAS_NO']
        regulate_type=dic['REGULATE_TYPE']
        restrictlist_ko_name=dic['INGR_STD_NAME']
        restrictlist_en_name=dic['INGR_ENG_NAME']   
        restrictlist_limit=dic['LIMIT_COND']
        restrictlist_obj={
                # 'restrict_id':restrictlist_id,
                'restrict_regulate_type':regulate_type,
                'restrict_name_ko':restrictlist_ko_name,
                'restrict_name_en':restrictlist_en_name,
                'restrict_country':restrictlist_country,
                'restrict_limit':restrictlist_limit,
        }    
        result.append(restrictlist_obj)


    #print(result)
    return result

def insertDB(json_result):
    for ingredient in json_result:
        print("add: "+ingredient['restrict_name_ko'])
        restrictList(
            # restrict_id=ingredient['restrict_id'],
                     restrict_regulate_type=ingredient['restrict_regulate_type'],
                     restrict_name_ko=ingredient['restrict_name_ko'],
                     restrict_name_en=ingredient['restrict_name_en'],
                     restrict_country=ingredient['restrict_country'],
                     restrict_limit=ingredient['restrict_limit']).save()

for i in range(1,118):
    url='https://apis.data.go.kr/1471000/CsmtcsUseRstrcInfoService/getCsmtcsUseRstrcInfoService?serviceKey=da6yY52o3ERSZU9AJC9FjiIpdnDsq3CAOfrFx3BPAt5IQbdxNd%2Boi5c6nmfvivvtiLpDZQpoc93KX4%2FOkeef7A%3D%3D&pageNo='+str(i)+'&numOfRows=100&type=json'
    restrict_json_result=loadjson(url)
    insertDB(restrict_json_result)

# print(body)

#print(json_ob)
# print(type(json_ob))

# from urllib.parse import urlencode,unquote
# import requests
# import json
# import pprint

# url="https://apis.data.go.kr/1471000/CsmtcsUseRstrcInfoService/getCsmtcsUseRstrcInfoService?"
# queryString="?"+urlencode({
#     "serviceKey":unquote("da6yY52o3ERSZU9AJC9FjiIpdnDsq3CAOfrFx3BPAt5IQbdxNd+oi5c6nmfvivvtiLpDZQpoc93KX4/Okeef7A=="),
#     "pageNo":1,
#     "numOfRows":"100",
#     "resultType":"json",
# })
# queryURL=url+queryString

# response=requests.get(queryURL)
# contents=response.text

# pp=pprint.PrettyPrinter(indent=4)
# print(pp.pprint(contents))


