# -*- coding: utf-8 -*-

from django.core.mail import mail_admins, send_mail
from django.conf import settings

def multiple_inform(emails=[], url_site=None, ref_unsubscribe=None,
                    html_message=None):
	subject = u"Сообщение с сайта " + settings.SITE_NAME
	message = ""
	html_message = u"{} <p>Если вы хотите отписаться от получения новостей, " \
	               u"пройдите по ссылке {} </p>"\
				   .format(html_message, ref_unsubscribe)
	send_mail(subject, message, settings.EMAIL_HOST_USER, emails,
	          html_message=html_message)
	return

def notify_user(email=None, domain_site=None, ref_unsubscribe=None):
	subject = u"Сообщение с сайта {}".format(domain_site)
	message = ""
	html_message = u"<h3>Вас приветсвует школа капоэйры Capoeira de Rua</h3>" \
	               u"<h4>Спасибо, что остаетесь с нами на связи. Мы будем " \
	               u"оповещать Вас о всех мероприятиях и акциях школы</h4>" \
	               u"<p>Если вы хотите отписаться от получения новостей," \
	               u" пройдите по ссылке {} </p>".format(ref_unsubscribe)
	send_mail(subject, message, domain_site, [email,],
	          html_message=html_message)
	return

def added_new_student(name=None, phone=None, filial=None, domain_site=None):
	subject = u"Сообщение с сайта " + domain_site
	message = ""
	html_message = u"<h4>На класс по капоэйре записался новый ученик:</h4>" \
	               u"<p>Имя: {}</p><p>Номер телефона: {}</p><p>Филиал: {}</p>"\
				   .format(name, phone, filial)
	mail_admins(subject, message, fail_silently=False, connection=None,
	            html_message=html_message)
	return

