from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.login, name="Students-login"),
    path('home/', views.home, name="Students-home"),
    path('', views.home, name="Students-home"),
    path('about/', views.about, name="Students-about"),
    path('viewjournals/', views.viewjournals, name="Students-viewjournals"),
    path('addjournal/', views.addjournal, name="Students-addjournal"),
    path('deletejournal/<int:jid>', views.deletejournal,name="Students-deletejournal"),
]