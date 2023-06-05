from django.urls import path
# from restrictIng.views import restrictViewSet
from restrictIng.views import imageAPI

urlpatterns=[
    path('imgPost/',imageAPI.as_view())
]