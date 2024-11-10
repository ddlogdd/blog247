from django.urls import path
# from .views import NewsListView, ForexListView, StockListView, SportsListView, MovieListView
from .views import  PostListView, PostDetailView, HomeView
from django.conf import settings
from django.conf.urls.static import static
from . import views
# urlpatterns = [
#     path('news/', NewsListView.as_view(), name='news-list'),
#     path('forex/', ForexListView.as_view(), name='forex-list'),
#     path('stocks/', StockListView.as_view(), name='stock-list'),
#     path('sports/', SportsListView.as_view(), name='sports-list'),
#     path('movies/', MovieListView.as_view(), name='movie-list'),
# ]
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('search/', views.search, name='search'),
    # path('about', PostAboutView.as_view(), name='about'),
    # path('contact', PostContactView.as_view(), name='contact'),
    path('<slug:category>/', PostListView.as_view(), name='post_list'),
    path('<slug:category>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




