import schedule as s
import time as t

hora = '08:45'

def do():
    print('sucesso!')


s.every().thursday.at(hora).do(do)

while True:
		try:
			s.run_pending()
		except Exception as e:
			print ("Excepion running pending: %s" % (e))
		t.sleep(10)