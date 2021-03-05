import cv2
import uuid

vs = cv2.VideoCapture(0)
width = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = vs.read()
    imgname = f'./Images/likeNight/{str(uuid.uuid1())}.jpg'
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


vs.release()
#vs.destroyAllWindows()
