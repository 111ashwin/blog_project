from django import forms

from .models import Blog, BlogComment

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = [
			'name',
			'description',
			'author',
			'blog_cover_image',
		]

class BlogCommentForm(forms.ModelForm):
	class Meta:
		model = BlogComment
		fields = ['description']