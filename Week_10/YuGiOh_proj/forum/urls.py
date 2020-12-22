from django.urls import path
from . import views


urlpatterns = [
    path('', views.CommentListView.as_view(), name='comment_list'),
    path('comment/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>', views.CommentDetailView.as_view(), name='comment_detail'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/reply/', views.ReplyCreateView.as_view(), name='reply_create'),
    ]