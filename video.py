import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2 
def videocap():
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("videocap",frame)
        k=cv2.waitKey(1)
        if k==ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
