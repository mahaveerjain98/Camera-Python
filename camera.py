import cv2
import time

if __name__=="__main__":
    casc_path="haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(casc_path)
    curr_frame = 1
    video_capture = False
    gray_filter= False
    rgb_filter = False

    def vid(name="videos/videostream.avi",fps=25,frame_size= (640,480) ):
        out = cv2.VideoWriter( str(name), cv2.VideoWriter_fourcc(*'MJPG') ,fps, frame_size)
        return out

    cap = cv2.VideoCapture(0)
    texts=''
    print("Camera Opened")
    while(True):
        ret, image = cap.read()
        frame = cv2.flip(image,1)
        if not ret: break
        if ret:
            #add transforms of the image if needed such as resize ,blur and etc..
            st=time.time()
            key= cv2.waitKey(5) & 0xff
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face = faceCascade.detectMultiScale(frame,scaleFactor=1.2,minNeighbors=4)
    #image capture and save
            if key == ord('s'):
                name = "_" + str(curr_frame) + ".jpg" #saving the image as you need
                curr_frame += 1
                cv2.imwrite(f"images/img{name}", frame)# wirte it into your path or yield into a generator by creating a function
                et=time.time()
                texts="Image saved "+str(name)
                print(texts)
    #stop video
            elif key == ord('b'):
                if video_capture:
                    video_capture=False
                    et=time.time()
                    texts="Video recording ended" 
                    print("Total Video Capture time :",et-vt)
                else:
                    texts="Video is not started\nStart the Video Recording"
    #normal video
            elif key == ord('v'): 
                if video_capture==False:
                    video_capture=True
                    output=vid(name="Video.avi")
                    vt=time.time()
                else :
                    texts="Stop the previous recording then start this recording"
    #fast video
            elif key == ord('f'): 
                if video_capture==False:
                    video_capture=True
                    output=vid(name="Fast_video.avi",fps=90)
                    vt=time.time()
                else :
                    texts="Stop the previous recording then start this recording"
    #Slow_mo_video
            elif key ==ord('d'): 
                if video_capture==False:
                    video_capture=True
                    output=vid(name="Slowmo_video.avi",fps=15)
                    vt=time.time()
                else :
                    texts="Stop the previous recording then start this recording"
    #pause/resume       
            elif key== ord('p'): 
                if video_capture:
                    video_capture = False
                    texts="Video Paused"
                else:
                    video_capture = True   
                    texts="Video resumed"
    #close                
            elif key == ord('q'):  
                if video_capture:
                    texts="End the Video by 'b' and then quit"
                else:
                    print("\nCamera Close")
                break
    #gray filter on/off
            elif key == ord('g'):
                if gray_filter:
                    gray_filter=False
                else:
                    gray_filter= True
            elif gray_filter:
                frame=gray
    #rgb filter on/off
            elif key == ord('r'):
                if rgb_filter:
                    rgb_filter = False
                else:
                    rgb_filter = True
            elif rgb_filter:
                frame=rgb
    #start recording any type        
            elif video_capture:    
                texts="Video recording starts....... Tap 'b' to end the recording"
                output.write(frame) # to write the images in a video
                output.release()
    #face detection
            for (x, y, w, h) in face:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (150, 100, 0), 2)
                cv2.putText(frame,"Person Detected",(x-10, y-10),cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
    #option show on image
            cv2.putText(frame,texts,(10,50), cv2.FONT_HERSHEY_PLAIN, 1,(209, 80, 0, 255), 1) #image,text,position,font,fontcolor,stroke)
            cv2.imshow('img',frame)   

    cv2.destroyAllWindows()
    cap.release()
