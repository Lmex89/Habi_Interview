from django.urls import path
from Furniture import views


urlpatterns = [
    # GET List all furnitures as a List GET Method
    path('furniture/', views.FurnitureList.as_view()), 
     
]