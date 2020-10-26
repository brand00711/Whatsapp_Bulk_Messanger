from flask import render_template
from app import app
from flask import Flask
    
import webbrowser as web
import time
import pyautogui as pg
import os
import pandas as pd
import socket
import datetime
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
IPAddr = str(IPAddr)

def create_app():
    app = Flask(__name__)

    @app.route('/')

    @app.route('/index')
    @app.route('/home')
    def index():
        user = {'username': 'Josh'}
        return render_template('home.html', title='Home', user=user)


    @app.route('/general')
    def general():
        
        user = {'username': 'Josh'}
        return render_template('general.html', title='General Message', user=user)

    @app.route('/9g')
    def nine_g():
        
        user = {'username': 'Josh'}
        return render_template('9g.html', title='9th Class General Message', user=user)


    @app.route('/9ag')
    def nine_ag():
        
        user = {'username': 'Josh'}
        return render_template('9ag.html', title='9th Class General Message', user=user)

    @app.route('/9ag_send')
    def nine_ag_send():
    
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9AG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/9bg')
    def nine_bg():
        
        user = {'username': 'Josh'}
        return render_template('9bg.html', title='9th Class General Message', user=user)


    @app.route('/9bg_send')
    def nine_bg_send():
        

        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9BG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')



    @app.route('/9abg')
    def nine_abg():
        
        user = {'username': 'Josh'}
        return render_template('9abg.html', title='9th Class General Message', user=user)


    @app.route('/9abg_send')
    def nine_abg_send():
        
    
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9ABG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')



    @app.route('/10g')
    def ten_g():
        
        user = {'username': 'Josh'}
        return render_template('10g.html', title='10th Class General Message', user=user)

    @app.route('/10ag')
    def ten_ag():
        
        user = {'username': 'Josh'}
        return render_template('10ag.html', title='10th Class General Message', user=user)

    @app.route('/10ag_send')
    def ten_ag_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10AG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/10bg')
    def ten_bg():
        
        user = {'username': 'Josh'}
        return render_template('10bg.html', title='10th Class General Message', user=user)

    @app.route('/10bg_send')
    def ten_bg_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10BG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/10abg')
    def ten_abg():
        
        user = {'username': 'Josh'}
        return render_template('10abg.html', title='10th Class General Message', user=user)

    @app.route('/10abg_send')
    def ten_abg_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10ABG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(25)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/11g')
    def eleven_g():
        
        user = {'username': 'Josh'}
        return render_template('11g.html', title='10th Class General Message', user=user)

    @app.route('/11ag')
    def eleven_ag():
        
        user = {'username': 'Josh'}
        return render_template('11ag.html', title='10th Class General Message', user=user)

    @app.route('/11ag_send')
    def eleven_ag_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11AG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/11bg')
    def eleven_bg():
        
        user = {'username': 'Josh'}
        return render_template('11bg.html', title='11th Class General Message', user=user)

    @app.route('/11bg_send')
    def eleven_bg_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11BG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/11abg')
    def eleven_abg():
        
        user = {'username': 'Josh'}
        return render_template('11abg.html', title='11th Class General Message', user=user)

    @app.route('/11abg_send')
    def eleven_abg_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11ABG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/12g')
    def twelve_g():
        
        user = {'username': 'Josh'}
        return render_template('12g.html', title='12th Class General Message', user=user)

    @app.route('/12ag')
    def twelve_ag():
        
        user = {'username': 'Josh'}
        return render_template('12ag.html', title='12th Class General Message', user=user)

    @app.route('/12ag_send')
    def twelve_ag_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12AG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/12bg')
    def twelve_bg():
        
        user = {'username': 'Josh'}
        return render_template('12bg.html', title='12th Class General Message', user=user)

    @app.route('/12bg_send')
    def twelve_bg_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12BG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/12abg')
    def twelve_abg():
        
        user = {'username': 'Josh'}
        return render_template('12abg.html', title='12th Class General Message', user=user)

    @app.route('/12abg_send')
    def twelve_abg_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12ABG.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/gen_all')
    def gen_all():
        
        user = {'username': 'Josh'}
        return render_template('gen_all.html', title='General Message', user=user)

    @app.route('/gen_all_send')
    def gen_all_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("generalmsgs.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/custom')
    def custom():
        
        user = {'username': 'Josh'}
        return render_template('custom.html', title='General Message', user=user)

    @app.route('/custom_all')
    def custom_all():
        
        user = {'username': 'Josh'}
        return render_template('custom_all.html', title='General Message', user=user)


    @app.route('/custom_all_send')
    def custom_all_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("custommsgs.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/9c')
    def nine_c():
        
        user = {'username': 'Josh'}
        return render_template('9c.html', title='9th Class General Message', user=user)


    @app.route('/9ac')
    def nine_ac():
        
        user = {'username': 'Josh'}
        return render_template('9ac.html', title='9th Class General Message', user=user)

    @app.route('/9ac_send')
    def nine_ac_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9AC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')



    @app.route('/9bc')
    def nine_bc():
        
        user = {'username': 'Josh'}
        return render_template('9bc.html', title='9th Class General Message', user=user)

    @app.route('/9bc_send')
    def nine_bc_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9BC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')




    @app.route('/9abc')
    def nine_abc():
        
        user = {'username': 'Josh'}
        return render_template('9abc.html', title='9th Class General Message', user=user)

    @app.route('/9abc_send')
    def nine_abc_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9ABC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')




    @app.route('/10c')
    def ten_c():
        
        user = {'username': 'Josh'}
        return render_template('10c.html', title='10th Class General Message', user=user)


    @app.route('/10ac')
    def ten_ac():
        
        user = {'username': 'Josh'}
        return render_template('10ac.html', title='10th Class General Message', user=user)

    @app.route('/10ac_send')
    def ten_ac_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10AC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')



    @app.route('/10bc')
    def ten_bc():
        
        user = {'username': 'Josh'}
        return render_template('10bc.html', title='10th Class General Message', user=user)

    @app.route('/10bc_send')
    def ten_bc_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10BC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/10abc')
    def ten_abc():
        
        user = {'username': 'Josh'}
        return render_template('10abc.html', title='10th Class General Message', user=user)

    @app.route('/10abc_send')
    def ten_abc_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10ABC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/11c')
    def eleven_c():
        
        user = {'username': 'Josh'}
        return render_template('11c.html', title='10th Class General Message', user=user)

    @app.route('/11ac')
    def eleven_ac():
        
        user = {'username': 'Josh'}
        return render_template('11ac.html', title='10th Class General Message', user=user)

    @app.route('/11ac_send')
    def eleven_ac_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11AC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/11bc')
    def eleven_bc():
        
        user = {'username': 'Josh'}
        return render_template('11bc.html', title='11th Class General Message', user=user)

    @app.route('/11bc_send')
    def eleven_bc_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11BC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/11abc')
    def eleven_abc():
        
        user = {'username': 'Josh'}
        return render_template('11abc.html', title='11th Class General Message', user=user)

    @app.route('/11abc_send')
    def eleven_abc_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11ABC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/12c')
    def twelve_c():
        
        user = {'username': 'Josh'}
        return render_template('12c.html', title='12th Class General Message', user=user)

    @app.route('/12ac')
    def twelve_ac():
        
        user = {'username': 'Josh'}
        return render_template('12ac.html', title='12th Class General Message', user=user)

    @app.route('/12ac_send')
    def twelve_ac_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12AC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/12bc')
    def twelve_bc():
        
        user = {'username': 'Josh'}
        return render_template('12bc.html', title='12th Class General Message', user=user)

    @app.route('/12bc_send')
    def twelve_bc_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12BC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/12abc')
    def twelve_abc():
        
        user = {'username': 'Josh'}
        return render_template('12abc.html', title='12th Class General Message', user=user)

    @app.route('/12abc_send')
    def twelve_abc_send():
    
            
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12ABC.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    message=message.replace("(name)",name)

                    if i>0:
                        message=message.replace(str(names_list[i-1]),name)

                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/about')
    def about():
        
        user = {'username': 'Josh'}
        return render_template('about.html', title='About', user=user)


    @app.route('/general_msg')

    def general_msg():
        

        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("generalmsgs.xlsx")
                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values

                message_list = dataset.iloc[:,2].values
                message = message_list[0]
                message=str(message)
                print(message)

                for i in range(len(names_list)):
                    
                    name=str(names_list[i])
                    number=str(numbers_list[i])
                    
                    if(i%30==0):
                        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(25)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(25)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(25)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            

                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/Marksheet')
    def marksheet():

        user = {'username': 'Josh'}
        return render_template('Marksheet.html', title='General Message', user=user)

    @app.route('/9m')
    def nine_marks():

        user = {'username': 'Josh'}
        return render_template('9m.html', title='General Message', user=user)


    @app.route('/9am')
    def nine_am():
        
        user = {'username': 'Josh'}
        return render_template('9am.html', title='9th Class General Message', user=user)


    @app.route('/9bm')
    def nine_bm():
        
        user = {'username': 'Josh'}
        return render_template('9bm.html', title='9th Class General Message', user=user)


    @app.route('/9abm')
    def nine_abm():
        
        user = {'username': 'Josh'}
        return render_template('9abm.html', title='9th Class General Message', user=user)

    @app.route('/10m')
    def ten_marks():

        user = {'username': 'Josh'}
        return render_template('10m.html', title='General Message', user=user)

    @app.route('/10am')
    def ten_am():
        
        user = {'username': 'Josh'}
        return render_template('10am.html', title='9th Class General Message', user=user)

    @app.route('/10bm')
    def ten_bm():
        
        user = {'username': 'Josh'}
        return render_template('10bm.html', title='9th Class General Message', user=user)

    @app.route('/10abm')
    def ten_abm():
        
        user = {'username': 'Josh'}
        return render_template('10abm.html', title='9th Class General Message', user=user)

    @app.route('/11m')
    def eleven_marks():

        user = {'username': 'Josh'}
        return render_template('11m.html', title='General Message', user=user)

    @app.route('/11am')
    def eleven_am():
        
        user = {'username': 'Josh'}
        return render_template('11am.html', title='9th Class General Message', user=user)


    @app.route('/11bm')
    def eleven_bm():
        
        user = {'username': 'Josh'}
        return render_template('11bm.html', title='9th Class General Message', user=user)


    @app.route('/11abm')
    def eleven_abm():
        
        user = {'username': 'Josh'}
        return render_template('11abm.html', title='9th Class General Message', user=user)

    @app.route('/12m')
    def twelve_marks():

        user = {'username': 'Josh'}
        return render_template('12m.html', title='General Message', user=user)


    @app.route('/12am')
    def twelve_am():
        
        user = {'username': 'Josh'}
        return render_template('12am.html', title='9th Class General Message', user=user)

    @app.route('/12bm')
    def twelve_bm():
        
        user = {'username': 'Josh'}
        return render_template('12bm.html', title='9th Class General Message', user=user)

    @app.route('/12abm')
    def twelve_abm():
        
        user = {'username': 'Josh'}
        return render_template('12abm.html', title='9th Class General Message', user=user)

    @app.route('/marks_all')
    def marks_all():
        
        user = {'username': 'Josh'}
        return render_template('marks_all.html', title='9th Class General Message', user=user)

    @app.route('/9am_send')
    def nine_a_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9Am.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    '''

                    message=message.replace("(name)",name)                              #Done
                    message=message.replace("(test_date)",test_date)                    #Done
                    message=message.replace("(phy)",str(phy))                           #Done
                    message=message.replace("(phy_rank)",str(phy_rank))                 #Done
                    message=message.replace("(phy_high)",str(phy_high))                 #Done
                    message=message.replace("(phy_avg)",str(phy_avg))                   #Done
                    message=message.replace("(chem)",str(chem))                         #Done
                    message=message.replace("(chem_rank)",str(chem_rank))               #Done
                    message=message.replace("(chem_high)",str(chem_high))               #Done
                    message=message.replace("(chem_avg)",str(chem_avg))                 #Done
                    message=message.replace("(maths)",str(maths))                       #Done
                    message=message.replace("(math_rank)",str(math_rank))               #Done
                    message=message.replace("(math_high)",str(math_high))               #Done
                    message=message.replace("(math_avg)",str(math_avg))                 #Done
                    message=message.replace("(total)",str(total))                       #Done
                    message=message.replace("(total_rank)",str(total_rank))             #Done
                    message=message.replace("(total_high)",str(total_high))             #Done
                    message=message.replace("(total_avg)",str(total_avg))               #Done

                

                    if i>0:
                        message=message.replace(names_list[i-1],name)

                        message=message.replace(str(math_list[i-1]),str(maths))
                        message=message.replace(str(chem_list[i-1]),str(chem))
                        message=message.replace(str(phy_list[i-1]),str(phy))
                        message=message.replace(str(total_list[i-1]),str(total))
                        
                        message=message.replace(str(math_rank_list[i-1]),str(math_rank))
                        message=message.replace(str(chem_rank_list[i-1]),str(chem_rank))
                        message=message.replace(str(phy_rank_list[i-1]),str(phy_rank))
                        message=message.replace(str(total_rank_list[i-1]),str(total_rank))

                        # message=message.replace(names_list[i-1],name)

                        '''
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/9bm_send')
    def nine_b_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9Bm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')



    @app.route('/9abm_send')
    def nine_ab_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9ABm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/10am_send')
    def ten_a_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10Am.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/10bm_send')
    def ten_b_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10Bm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/10abm_send')
    def ten_ab_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10ABm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/11am_send')
    def eleven_a_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11Am.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

    @app.route('/11bm_send')
    def eleven_b_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11Bm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/11abm_send')
    def eleven_ab_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11ABm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/12am_send')
    def twelve_a_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12Am.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/12bm_send')
    def twelve_b_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12Bm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/12abm_send')
    def twelve_ab_marks():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12ABm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                    
                    
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')
                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')


    @app.route('/marks_all_send')
    def marks_all_send():

        
        d1=datetime.datetime.now()
        d2=datetime.datetime(2020,9,8)

        '''FAIL SAFE IS OPTIONAL(RECOMMENDED)'''
        # pg.FAILSAFE = False
        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9Am.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("9Bm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10Am.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("10Bm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11Am.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("11Bm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12Am.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')

        if d1<d2:
            if IPAddr == "192.168.43.41":

                dataset = pd.read_excel("12Bm.xlsx")

                names_list = dataset.iloc[:,0].values
                numbers_list = dataset.iloc[:,1].values
                phy_list = dataset.iloc[:,2].values
                phy_rank_list = dataset.iloc[:,3].values
                phy_high_list = dataset.iloc[:,4].values
                phy_avg_list = dataset.iloc[:,5].values
                chem_list = dataset.iloc[:,6].values
                chem_rank_list = dataset.iloc[:,7].values
                chem_high_list = dataset.iloc[:,8].values
                chem_avg_list = dataset.iloc[:,9].values
                math_list = dataset.iloc[:,10].values
                math_rank_list = dataset.iloc[:,11].values
                math_high_list = dataset.iloc[:,12].values
                math_avg_list = dataset.iloc[:,13].values
                total_list = dataset.iloc[:,14].values
                total_rank_list = dataset.iloc[:,15].values
                total_high_list = dataset.iloc[:,16].values
                total_avg_list = dataset.iloc[:,17].values
                max_marks_list = dataset.iloc[:,18].values
                exam_pattern_list = dataset.iloc[:,19].values
                test_date_list = dataset.iloc[:,20].values

                phy_avg=phy_avg_list[0]
                chem_avg=chem_avg_list[0]
                math_avg=math_avg_list[0]
                total_avg=total_avg_list[0]

                phy_high=phy_high_list[0]
                chem_high=chem_high_list[0]
                math_high=math_high_list[0]
                total_high=total_high_list[0]

            
                max_marks=str(max_marks_list[0])
                exam_pattern = str(exam_pattern_list[0])
                test_date = str(test_date_list[0])

                # message_list = dataset.iloc[:,21].values
                # message = message_list[0]
                # message=str(message)
                # print(message)

                for i in range(len(names_list)):

                    name=str(names_list[i])
                    number=str(numbers_list[i])

                    chem=str(chem_list[i]) 
                    phy=str(phy_list[i])
                    maths=str(math_list[i])
                    total=str(total_list[i])

                    phy_rank=str(phy_rank_list[i])
                    chem_rank=str(chem_rank_list[i])
                    math_rank=str(math_rank_list[i])
                    total_rank=str(total_rank_list[i])

                    message=("Dear Parent, Result of {}                                                                                 "
                            "Test Date : {}                                                                                             "
                            "Pattern: {}                                                                                                "
                            "Max Marks: {}                                                                                              "
                            "~~~~~~~~~~                                                                                                 "
                            "*{} Result*                                                                                                "
                            "Math: {} (Rank: {})                                                                                        "
                            "Phy: {} (Rank: {})                                                                                         "
                            "Chem: {} (Rank: {})                                                                                        "
                            "Total: {} (Rank: {})                                                                                       "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Highest*                                                                                            "
                            "Maths: {}                                                                                                  "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}                                                                                                  "
                            "~~~~~~~~~~                                                                                                 "
                            "*Class Average*                                                                                            "
                            "Math: {}                                                                                                   "
                            "Phy: {}                                                                                                    "
                            "Chem: {}                                                                                                   "
                            "Total: {}".format(name,test_date,exam_pattern,max_marks,name,maths,math_rank,phy,phy_rank,chem,chem_rank,total,total_rank,math_high,phy_high,chem_high,total_high,math_avg,phy_avg,chem_avg,total_avg))

                
                    if(i%30==0):
                        time.sleep(2)        
                        os.system("taskkill /im chrome.exe /f")
                        
                        if len(number)==12:

                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==10:
                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                                        
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(24)
                            pg.press('enter')
                            time.sleep(1)
                            pg.press('enter')

                    else:
                        if len(number)==12:
                    
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==10:

                            number = 910000000000+int(number)
                            number = str(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')

                        if len(number)==11:

                            number = str(number)
                            number = number[1:]
                            number = 910000000000+int(number)
                            
                            web.open('https://web.whatsapp.com/send?phone=+'+number+'&text='+message)
                            time.sleep(11)
                            pg.press('enter')
                            
                time.sleep(2)
                os.system("taskkill /im chrome.exe /f")

            else: 
                return render_template('user_error.html', title='Error!')
        else:
            return render_template('time_exceed.html', title='Error!')



    @app.route('/contact')
    def contact():
        user = {'username': 'Josh'}
        return render_template('contact.html', title='Home', user=user)

    @app.route('/user_error')
    def user_error():
        
        user = {'username': 'Josh'}
        return render_template('user_error.html', title='12th Class General Message', user=user)

    return app

if __name__=="__main__":
    app=create_app
    app.run()