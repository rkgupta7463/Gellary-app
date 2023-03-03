from django.urls import path
from .views import home,recent,previous,delImg

urlpatterns = [
    path('',home,name="home"),
    path('image/recent',recent,name="recent"),
    path('image/previous',previous,name="previous"),
    path('image/<int:pk>/delete',delImg,name="delimg"),
]
