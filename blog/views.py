from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import BlogAuthor, Blog, BlogComment
from .forms import BlogForm, BlogCommentForm
from .blog_serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
def index(request):
	return render(request, 'index.html')



# @api_view(['GET', 'POST', 'DELETE'])
# def get_blogs(request):
# 	if request.method == 'GET':
# 		blogs = Blog.objects.all()
# 		blog_serializer = BlogSerializer(blogs, many=True)
# 		return Response(blog_serializer.data)
# 	if request.method == 'POST':
# 		serializer = BlogSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewBlog(generic.CreateView):
	form_class = BlogForm
	template_name = "blog/blog_create_form.html"

class BlogListView(generic.ListView):
	model = Blog
	panginate_by = 5

class BlogListByAuthor(generic.ListView):
	model = Blog
	panginate_by = 5
	template_name = "blog.blog_list_by_author.html"

	def get_queryset(self):

		id = self.kwargs['pk']
		target_author = get_object_or_404(BlogAuthor, pk = id)
		return Blog.objects.filter(author=target_author)

	def get_context_data(self, **	kwargs):

		context = super(BlogListByAuthor, self).get_context_data(**kwargs)
		context['blogger'] = get_object_or_404(BlogAuthor, pk = self.kwargs['pk'])
		return context

class BlogDetailView(generic.DetailView):
	"""
	Generic class-based detail view for a blog.
	"""
	model = Blog

	
class BloggerListView(generic.ListView):
	"""
	Generic class-based view for a list of bloggers.
	"""
	model = BlogAuthor
	paginate_by = 5

class BlogCommentCreate(generic.CreateView):
	form_class = BlogCommentForm
	field = ['description']
	template_name = "blog/blogcomment_form.html"

	def get_context_data(self, **kwargs):
		context = super(BlogCommentCreate, self).get_context_data(**kwargs)
		context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
		return context

	def form_valid(self, form):
		# import pdb;pdb.set_trace()
		form.instance.author = BlogAuthor.objects.get(user=self.request.user)
		form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
		return super(BlogCommentCreate, self).form_valid(form)

	def get_url_success():
		return reverse("blog-detail", kwargs={'pk':self.kwargs['pk']})
