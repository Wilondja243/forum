
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

from forum_django.models import ResponseModel, LikeModel, ProfilModel, QuestionModel


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, 
        widget = forms.TextInput(attrs={
            'placeholder':'Entrer votre nom'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'luckson@gmail.com'
    }))
    password = forms.CharField(max_length=50, 
        widget=forms.PasswordInput(attrs={
            'placeholder':'*********'
    }))
    password2 = forms.CharField(max_length=50, 
        widget=forms.PasswordInput(attrs={
            'placeholder':'*********'
    }))

    class Meta:
        model = User
        fields = ['username','email','password','password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username = username).exists():
            raise ValidationError(""" Le nom d' utilisateur que
                            vous avez entrer existe deja! """)
        if len(username) < 8:
            raise ValidationError(" votre nom est trop petit!")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise ValidationError("L'email existe deja!")
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) <= 7:
            raise ValidationError(""" Le mot de passe doit 
                        contenir au moin 8 caracteres! """)
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError("Le mot de passe ne correspond pas!")
        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, 
        widget=forms.TextInput(attrs={
        'placeholder':'Votre nom'
    }))
    password = forms.CharField(max_length=50, 
        widget=forms.PasswordInput(attrs={
            'placeholder':'********'
    }))
    
class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder':'titre'
    }))
    content = forms.CharField(max_length=200, 
        widget=forms.TextInput(attrs={
            'placeholder':'votre contenu'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'votre description'
    }))

    class Meta:
        model = QuestionModel
        fields = ['title','content','description']

        def clean_title(self):
            title = self.cleaned_data.get('title')
            if len(title) > 100:
                raise ValidationError(""" Le titre ne doit 
                            pas depasser 100 caracteres! """)
            return title
        
        def clean_content(self):
            content = self.cleaned_data('content')
            if len(content) > 200:
                raise ValidationError(""" Le contenu doit 
                        avoir minimum 200 caracteres! """)
            return content

class ProfilForm(forms.ModelForm):
    class Meta:
        model = ProfilModel
        fields = ['profil_image',]

class ResponseForm(forms.ModelForm):
    response = forms.CharField(max_length=800, 
        widget=forms.TextInput(attrs={
            'placeholder':'Repondre a la question'
    }))
    class Meta:
        model = ResponseModel
        fields = ['response',]

    def clean_response(self):
        response = self.cleaned_data.get('response')
        if len(response) > 500:
            raise ValidationError(""" La reponse ne doit
                         pas depasser 800 caracteres """)
        return response
    
class LikeForm(forms.ModelForm):
    class Meta:
        model = LikeModel
        fields = ['like',]


class StudentForm(forms.Form):
    student = forms.CharField(max_length=200)

class SearchQuestionForm(forms.Form):
    search = forms.CharField(label='recherche de questions', 
                max_length=200,
                widget=forms.TextInput(attrs={
                    'placeholder':'rechercher une questions'
                })
            )
