from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class FormPageView(TemplateView):
    template_name = "form.html"

class FinishPageView(TemplateView):
    template_name = "finish.html"

class FinishRealPageView(TemplateView):
    template_name = "finishreal.html"

class IndexCopyPageView(TemplateView):
    template_name = "index_copy.html"