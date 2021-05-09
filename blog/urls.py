from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogs/new', views.NewBlog.as_view(), name='new_blogs'),
    path('blogger/<int:pk>', views.BlogListByAuthor.as_view(), name='blogs-by-author'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blog/<int:pk>/comment', views.BlogCommentCreate.as_view(), name='blog_comment'),
]

# urlpatterns = [
#     path('', views.index,),
#     path('blogs/', views.get_blogs,),
# ]