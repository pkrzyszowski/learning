# import smtplib
#
# server = smtplib.SMTP('mail.spero.click', 587)
# server.starttls()
# server.login('piotr.krzyszowski@spero.click', 'Krzyszowski2017')
#
# msg = "YOUR MESSAGE!"
# server.sendmail("piotr.krzyszowski@spero.click", "guardian@spero.click", msg)
# server.quit()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "robs@spero.click"
toaddr = ""

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "[ROBS]Protokół Zwrotu Pojazdu WF0195J"

body = "Utworzono protokół zwrotu pojazdu \n" \
       " firma: Lindt & Sprüngli (Poland) Sp. z o.o.(szkoda) \n" \
       "pojazd: WF0195J (SKODA FABIA) \n" \
       "Autologistic \n" \
       "ta wiadomość została wysłana automatycznie, prosimy na nią nie odpowiadać"

msg.attach(MIMEText(body, 'plain'))


filename = "WF0195J.pdf"
attachment = open('/home/vagrant/programming/WF0195J.pdf', "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('mail.spero.click', 587)
server.starttls()
server.login('robs@spero.click', 'w+HO.0$JM&$e')
text = msg.as_string()
server.sendmail("robs@spero.click", [] + ['piotr.krzyszowski@spero.click', 'guardian@spero.click', 'szisz90@gmail.com'], text)
server.quit()