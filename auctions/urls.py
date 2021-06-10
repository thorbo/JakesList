from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("watch/<int:listing_id>", views.watch, name="watch"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("cat/<str:cat_id>", views.cat, name="cat"),
    path("close/<int:listing_id>", views.close, name="close")
]
