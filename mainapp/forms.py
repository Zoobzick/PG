from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Ваше Имя")
    email = forms.EmailField(required=True, label="Ваша почта")
    subject = forms.CharField(max_length=100, required=True, label="Тема")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Сообщение")