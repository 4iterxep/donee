from django.urls import path, include
from . import views
from .views import SearchResultsView
from users.views import MyLoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('kupons/', views.kupons, name='kupons'),
    path('profile/', views.profile, name='profile'),
    path('users/', include('users.urls')),
    path('<int:pk>', views.KuponDetailView.as_view(), name='kupon_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('basket-add/<int:kupon_id>/', views.basket_add, name='basket_add'),
    path('accounts/login/', MyLoginView.as_view(), name='login'),
]
