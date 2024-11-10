from django.shortcuts import render
from .models import Post, Stock, Sports, Category
from django.views.generic import ListView, DetailView
def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    
    # Fetch the latest posts, sports, and stock data for this category
    latest_posts = Post.objects.filter(category=category).order_by('-created')[:5]
    stocks = Stock.objects.filter(category=category).order_by('-updated_at')[:5]
    sports = Sports.objects.filter(category=category).order_by('-event_date')[:5]

    context = {
        'category': category,
        'latest_posts': latest_posts,
        'stocks': stocks,
        'sports': sports,
    }
    return render(request, 'category.html', context)

class PostListView(ListView):
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        return Post.published.filter(categories=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
    
class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        categories = Category.objects.all()
        latest_posts = {}
        for category in categories:
            latest_post = Post.published.filter(categories=category).first()
            if latest_post:
                latest_posts[category] = latest_post
        return latest_posts
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        print("Current Post:", post)  # Debugging print
        category = post.categories.first()
        print("Post Category:", category)
        other_posts = Post.published.filter(categories=category).exclude(pk=post.pk)[:5]  # Exclude the current post itself
        print("Other Posts:", other_posts)
        context['other_posts'] = other_posts
        return context