#chat_auto_open_2

#importing the libraries
import pyautogui as p
from selenium import webdriver
import winsound
from selenium.webdriver.common.keys import Keys
import time as t
import schedule
import smtplib
import os


#the code
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
    t.sleep(5)

    print('opening a new window')
    #open new window
    p.hotkey('ctrl','t')
    t.sleep(0.5)
    p.write('https://www.zoho.com/mail/login.html')
    print('     waiting 3 seconds...')
    t.sleep(3)
    p.hotkey('enter')
    print('     waiting 10 seconds...')
    t.sleep(10)
    p.moveTo(923,-411)
    p.click()
    print('     waiting 10 seconds...')
    t.sleep(10)

    print('logining in the Zoho email')
    #opening the email new window
        #writing the email
    p.moveTo(488,-514)
    p.click()
    p.write('suporte@pctel.com.br')
    t.sleep(1)
    p.hotkey('enter')
    print('     waiting 5 seconds...')
    t.sleep(5)
        #writing the password
    p.moveTo(494,-463)
    p.click()
    p.write('Pctel@123')
    t.sleep(1)
    p.hotkey('enter')
    print('     waiting 5 seconds...')
    t.sleep(5)

    print('opening the Help Desk')
    #opening the Help Desk
        #writing the email
    p.hotkey('ctrl','t')
    t.sleep(1)
    p.write('http://pctel3.duckdns.org:40080')
    t.sleep(1)
    p.hotkey('enter')
    t.sleep(3)
    #login in the helpdesk
        #writing the email
    print('logining in the Help Desk')
    p.write('DIEGO.F')
    t.sleep(1)
        #writing the password
    p.hotkey('tab')
    p.write('pctel123')
    t.sleep(1)
    p.hotkey('enter')
    print('     waiting 5 seconds...')
    t.sleep(5)

    print('chat opening finished!')

chat()