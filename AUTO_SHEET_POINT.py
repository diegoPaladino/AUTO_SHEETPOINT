#AUTO_SHEET_POINT

#SCRIPT_AUTOMATE-EMAIL_SEND
#Programa baseado no conteúdo do tutorial abaixo, após já ter sido criado o envio semiautomatico.
#Como Agendar Scripts Python & Execução Paralela #DevAprender
#LINK DO TUTORIAL: Como Agendar Scripts Python & Execução Paralela #DevAprender | https://www.youtube.com/watch?v=PAnrHMQBB-Y

import schedule
import time
import smtplib

def envio_email_entrada():
    sender_email= "diegopaladinofoto@gmail.com"
    rec_email="ponto@pctel.com.br"
    password='Paladio804680'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email, password)

    subject = 'PONTO DIEGO'
    body = 'ENTRADA: 12:00'

    msg = f'Subject: {subject}\n\n{body}'

    print("Login succes")
    server.sendmail(sender_email,rec_email,msg)
    print("Email has sent to",rec_email)

def envio_email_saida():
    sender_email= "diegopaladinofoto@gmail.com"
    rec_email="ponto@pctel.com.br"
    password='Paladio804680'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email, password)

    subject = 'PONTO DIEGO'
    body = 'SAIDA: 18:00'

    msg = f'Subject: {subject}\n\n{body}'

    print("Login succes")
    server.sendmail(sender_email,rec_email,msg)
    print("Email has sent to",rec_email)

def mensagem_envio():
    print('mensagem enviada')


#schedule.cada.tempo.fazer
#Entrada
schedule.every().monday.at('12:00').do(envio_email_entrada)
schedule.every().tuesday.at('12:00').do(envio_email_entrada)
schedule.every().wednesday.at('12:00').do(envio_email_entrada)
schedule.every().thursday.at('12:00').do(envio_email_entrada)
schedule.every().friday.at('12:00').do(envio_email_entrada)


#Saída
schedule.every().monday.at('18:00').do(envio_email_saida)
schedule.every().tuesday.at('18:00').do(envio_email_saida)
schedule.every().wednesday.at('18:00').do(envio_email_saida)
schedule.every().thursday.at('18:00').do(envio_email_saida)
schedule.every().friday.at('18:00').do(envio_email_saida)


while 1:
    schedule.run_pending()
    time.sleep(1)

