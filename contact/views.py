from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from contact.models import Receipient

# Create your views here.
@api_view(['POST'])
def sendMail(request):
   if request.method == 'POST':
      data = request.data
      message = f"Name: {data.get('name')}\nEmail: {data.get('email')}\nPhone: {data.get('phone')}\nMessage: {data.get('message')}"

      try:
         send_mail(
            subject='Email from contact form on amartislab.com',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[receipient.email for receipient in Receipient.objects.all()]
         )
         print("\n"+message)

         # return Response('success')
         return Response({"code": "success", "message": "We will get back to you in a moment"})

      except Exception as e:
         print(f'Exception: {e}')
         return Response('{"code": "failure", "message": "Sorry lets find out the issue"}')


class ContactView(TemplateView):
    template_name = "contact/contact.html"

