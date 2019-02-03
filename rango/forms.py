from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=Category._meta.get_field("name").max_length,help_text="Please enter the category name:")
	views = forms.IntegerField(widget=forms.HiddenInput(),initial=0,required=False)
	likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0,required=False)
	slug = forms.CharField(widget=forms.HiddenInput(),required=False)

	class Meta:
		model = Category
		fields = ("name",)

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=Page._meta.get_field('title').max_length,help_text="Please enter the title of the page.")
	url = forms.URLField(max_length=200,help_text="Please enter the url of the page.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)

	class Meta:
		model = Page
		exclude = ("category",)

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')
