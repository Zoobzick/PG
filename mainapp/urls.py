from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(),
         name="mainapp_view"),
    path("contacts/", views.ContactsPageView.as_view(),
         name="mainapp_contacts")
]