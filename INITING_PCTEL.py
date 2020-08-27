#INITING_PCTEL

#Tentativa de automatizar a abertura de todos os recursos necessários para o trabalho com a Pctel
#Auomatize trie to open all necessaries resourses to work with a Pctel (wrong write)
#Attemp to automate the opening of all resources made available to work with a Pctel

import pyautogui as p
from selenium import webdriver
import winsound
from selenium.webdriver.common.keys import Keys
import time
import schedule
import smtplib
import os

#declarando variáveis(declaring variavals)
hora_entrada = '09:22'
hora_saida = '18:00'
hora_zoiper = '09:22'
hora_bloco_notas = '09:22'
hora_chat = '09:24'


#definindo as funções(definign the functions)
def envio_email_entrada():
    sender_email= "diegopaladinofoto@gmail.com"
    rec_email="diegopaladinofoto@gmail.com"
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
    rec_email="diegopaladinofoto@gmail.com"
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


def chat():
    print('opening the Firefox')
    #buscando o executável do drive do Firefox
    operadriver='C://Users//diego//OneDrive//Desktop//DESKTOP//PROGRAMAS//MOZILA//geckodriver.exe'
    driver = webdriver.Firefox()

    #solicitando a abertura de uma página
    driver.get('http://dashboard.tawk.to')
    driver.set_window_position(166,-700)
    driver.maximize_window()

    print('logining in the chat')
    #efetuando o login na página inicial
    username = driver.find_element_by_id('email')
    password = driver.find_element_by_id('password')
    username.send_keys('expedicao@pctel.com.br')
    password.send_keys('pctel123')
    t.sleep(0.5)
    p.hotkey('enter')
    print('     waiting 5 seconds...')
    time.sleep(5)

    print('opening a new window')
    #open new window
    p.hotkey('ctrl','t')
    time.sleep(0.5)
    p.write('https://www.zoho.com/mail/login.html')
    print('     waiting 3 seconds...')
    time.sleep(3)
    p.hotkey('enter')
    print('     waiting 10 seconds...')
    time.sleep(10)
    p.moveTo(923,-411)
    p.click()
    print('     waiting 10 seconds...')
    time.sleep(10)

    print('logining in the Zoho email')
    #opening the email new window
        #writing the email
    p.moveTo(488,-514)
    p.click()
    p.write('suporte@pctel.com.br')
    time.sleep(1)
    p.hotkey('enter')
    print('     waiting 5 seconds...')
    time.sleep(5)
        #writing the password
    p.moveTo(494,-463)
    p.click()
    p.write('Pctel@123')
    time.sleep(1)
    p.hotkey('enter')
    print('     waiting 5 seconds...')
    time.sleep(5)

    print('opening the Help Desk')
    #opening the Help Desk
        #writing the email
    p.hotkey('ctrl','t')
    time.sleep(1)
    p.write('http://pctel3.duckdns.org:40080')
    time.sleep(1)
    p.hotkey('enter')
    time.sleep(3)
    #login in the helpdesk
        #writing the email
    print('logining in the Help Desk')
    p.write('DIEGO.F')
    time.sleep(1)
        #writing the password
    p.hotkey('tab')
    p.write('pctel123')
    time.sleep(1)
    p.hotkey('enter')
    print('     waiting 5 seconds...')
    time.sleep(5)

    print('chat opening finished!')

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

#Abrindo os chat e janelas secundárias(opening the chat and secundary windows)
schedule.every().monday.at(hora_chat).do(chat)
schedule.every().tuesday.at(hora_chat).do(chat)
schedule.every().wednesday.at(hora_chat).do(chat)
schedule.every().thursday.at(hora_chat).do(chat)
schedule.every().friday.at(hora_chat).do(chat)

while 1:
    schedule.run_pending()
    time.sleep(1)

os.exit(0)

p.keyDown('ctrl')
p.hotkey('c')
p.keyUp('ctrl')


exit()