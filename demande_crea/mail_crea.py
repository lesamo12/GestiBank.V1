import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from sql.sql import connexion
from compte_user.user import User
from demande_crea.demande_crea_compte import DemandCreaCompte as Creation


class Mail_Crea(User):

    def __init__(self, id):
        super().__init__("CLIENT", id)


    def adresse_mail(self):
        mail_user = self.mail


    #
    # server = smtplib.SMTP()
    # # server.set_debuglevel(1) # Décommenter pour activer le debug
    # server.connect('smtp.toto.fr')
    #
    # server.helo()
    #
    # fromaddr = 'TOTO <moi@toto.fr>'
    # toaddrs = ['']  # On peut mettre autant d'adresses que l'on souhaite
    # sujet = "Un Mail avec Python"
    # html = u"""\
    # <html>
    # <head>
    # <meta charset="utf-8" />
    # </head>
    # <body>
    # <div>
    # Velit morbi ultrices magna integer.
    # Metus netus nascetur amet cum viverra ve cum.
    # Curae fusce condimentum interdum felis sit risus.
    # Proin class condimentum praesent hendrer
    # it donec odio facilisi sit.
    # Etiam massa tempus scelerisque curae habitasse vestibulum arcu metus iaculis hac.
    # </div>
    # </body
    # </html>
    # """
    #
    # msg = MIMEMultipart('alternative')
    # msg['Subject'] = sujet
    # msg['From'] = fromaddr
    # msg['To'] = ','.join(toaddrs)
    #
    # part = MIMEText(html, 'html')
    # msg.attach(part)
    #
    # try:
    #     server.sendmail(fromaddr, toaddrs, msg.as_string())
    # except smtplib.SMTPException as e:
    #     print(e)
    #
    # server.quit()

#TEST
if __name__ == "__main__":
    u = Mail_Crea("145")
    print(str(u))
