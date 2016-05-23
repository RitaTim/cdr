from __future__ import unicode_literals
from django.core.mail import mail_admins, send_mail
from django.conf import settings

def multiple_inform(emails=[], url_site=None, ref_unsubscribe=None, html_message=None):
	subject = "Сообщение с сайта " + domain_site
	message = ""
	html_message = + "<p>Если вы хотите отписаться от получения новостей, пройдите по ссылке " + ref_unsubscribe + "</p>"
	send_mail(subject, message, settings.EMAIL_HOST_USER, emails, html_message=html_message)
	return

def notify_user(email=None, domain_site=None, ref_unsubscribe=None):
	subject = "Сообщение с сайта " + domain_site
	message = ""
	html_message = "<h3>Вас приветсвует школа капоэйры Capoeira de Rua</h3>"
	html_message += "<h4>Спасибо, что остаетесь с нами на связи. Мы будем оповещать Вас о всех мероприятиях и акциях школы</h4>"
	html_message +=	"<p>Если вы хотите отписаться от получения новостей, пройдите по ссылке " + ref_unsubscribe + "</p>"

	send_mail(subject, message, domain_site, [email,], html_message=html_message)
	return

def added_new_student(name=None, phone=None, filial=None, domain_site=None):
	subject = "Сообщение с сайта " + domain_site
	message = ""
	html_message = "<h4>На класс по капоэйре записался новый ученик:</h4>"
	html_message += "<p>Имя: " + name + "</p><p>Номер телефона: " + phone + "</p><p>Филиал: " + filial + "</p>"
	mail_admins(subject, message, fail_silently=False, connection=None, html_message=html_message)
	return