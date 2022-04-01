from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews_list),
    path('<int:fk>/reviews/', views.review_detail)
]