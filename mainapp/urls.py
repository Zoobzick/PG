from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

# app_name = MainappConfig.name

from mainapp.views import ProjectDetailView

app_name = 'mainapp'

urlpatterns = [
    path("", views.MainPageView.as_view(),
         name="mainapp_view"),
    path("contacts/", views.ContactsPageView.as_view(),
         name="mainapp_contacts"),
    path("projects/", views.ProjectPageView.as_view(),
         name="mainapp_projects"),
    path("project/<int:pk>", ProjectDetailView.as_view(),
         name="mainapp_project-detail")
]