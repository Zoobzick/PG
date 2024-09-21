from django.conf import settings
from django.conf.urls.static import static
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
         name="mainapp_project-detail"),
    path("about/", views.AboutView.as_view(),
         name="mainapp_about"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)