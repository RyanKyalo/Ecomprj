from django.urls import path
from core import views
from core.views import index

app_name = "core"

urlpatterns = [
    
    path("", index, name= "index" )
]
