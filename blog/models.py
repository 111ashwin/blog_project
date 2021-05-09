from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class BlogAuthor(models.Model):

	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
	bio = models.TextField(max_length=50, help_text="Enter your Bio details here.")

	class Meta:
		ordering = ["user", "bio"]

	def __str__(self):
		return self.user.username

class Blog(models.Model):

	name = models.CharField(max_length=30, blank=True)
	description = models.TextField(max_length=500 ,blank=True)
	author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
	post_date = models.DateTimeField(auto_now_add=True)
	blog_cover_image = models.ImageField(upload_to="images/", blank=True)

	def __str__(self):
		return self.author.user.username+ ' -> ' +self.name

	def get_absolute_url(self):
		return reverse("blog-detail", args=[str(self.id)])

	@property
	def image_url(self):
		if self.blog_cover_image and hasattr(self.blog_cover_image, 'url'):
			return self.blog_cover_image.url

class BlogComment(models.Model):

	description = models.TextField(max_length=500 ,blank=True)
	author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	post_date = models.DateTimeField(auto_now_add=True)	

	def get_absolute_url(self):
		return reverse("blog-detail", kwargs={'pk':self.blog.id})
