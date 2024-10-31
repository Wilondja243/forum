from django.urls import path

from .views import (HomeView, ImageProfilMakerView, 
        LoginView, ProfilView, PublishQuestionView, 
        SearchView, SinginView)

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('singin/', SinginView.as_view(), name='singin'),
    path('accounts/login/', LoginView.as_view(), 
            name='login'),
    path('profil_maker/', ImageProfilMakerView.as_view(), 
            name='profil_maker'),
    path('home/<uuid:pk>/user_profil/', ProfilView.as_view(), 
            name='profil'),
    path('home/published', PublishQuestionView.as_view(), 
            name='publish_question'),
    path('home/search_questions', SearchView.as_view(), 
            name='search'),
    path('logout/', LoginView.as_view(), name='logout'),
]