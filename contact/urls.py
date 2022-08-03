from django.urls import path

from contact.views import ContactView, sendMail

app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name='contact-page'),
    path('sendMail/', sendMail, name='send-mail'),
]