from django.urls import path
from todoList.views import *

app_name = 'todoList'
urlpatterns = [
    path('',homePage,name="homePage"),
    path('noteAdd',noteAdd,name="noteAdd"),
    path('noteUpdate',noteUpdate,name="noteUpdate"),
    path('noteDelete',noteDelete,name="noteDelete"),
    path('markStar',markStar,name="markStar"),
    path('removeStar',removeStar,name="removeStar")
]