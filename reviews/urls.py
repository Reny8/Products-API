from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews_list),
    path('reviews/<int:fk>/', views.review_detail)
]