from django.views.generic import (TemplateView, ListView, 
        DeleteView, DetailView, View, FormView)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy

from forum_django.forms import (LoginForm, ProfilForm, 
        QuestionForm, SearchQuestionForm, UserForm)
from forum_django.models import ProfilModel, QuestionModel

# sing in form validation
class SinginView(View):
    model = User
    form_class = UserForm
    template_name = 'forum_django/singin.html'
    success_url = reverse_lazy('profil_maker')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form':form})

# login form validation
class LoginView(View):
    form_class = LoginForm
    template_name = 'forum_django/login.html'
    success_url = reverse_lazy('home')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect(self.success_url)
            else:
                messages.error(request, "Identifiants incorrects!")
        return render(request, self.template_name, {'form':form})

class ImageProfilMakerView(LoginRequiredMixin, FormView):
    model = ProfilModel
    form_class = ProfilForm
    template_name = 'forum_django/image_profil_maker.html'
    success_url = reverse_lazy('home')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            profil = form.save(commit = False)
            profil.profil_id = request.user
            profil.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form':form})

# home view
class HomeView(LoginRequiredMixin, ListView):
    model = QuestionModel
    template_name = 'forum_django/home.html'
    context_object_name = 'user_questions'
    
    def get_queryset(self):
        return QuestionModel.objects.filter()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = self.request.user
    #     context['user_profil'] = user.profilmodel
    #     return context

class ProfilView(DetailView):
    model = ProfilModel
    template_name = 'forum_django/profil.html'
    context_object_name = 'profil'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.profil_id
        context['user_questions'] = QuestionModel.objects.filter(user_id = user)
        
        return context

class PublishQuestionView(View):
    model = QuestionModel
    form_class = QuestionForm
    template_name = 'forum_django/publish_question.html'
    success_url = reverse_lazy('home')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,{'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_post = form.save(commit=False)
            user_post.user_id = request.user
            user_post.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form':form})

# View to find questions

class SearchView(View):
    form_class = SearchQuestionForm
    template_name = 'forum_django/search.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            search_questions = QuestionModel.objects.filter(title__contains = "connexion")
            
            return render(request, self.template_name, {
                'search_questions':search_questions,
                'form':form,
                })
        return render(request, self.template_name, {'form':form})

class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))