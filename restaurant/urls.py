<<<<<<< HEAD
from django.urls import path
from . import views

=======
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 66cdd400b0dbe343d4af6af94b7b9901f792f672

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
<<<<<<< HEAD
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    path('menu/', views.Menu, name="menu"),
=======
    path('book/', views.book, name="book"), 
    path('menu/', views.menu, name="menu"),
>>>>>>> 66cdd400b0dbe343d4af6af94b7b9901f792f672
    path('menu_item/<int:pk>/', views.display_menu_items, name="menu_item"),
]