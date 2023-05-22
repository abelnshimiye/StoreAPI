from django.core.mail import send_mail, mail_admins, EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        # send_mail('subject', 'message', 'info@abel.com', ['bob@abel.com'])
        # mail_admins('subject', 'message', html_message='message')
        # message = EmailMessage('subject', 'message', 'from@abel.com', ['bob@abel.com'])
        # message.attach_file('playground/static/images/kitenge.jpg')
        # message.send()
        message = BaseEmailMessage(
            template_name='email/hello.html',
            context={'name':'Abel'}
        )
        message.send(['bob@abel.com']) # we add tyo a list of receipent 

    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Abel'})
