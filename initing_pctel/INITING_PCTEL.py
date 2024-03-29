#INITING_PCTEL

#Tentativa de automatizar a abertura de todos os recursos necessários para o trabalho com a Pctel
#Auomatize trie to open all necessaries resourses to work with a Pctel (wrong write)
#Attemp to automate the opening of all resources made available to work with a Pctel

# title of tutorial(schedule): Como Agendar Scripts Python & Execução Paralela #DevAprender
# link of tutorial(schedule): https://www.youtube.com/watch?v=PAnrHMQBB-Y
# link of tutorial:


import pyautogui as p
from selenium import webdriver
import winsound
from selenium.webdriver.common.keys import Keys
import time as t
import schedule
import smtplib
import os

#declarando variáveis(declaring variavals)
hora_entrada = '06:00'
hora_saida = '12:00'
hora_zoiper = '06:00'
hora_bloco_notas = '06:00'
# hora_chat = '10:27'


#definindo as funções(definign the functions)
def envio_email_entrada():
    sender_email= "diegopaladinopctel@gmail.com"
    rec_email="ponto@pctel.com.br"
    password='paladino804680'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email, password)

    subject = 'PONTO DIEGO'
    body = 'ENTRADA: 06:00'

    msg = f'Subject: {subject}\n\n{body}'

    print("Login succes")
    server.sendmail(sender_email,rec_email,msg)
    print("Email has sent to",rec_email)

def envio_email_saida():
    sender_email= "diegopaladinopctel@gmail.com"
    rec_email="ponto@pctel.com.br"
    password='paladino804680'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email, password)

    subject = 'PONTO DIEGO'
    body = 'SAIDA: 12:00'

    msg = f'Subject: {subject}\n\n{body}'

    print("Login succes")
    server.sendmail(sender_email,rec_email,msg)
    print("Email has sent to",rec_email)

def mensagem_envio():
    print('mensagem enviada')

#defining the Zoiper software opening:
def zoiper():
    os.startfile('C:\Program Files (x86)\Attractel\Zoiper\Zoiper.exe')
    print('Zoiper opened')

#defining the notepads opening:
def bloco_notas():
    os.startfile(r'C:\Users\diego\OneDrive\Desktop\DESKTOP\ALC-BRASIL\PCTEL\BLOCO_NOTAS\ANOTAÇÕES_DIEGO_SUPORTE.txt')
    print('opening ANOTAÇÕES_DIEGO_SUPORTE')
    os.startfile(r'C:\Users\diego\OneDrive\Desktop\DESKTOP\ALC-BRASIL\PCTEL\BLOCO_NOTAS\COMANDOS-CMD.txt')
    print('opening COMANDOS-CMD')
    print('notepads opened')


# def chat():
#     print('opening the Firefox')
#     #buscando o executável do drive do Firefox
#     operadriver='C://Users//diego//OneDrive//Desktop//DESKTOP//PROGRAMAS//MOZILA//geckodriver.exe'
#     driver = webdriver.Firefox()

#     #solicitando a abertura de uma página
#     driver.get('http://dashboard.tawk.to')
#     driver.set_window_position(166,-700)
#     driver.maximize_window()

#     print('logining in the chat')
#     #efetuando o login na página inicial
#     username = driver.find_element_by_id('email')
#     password = driver.find_element_by_id('password')
#     username.send_keys('expedicao@pctel.com.br')
#     password.send_keys('pctel123')
#     t.sleep(0.5)
#     p.hotkey('enter')
#     print('     waiting 5 seconds...')
#     t.sleep(5)

#     print('opening a new window')
#     #open new window
#     p.hotkey('ctrl','t')
#     t.sleep(0.5)
#     p.write('https://www.zoho.com/mail/login.html')
#     print('     waiting 3 seconds...')
#     t.sleep(3)
#     p.hotkey('enter')
#     print('     waiting 10 seconds...')
#     t.sleep(10)
#     p.moveTo(923,-411)
#     p.click()
#     print('     waiting 10 seconds...')
#     t.sleep(10)

