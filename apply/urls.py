from django.urls import path     
from . import views
urlpatterns = [
    path('', views.apply),  #apply to join the team form
    path('/submitapply', views.submitapply),  #user applies to join the team
    path('/success', views.successapply),  #user has succesfully applied
]