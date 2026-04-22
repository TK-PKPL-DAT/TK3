from django import forms
import uuid

class CustomerRegisterForm(forms.Form):
    """Form register khusus Customer"""
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan username',
            'required': True
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan password',
            'required': True
        })
    )
    
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Konfirmasi password',
            'required': True
        })
    )
    
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan nama lengkap',
            'required': True
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan email',
            'required': True
        })
    )
    
    phone_number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nomor telepon (opsional)',
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        username = cleaned_data.get('username')
        
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("Password tidak cocok!")
        
        if username:
            from .models import UserAccount
            if UserAccount.objects.filter(username=username).exists():
                raise forms.ValidationError("Username sudah digunakan!")
        
        return cleaned_data


class OrganizerRegisterForm(forms.Form):
    """Form register khusus Organizer"""
    organizer_name = forms.CharField(
        max_length=100,
        label='Nama Lengkap',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan nama lengkap',
            'required': True
        })
    )
    
    contact_email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan email',
            'required': True
        })
    )
    
    phone_number = forms.CharField(
        max_length=20,
        required=False,
        label='Nomor Telepon',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nomor telepon (opsional)',
        })
    )
    
    username = forms.CharField(
        max_length=100,
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Pilih username',
            'required': True
        })
    )
    
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Minimal 6 karakter',
            'required': True
        })
    )
    
    password_confirm = forms.CharField(
        label='Konfirmasi Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Konfirmasi password',
            'required': True
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        username = cleaned_data.get('username')
        
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("Password tidak cocok!")
        
        if username:
            from .models import UserAccount
            if UserAccount.objects.filter(username=username).exists():
                raise forms.ValidationError("Username sudah digunakan!")
        
        return cleaned_data


class AdminRegisterForm(forms.Form):
    """Form register khusus Admin"""
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan username',
            'required': True
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan password',
            'required': True
        })
    )
    
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Konfirmasi password',
            'required': True
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email admin',
            'required': True
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        username = cleaned_data.get('username')
        
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("Password tidak cocok!")
        
        if username:
            from .models import UserAccount
            if UserAccount.objects.filter(username=username).exists():
                raise forms.ValidationError("Username sudah digunakan!")
        
        return cleaned_data


class LoginForm(forms.Form):
    """Form login"""
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan username',
            'required': True
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Masukkan password',
            'required': True
        })
    )
