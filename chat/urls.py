from django.urls import path
from chat import views
app_name = 'chat'
urlpatterns = [
    # path('chat/',index,name='chat')
    path('',views.index,name='chat'),
    path('<str:room_name>/', views.room, name='room'),
]