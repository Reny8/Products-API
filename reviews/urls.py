from django.urls import path
from . import views

urlpatterns = [
    path('add_review/',views.create_a_review),
]