
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from restrictIng.models import ingredeintList
from restrictIng.seriallizers import totalSelializer

class imageAPI(APIView):    
    def post(self, req):
        if req.FILES:
            req_img=req.FILES['image']      
            byte_str=req_img.read()

            req_json={'image':byte_str}
            MODEL_SERVER='http://133.186.213.221:5000/imgTest' 
            res=requests.post(MODEL_SERVER,files=req_json)

            if res:                
                re=res.json()
                result=db_to_search(re) 
                #print("result: ",result)                                 
                return Response(result,status=status.HTTP_200_OK)
            else:
                result={'all_ingredient':'Model response is not enough'}
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        else:
            result={'all_ingredient':'sorry, req is not image'}
            return Response(status=status.HTTP_400_BAD_REQUEST)     

def db_to_search(res):
    restrict_list=[]
    all_list=[]
    for i in res['all_ingredient_name']:
        querySet=ingredeintList.objects.filter(ingredient_ko_name=i).values()
        all_list.append(querySet[0])
        if querySet[0]['restrict_type']==True:
            restrict_list.append(querySet[0])
    data={
        'all_ingredient':all_list,
        'restrict_ingredient':restrict_list
    }
    serializer=totalSelializer(instance=data)
    return serializer.data        


