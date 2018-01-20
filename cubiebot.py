# -*- coding: UTF-8 -*-

import os
import time
import telepot
import urllib2
import commands
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def handle(msg):

    command = msg['text']
    content_type, chat_type, chat_id = telepot.glance(msg)
    m = telepot.namedtuple.Message(**msg)
    
    def getinfo(chat_id):
        if chat_id < 0:
            print 'Type of message %s' % (content_type,)
            print '-------------------------------------'
            print 'Chat ID : %s' % m.chat[0]
            print 'Chat type: %s' % m.chat[1]
            print 'Group name: %s' % m.chat[2]
            print 'Username : %s' % m.chat[3]
            print 'First Name: %s' % m.chat[4]
            print 'Last Name: %s' % m.chat[5]
            print 'Send from %s' % (m.from_,)
                print time.strftime('%Y-%m-%d %H:%M:%S')
            print '--------------------------------------'
        else:
            print 'Type of message %s ' % (content_type,)
            print '--------------------------------------'
            print 'Chat ID : %s' % m.chat[0]
            print 'Chat type : %s' % m.chat[1]
            print 'Username : %s' % m.chat[3]
            print 'First Name: %s' % m.chat[4]
            print 'Last Name: %s' % m.chat[5]
                print time.strftime('%Y-%m-%d %H:%M:%S')
            print '--------------------------------------'
    

    keyboard=ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Memory"), KeyboardButton(text="UpTime")],
            [KeyboardButton(text="SdUse"),  KeyboardButton(text="DateTime")],
            [KeyboardButton(text="IP")],
        ])
    

    if command == '/start':
        bot.sendMessage(chat_id, '''Hello!
Starting bot
Use commands in keyboard ''', reply_markup=keyboard )
        getinfo(chat_id)
        
    elif command == 'Memory':
        print '---------------------------'
        print 'Received command: ', command
        print '---------------------------'

        mem_total = commands.getoutput("free -h | grep 'Mem' | cut -c 15-18")
        mem_used = commands.getoutput("free -h | grep 'Mem' | cut -c 26-29")
        mem_free = commands.getoutput("free -h | grep 'Mem' | cut -c 37-40")
        bot.sendMessage(chat_id, '''Total memory: %s
Used memory: %s
Free memory: %s''' %(mem_total, mem_used, mem_free))
        
        getinfo(chat_id)
    

    elif command == 'UpTime':
        print '---------------------------'
        print 'Received command: ',  command
        print '---------------------------'
        uptime = commands.getoutput("uptime")
        bot.sendMessage(chat_id, '''System Up Time: 
%s''' %uptime)
        getinfo(chat_id)
        
    elif command == 'SdUse':
        print '---------------------------'
        print 'Received command: ', command
        print '---------------------------'
        partRoot = commands.getoutput("df -h | grep '/dev/root'| head -1")
        bot.sendMessage(chat_id, '''Root partition: 
%s''' %partRoot)
        getinfo(chat_id)
    
    elif command == 'DataTime':
        print '---------------------------'
        print 'Received command: ', command
        print '---------------------------'
        date = commands.getoutput("date")
        bot.sendMessage(chat_id,'''Date and time: 
%s''' %date)
        getinfo(chat_id)
        
        
    elif command == 'IP':
        print '---------------------------'
        print 'Received command: ', command
        print '---------------------------'
        # ip local 
        if chat_id == 24774270:
            
            # aqui pega o ip da lan   ** eth0 para cabo wlan0 para wifi **
            ip_lan = commands.getoutput("sudo ifconfig eth0 |  grep inet | cut -c 21-35 | head -1")
            bot.sendMessage(chat_id, 'Local IP: %s' %ip_lan)
            
            #ip externo so pra min
            if chat_id == 24774270: 
                # aqui pega o ip externo dessa bagaÃ§a 
                response = urllib2.urlopen('http://bot.whatismyipaddress.com/')
                ip_ex = response.read()         
                bot.sendMessage(chat_id, 'External IP: %s' %ip_ex)
    
        else:
            bot.sendMessage(chat_id, 'No permissions')
            getinfo(chat_id)    
        
    else:
            bot.sendMessage(chat_id, 'Invalid Command')
        
bot = telepot.Bot('yourtokenhere')
bot.message_loop(handle)

print 'Waiting ...'

while 1:
    time.sleep(5)
