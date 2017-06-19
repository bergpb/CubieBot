# -*- coding: UTF-8 -*-

from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import telepot
import time
import os
import commands
import urllib2

def handle(msg):

	command = msg['text']
	content_type, chat_type, chat_id = telepot.glance(msg)
	m = telepot.namedtuple.Message(**msg)
	

	def getinfo(chat_id):
		if chat_id < 0:
			print 'Menssage do tipo %s' % (content_type,)
			print '-------------------------------------'
			print 'Chat ID : %s' % m.chat[0]
			print 'Tipo de chat : %s' % m.chat[1]
			print 'Nome do Grupo: %s' % m.chat[2]
			print 'Username : %s' % m.chat[3]
			print 'First Name: %s' % m.chat[4]
			print 'Last Name: %s' % m.chat[5]
			print 'Enviada por %s' % (m.from_,)
      			print time.strftime('%Y-%m-%d %H:%M:%S')
			print '--------------------------------------'
		else:
			print 'Messagem do tipo %s ' % (content_type,)
			print '--------------------------------------'
			print 'Chat ID : %s' % m.chat[0]
			print 'Tipo de chat : %s' % m.chat[1]
			print 'Username : %s' % m.chat[3]
			print 'First Name: %s' % m.chat[4]
			print 'Last Name: %s' % m.chat[5]
      			print time.strftime('%Y-%m-%d %H:%M:%S')
			print '--------------------------------------'
	

	keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Memoria"), KeyboardButton(text="UpTime")],
            [KeyboardButton(text="UsoSD"),  KeyboardButton(text="Data")],
            [KeyboardButton(text="IP")],
        ])
	

	if command == '/start':
		bot.sendMessage(chat_id, ''' Bem Vindo!!!
Iniciando o Bot...
Use os comandos do teclado abaixo: ''', reply_markup=keyboard )
		getinfo(chat_id)
		
	elif command == 'Memoria':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'

		mem_total = commands.getoutput("free -h | grep 'Mem' | cut -c 15-18")
		mem_used = commands.getoutput("free -h | grep 'Mem' | cut -c 26-29")
		mem_free = commands.getoutput("free -h | grep 'Mem' | cut -c 37-40")
		bot.sendMessage(chat_id, '''Memoria total: %s
Memoria em uso: %s
Memoria livre: %s''' %(mem_total, mem_used, mem_free))
		
		getinfo(chat_id)
	

	elif command == 'UpTime':
		print '---------------------------'
		print 'Comando usado ',  command
		print '---------------------------'
		uptime = commands.getoutput("uptime")
		bot.sendMessage(chat_id, '''System Up Time: 
%s''' %uptime)
		getinfo(chat_id)
		
	elif command == 'UsoSD':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		partRoot = commands.getoutput("df -h | grep '/dev/root'| head -1")
		bot.sendMessage(chat_id, '''Root partition: 
%s''' %partRoot)
		getinfo(chat_id)
	
	elif command == 'Data':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		date = commands.getoutput("date")
 		bot.sendMessage(chat_id,'''Data e hora do Sistema: 
%s''' %date)
		getinfo(chat_id)
		
		
	elif command == 'IP':
		print '---------------------------'
		print 'Comando usado ', command
		print '---------------------------'
		# ip local 
		if chat_id == 24774270:
			
			# aqui pega o ip da lan   ** eth0 para cabo wlan0 para wifi **
			ip_lan = commands.getoutput("sudo ifconfig eth0 |  grep inet | cut -c 21-35 | head -1")
			bot.sendMessage(chat_id, 'IP Local: %s' %ip_lan)
			
			#ip externo so pra min
			if chat_id == 24774270:	
				# aqui pega o ip externo dessa bagaÃ§a 
				response = urllib2.urlopen('http://bot.whatismyipaddress.com/')
				ip_ex = response.read()			
				bot.sendMessage(chat_id, 'IP Externo: %s' %ip_ex)
	
		else:
			bot.sendMessage(chat_id, 'No permissions')
			getinfo(chat_id)	
		
	else:
    		bot.sendMessage(chat_id, 'Invalid Command')
		
bot = telepot.Bot('seu token aqui')
bot.message_loop(handle)

print 'Aguardando comandos ...'

while 1:
	time.sleep(5)
