**Problem Statement:**
Build a keylogger in python which performs the following:
1. Logs keys pressed
2. Gathers computer information
3. Gathers network information
4. Gets the clipboard contents
5. Records the user's microphone
6. Takes screenshots of the computer screen 

Encrypt all of these files, send them through email and delete original files from user's computer.

**Disclaimer**

This project has been built only for academic purposes. Strict consent is a must before using this code. It is the end user’s responsibility to obey all applicable local, state and federal laws. Developer assumes no liability and is not responsible for any misuse or damage caused by this software in general.

**Project Workflow**

<img align='center'>![Capture](https://user-images.githubusercontent.com/106017337/216836289-c9f4825a-cddf-4e50-841b-c8c75b83383d.JPG)</img>


**Libraries Used**

1. Logging Keys: pynput.keyboard
2. Email: smtplib, email.mime
3. Computer Information: platform, os  
4. Network Information: socket 
5. Clipboard: win32clipboard 
6. Screenshots: multiprocessing, PIL 
7. Microphone: scipy.io.wavfile, sounddevice 
8. Cryptography: cryptography.fernet 


**Work Breakdown Structure**


<img align='center'>![crypt](https://user-images.githubusercontent.com/106017337/216979598-49477750-2631-4603-9fc1-dcbd6b5128ee.jpg)</img>

