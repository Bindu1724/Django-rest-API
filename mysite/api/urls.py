
from . import views
from django.urls import path, include

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDelete.as_view(), name="update"),
]
