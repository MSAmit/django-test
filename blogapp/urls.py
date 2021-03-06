from django.conf.urls import url
from django.views.generic import ListView
from blogapp.models import Post

urlpatterns = [
	url(r'^', ListView.as_view(queryset = Post.objects.all().order_by("-created")[:2], 
								template_name = "blog.html")),
]
