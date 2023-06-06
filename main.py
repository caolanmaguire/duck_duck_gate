#import opencv
import cv2

def main():

    #Select Camera
    cam = cv2.VideoCapture(0)

    #Loop - show each frame
    while(True):

        ret, frame = cam.read()

        #Write count to image
        cv2.putText(frame, 'Count : ', (5,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
        #display image
        cv2.imshow('frame',frame)

        #Add break in case user wants to exit - q key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    #release camera once loop broken
    cam.release()

    #destroy all windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()