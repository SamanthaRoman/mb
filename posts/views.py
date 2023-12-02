from django.views.generic import ListView, CreateView, DetailView     # list view represents a scan and returns multiple records from a database tabel
from .models import Post

# vanilla use of list view of all the records in a python list called (the name of your model plus _list)
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post                                 # need to import the model at the top as well. 
                                                    # our recordd will be called post_list

class PostCreateView(CreateView):               # createview is one of the janga views to generate forms.
    template_name = "posts/new.html"            # the object that will be recieved in the form of html form.
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDetailView(DetailView):               #detail view gives you a single record at a time so it needs a primary key.
    template_name = "posts/detail.html"
    model = Post
