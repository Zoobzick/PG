import logging

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import ContactForm



class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная"
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        context["form"] = ContactForm()
        print(reverse('mainapp:mainapp_view'))
        return context

    def post(self, request, *args, **kwargs):

        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            full_message = f'Сообщение от {name} <{email}\n\n{message}>'

            send_mail(
                subject,
                full_message,
                'murdoc-94@yandex.ru',
                [email],
                fail_silently=False
            )
            messages.success(request, 'Ваше сообщение отправлено')

            return redirect(reverse('mainapp:mainapp_contacts'))

        return redirect(reverse('mainapp:mainapp_contacts'))
