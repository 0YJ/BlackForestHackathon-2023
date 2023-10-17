import os
import signal
import subprocess
import sys
import uuid
import cv2
from ultralytics import YOLO

BASEPATH = os.path.realpath(os.path.dirname(sys.argv[0]))
RECV = os.path.join(BASEPATH, 'received_frames')

print(" frames received at %s" % RECV)
os.makedirs(RECV, exist_ok=True)

working = False
fullname = False

def sigint_handler(signum, frame):
    global fullname, working
    print("\n")
    print(" about to cancel")
    if working and fullname:
        print(" unfinished file found. it will be killed")
        os.remove(f'{fullname}.tmp')
    sys.exit()
signal.signal(signal.SIGINT, sigint_handler)

n = 1
while True:
    recname = str(uuid.uuid1())
    print(f" [{n:8}] listening start and waiting for [{recname}]. ctrl+c to quit")
    fullname = os.path.join(RECV, recname)

    working = True
    subprocess.call(f'nc -lp 9999 > {fullname}.tmp', shell=True)
    os.rename(f'{fullname}.jpg', fullname)
    working = False

    n += 1
    
    model = YOLO('best.pt')
    
    images = [cv2.imread(file) for file in glob.glob("./received_frames/*.jpg")]

    results = model(frame)
    
    for result in results:
        label = result['label']  
        score = result['score']  
        cv2.putText(frame, f'{label}: {score}', ...)

    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
