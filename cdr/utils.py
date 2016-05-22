from django.core.mail import mail_admins, send_mail

def inform_all(emails=[], message=None):
	subject = "Новости с сайта capoeiraderua.ru"
	res = send_mail('Subject here', message, 'capoeiraderua@mail.ru', emails, fail_silently=False, html_message=True)
	return res

def added_new_student(name=None, phone=None):
	subject = "На занятие записался новый ученик"
	message = "<p>Данные пользователя:</p><p>" + name + "</p><p>" + phone + "</p>"
	res = mail_admins(subject, message, fail_silently=False, connection=None, html_message=True)
	return res