#     print('logining in the Zoho email')
#     #opening the email new window
#         #writing the email
#     p.moveTo(488,-514)
#     p.click()
#     p.write('suporte@pctel.com.br')
#     t.sleep(1)
#     p.hotkey('enter')
#     print('     waiting 5 seconds...')
#     t.sleep(5)
#         #writing the password
#     p.moveTo(494,-463)
#     p.click()
#     p.write('Pctel@123')
#     t.sleep(1)
#     p.hotkey('enter')
#     print('     waiting 5 seconds...')
#     t.sleep(5)

#     print('opening the Help Desk')
#     #opening the Help Desk
#         #writing the email
#     p.hotkey('ctrl','t')
#     t.sleep(1)
#     p.write('http://pctel3.duckdns.org:40080')
#     t.sleep(1)
#     p.hotkey('enter')
#     t.sleep(3)
#     #login in the helpdesk
#         #writing the email
#     print('logining in the Help Desk')
#     p.write('DIEGO.F')
#     t.sleep(1)
#         #writing the password
#     p.hotkey('tab')
#     p.write('pctel123')
#     t.sleep(1)
#     p.hotkey('enter')
#     print('     waiting 5 seconds...')
#     t.sleep(5)

#     print('chat opening finished!')

#lógica do schedule (schedule logic):
#schedule.cada.tempo.fazer(schedule.each.time.do)

#definindo a execução programada(defining the scheduled execution)
#Email de entrada no serviço(job entry email)
schedule.every().monday.at(hora_entrada).do(envio_email_entrada)
schedule.every().tuesday.at(hora_entrada).do(envio_email_entrada)
schedule.every().wednesday.at(hora_entrada).do(envio_email_entrada)
schedule.every().thursday.at(hora_entrada).do(envio_email_entrada)
schedule.every().friday.at(hora_entrada).do(envio_email_entrada)

#Email de saída no serviço(job outgoing email)
schedule.every().monday.at(hora_saida).do(envio_email_saida)
schedule.every().tuesday.at(hora_saida).do(envio_email_saida)
schedule.every().wednesday.at(hora_saida).do(envio_email_saida)
schedule.every().thursday.at(hora_saida).do(envio_email_saida)
schedule.every().friday.at(hora_saida).do(envio_email_saida)

#Abrindo o software Zoiper(opening the Zoiper software)
schedule.every().monday.at(hora_zoiper).do(zoiper)
schedule.every().tuesday.at(hora_zoiper).do(zoiper)
schedule.every().wednesday.at(hora_zoiper).do(zoiper)
schedule.every().thursday.at(hora_zoiper).do(zoiper)
schedule.every().friday.at(hora_zoiper).do(zoiper)

#Abrindo os blocos de notas(opening the notepads)
schedule.every().monday.at(hora_bloco_notas).do(bloco_notas)
schedule.every().tuesday.at(hora_bloco_notas).do(bloco_notas)
schedule.every().wednesday.at(hora_bloco_notas).do(bloco_notas)
schedule.every().thursday.at(hora_bloco_notas).do(bloco_notas)
schedule.every().friday.at(hora_bloco_notas).do(bloco_notas)

# #Abrindo os chat e janelas secundárias(opening the chat and secundary windows)
# schedule.every().monday.at(hora_chat).do(chat)
# schedule.every().tuesday.at(hora_chat).do(chat)
# schedule.every().wednesday.at(hora_chat).do(chat)
# schedule.every().thursday.at(hora_chat).do(chat)
# schedule.every().friday.at(hora_chat).do(chat)

# while 1:
#     schedule.run_pending()
#     t.sleep(1)

while True:
		try:
			schedule.run_pending()
		except Exception as e:
			print ("Excepion running pending: %s" % (e))
		t.sleep(10)    

#202010101607
#202010111928
