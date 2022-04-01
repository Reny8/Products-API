from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews_list),
    path('reviews/<int:pk>/', views.review_detail)
]