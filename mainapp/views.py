from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная"
        print(context['title'])
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context
