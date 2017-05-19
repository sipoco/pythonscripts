import threading, time
print('Start!')

def takeANap():
    time.sleep(5)
    print('Wakey wakey... WAKE up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()
print('Done, einde van het programma!')
