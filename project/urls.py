from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from project import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^form/$', views.FormPageView.as_view()), # Add this /about/ route
    url(r'^finish/$', views.FinishPageView.as_view()), # Add this /about/ route
    url(r'^finishreal/$', views.FinishRealPageView.as_view()), # Add this /about/ route
    url(r'^index_copy/$', views.IndexCopyPageView.as_view()), # Add this /about/ route
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)