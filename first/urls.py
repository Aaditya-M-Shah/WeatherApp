# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 10:24:07 2022

@author: Dr Mitesh shah
"""

from django.urls import path
from .views import *

urlpatterns = [
        path('',weather,name="Weather"),
        path("remove/<int:pk>",removecity,name="remove")
    ]