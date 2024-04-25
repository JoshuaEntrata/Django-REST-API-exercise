from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogPostList.as_view(), name="posts-view"),
    path('blog/create', views.BlogPostCreate.as_view(), name="posts-create"),
    path("blog/update/<int:pk>/", views.BlogPostUpdate.as_view(), name="post-edit"),
    path("blog/delete/<int:pk>/", views.BlogPostDelete.as_view(), name="post-delete"),
    path("blog/filter/<str:title>", views.BlogPostFilteredList.as_view(), name="posts-filtered"),
]