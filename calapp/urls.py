from django.contrib import admin
from django.urls import path
from .views import add_view, template_view

urlpatterns = [
    path('',template_view.as_view(),name='home'),
    path('add',add_view.as_view(),name='add'),
    path('ho',template_view.as_view(),name='home'),
    path('ho/<str:date>',template_view.as_view(),name='ho')
]
