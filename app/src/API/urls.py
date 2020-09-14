from django.urls import path
from API.views import CoffeMachineListView,CoffePodListView, CoffeMachineCreateView,CoffePodCreateView

urlpatterns = [
    path('create-machine/',      CoffeMachineCreateView.as_view()),
    path('create-pod/', CoffePodCreateView.as_view()),
    path('get-machine/', CoffeMachineListView.as_view()),
    path('get-pod/', CoffePodListView.as_view()),

]
