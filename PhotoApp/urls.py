from django.urls import path
from . import views

urlpatterns =[
    path('',views.GalleryFunction,name="Gallery"),
    path('upload',views.UploadFunction,name="Upload"),
    path('photo/<str:pk>/',views.PhotoFunction,name="Photo")
]