from django.views.generic import TemplateView


class TestPage(TemplateView):
    """
    For checking login or not.
    """
    template_name = 'test.html'


class ThanksPage(TemplateView):
    """
    For checking logout or not.
    """
    template_name = 'thanks.html'


class HomePage(TemplateView):
    """
    Create a HomePage class for Home Page of website and it's inherit from 'TemplateView'.
    """
    template_name = 'index.html'