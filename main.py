import numpy as np
import cv2

def out_video():
    # connect web-cam
    cap = cv2.VideoCapture(0)
    # connect ip-cam
    stream = cv2.VideoCapture('rtsp://admin:12345678@192.168.0.100:10554/tcp/av0_0')
    while (True):
        # get images of web-cam
        ret_web, frame_web = cap.read()
        # get images of ip-cam
        ret_ip, frame_ip = stream.read()

        frame_web = cv2.resize(frame_web, (800, 600))
        frame_ip = cv2.resize(frame_ip, (800, 600))

        frame = np.vstack((frame_web, frame_ip))

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    stream.release()
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    out_video()

