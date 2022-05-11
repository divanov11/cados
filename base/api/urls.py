from .import views 
from django.urls import path

urlpatterns = [
    path('', views.getRoutes),
    path('api/posts/', views.getPosts),

    path('api/posts/add/', views.addPost),
    path('api/posts/edit/<str:pk>/', views.editPost),
    path('api/posts/delete/<str:pk>/', views.deletePost),
    path('api/posts/<str:pk>/', views.getPost),

    path('api/users/', views.getUsers),
    path('api/users/recommended', views.getRecommendedUsers),
    path('api/users/<str:username>/', views.getUser),

    path('api/companies/', views.getCompanies),
    path('api/companies/<str:pk>/', views.getCompany),

    path('api/openings/', views.getLatestJobs),
]