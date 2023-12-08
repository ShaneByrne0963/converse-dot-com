from . import views
from django.urls import path


urlpatterns = [
    path('', views.ListPosts.as_view(), name='home'),
    path('sort/<int:by_new><path:current_dir>',
         views.SortPosts.as_view(), name='sort_posts'),
    path('<slug:slug>/', views.ViewPost.as_view(), name='view_post'),
    path('results', views.SearchPost.as_view(), name='search_post'),
    path('tags/<str:tag_query>', views.SearchTag.as_view(),
         name='search_tag'),
    path('category/<slug:category_slug>', views.CategorisedPosts.as_view(),
         name='categories'),
    path('categories/browse', views.BrowseCategories.as_view(),
         name='browse_categories'),
    path('my-posts', views.MyPosts.as_view(), name='my_posts'),
    path('new-post', views.AddPost.as_view(), name='new_post'),
    path('edit/<int:id>', views.EditPost.as_view(), name='edit_post'),
    path('like/<slug:slug>', views.LikePost.as_view(), name='like_post'),
    path('delete/<slug:slug>', views.DeletePost.as_view(), name='delete_post'),
    path('comment/<slug:slug>', views.SendComment.as_view(),
         name='send_comment'),
    path('like-comment/<int:comment_id>', views.LikeComment.as_view(),
         name='like_comment'),
    path('edit-comment/<int:comment_id>', views.EditComment.as_view(),
         name='edit_comment'),
    path('delete-comment/<int:comment_id>', views.DeleteComment.as_view(),
         name='delete_comment'),
    path('new-poll', views.AddPoll.as_view(), name='new_poll')
]
