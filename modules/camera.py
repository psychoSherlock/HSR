from cv2 import CAP_DSHOW, VideoCapture, imwrite


def webcamSnap(path):
    try:
        cam = VideoCapture(0)  # Add CAP_DSHOW
        t, selfie = cam.read()
        imwrite(path, selfie)
        return path
    except Exception as e:
        print(e)
        return path  # Change this to the 404 Image
