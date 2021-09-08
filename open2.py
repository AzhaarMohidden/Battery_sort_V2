import cv2
from time import sleep
import numpy as np
# import image_controller as ic
from reader import Log_reader as lg_r
import pytesseract
import threading
#------------------Image------------
# img = cv2.imread("lenna.png")
# cv2.imshow("Output",img)
# cv2.waitKey(0)
#------------------------------------------

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

det_num = 0

# Image controller bar values
# def track_values():
#     h_min = int(ic.Hue_min_val())
#     s_min = int(ic.Sat_min_val())
#     v_min = int(ic.Val_min_val())
#     h_max = int(ic.Hue_max_val())
#     s_max = int(ic.Sat_max_val())
#     v_max = int(ic.Val_max_val())
#     return np.array([h_min,s_min,v_min]), np.array([h_max,s_max,v_max])

def gry_img(source):
    gry = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY) #Gray Conversion
    # cv2.imshow("gray Image", gry)
    return gry

def Gausian_Blur(source, ad1, ad2, ad3):
    gryblr = cv2.GaussianBlur(source,(ad1,ad2),ad3) #GausianBlur (7,7),0
    # cv2.imshow("gray Image", gryblr)
    return gryblr

def Canny(source, ad1, ad2):
    Canny = cv2.Canny(source,ad1,ad2) #GausianBlur
    # cv2.imshow("gray Image", Canny)
    return Canny

def shape_def(source):
    peri = cv2.arcLength(source, True)
    approx = cv2.approxPolyDP(source, 0.03* peri, True)
    # print(len(approx))
    objCor = len(approx)
    if objCor == 3: shape = "Triangle"
    elif objCor == 4:
        x, y, w, h = cv2.boundingRect(approx)
        if(y!=0):
            r = x/y
        else:
            r = 1
        global det_num
        if(50>r>0):
            cropped = imagecon[y:y + h, x:x + w]
            # cv2.rectangle(imagecon, (x, y), (x + w, y + h), (0 ,0 ,255), 2,)
            shape = "Qadrilateral"
            # cv2.putText(imagecon, shape, ((x+w)+5, y), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0,0,240),1)
            text = str(pytesseract.image_to_string(cropped))
            # print("tes: "+ text)
            try:
                num = int(text)
                print("Serial: "+ str(num))
                # cv2.putText(imagecon, str(num), ((x+w)+5, y), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0,0,240),1)
                ser, soc = lg_r.info_read_vis(num)
                print("SOC: "+ str(soc))
                ser  = "Serial: " + str(ser)
                pers=int(soc)
                soc_1  = str(soc) +"%"
                # cv2.putText(imagecon, ser, ((x+w)+5, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)
                # cv2.putText(imagecon, soc, ((x+w)+5, y+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)
                pow = pers*3.6
                print(pow)
                det_num = det_num + 1

                if(det_num%2 == 1):
                    cv2.line(imagecon, ((x+w), y), ((x+w)+20,y-20), (0 ,0 ,255), 1,)
                    cv2.line(imagecon, ((x+w)+20,y-20), ((x+w)+200,y-20), (0 ,0 ,255), 1,)
                    cv2.putText(imagecon, ser, ((x+w)+20,y-25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    cv2.putText(imagecon, soc_1, ((x+w)+30,y+50+6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    cv2.ellipse(imagecon, ((x+w)+60,y+50), (50, 50), 0, 0, pow, (31, 81, 255), 3)
                else:
                    cv2.line(imagecon, ((x), y), ((x)-20,y-20), (0 ,0 ,255), 1,)
                    cv2.line(imagecon, ((x)-20,y-20), ((x)-200,y-20), (0 ,0 ,255), 1,)
                    cv2.putText(imagecon, ser, ((x)-200,y-25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    cv2.putText(imagecon, soc_1, ((x)-100,y+50+6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    cv2.ellipse(imagecon, ((x)-60,y+50), (50, 50), 0, 0, pow, (31, 81, 255), 3)
                # cv2.moveWindow(imagecon, 0,0)
                cv2.imshow('Last_Battery', imagecon)

            except:
                pass
            # text.strip("?")
            # print("x: " + str(x) + "y: " + str(y) + "w: " + str(w) +"h: " + str(h) )
    # elif objCor> 6:
    #     shape = "Circle"
        # x, y, w, h = cv2.boundingRect(approx)
        # cv2.rectangle(imagecon, (x, y), (x + w, y + h), (0 ,0 ,255), 2,)
        # cv2.line(imagecon, ((x+w), y), ((x+w)+20,y-20), (0 ,0 ,255), 1,)
        # cv2.line(imagecon, ((x+w)+20,y-20), ((x+w)+200,y-20), (0 ,0 ,255), 1,)
        # cv2.putText(imagecon, "Ser", ((x+w)+20,y-25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        # cv2.putText(imagecon, "SO%", ((x+w)+30,y+50+6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        # cv2.ellipse(imagecon, ((x+w)+60,y+50), (50, 50), 0, 0, 90, (31, 81, 255), 3)

    # else: shape ="Polygon"
    # cv2.putText(imagecon, shape, ((x+w)+5, y), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0,0,240),1)

def get_contours(source):
    grey = gry_img(source)
    g_blur = Gausian_Blur(grey,7,7,0)
    # lower, upper = track_values() ##Image controller
    imgresize1 = Canny(g_blur, 180,180)# low 0, uper 33
    # print(upper[0])
    contours, hierarchy = cv2.findContours(imgresize1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.imshow("Canny" , imgresize1)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area> 500:
            # print(area)

            cv2.drawContours(imagecon, cnt, -1, (255,0,0),2)
            shape_def(cnt)

def face_detect(source):
    imgresize = cv2.resize(source,(480, 320)) #Resize image
    # imagecon = imgresize.copy()
    gray = gry_img(imgresize)
    faces = faceCascade.detectMultiScale(gray, 1.2, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(imgresize,(x,y),(x+w, y + h), (200,234,0),2)

    cv2.imshow("Original", imgresize)
faceCascade = cv2.CascadeClassifier("HaarCascade_frontalface.xml")

def frame_rate():
    while(is_alive == 1):
        global f
        global sh
        global r
        # print("frame")
        sleep(1)
        r = 1
def qr_det():
    data, bbox, _ = detector.detectAndDecode(imgresize)
    global det_num
    if bbox is not None:
        # display the image with lines
        n_lines = len(bbox)
        # for i in range(len(bbox[0])):
        #     # draw all lines
        #     print('found')
        #     print(bbox)
        #     print(bbox[i][0])
        #     print(bbox[i][1])
        #     print(bbox[i+1][0])
        #     print(bbox[i+1][1])
        #     # print(bbox[0][0])
        #     # point1 = tuple(bbox[i][0])
        #     # point2 = tuple(bbox[(i+1) % n_lines][0])
        #
        #     # cv2.line(img, (int(bbox[0][0]), int(bbox[0][0])+5), (int(bbox[0][0])+5, int(bbox[0][0])+5), color=(255, 0, 0), thickness=2)
        #     # cv2.line(img, (bbox[0][i][0], bbox[0][i][1]), (bbox[0][i+1][0], bbox[0][i+1][1]), color=(255, 0, 0), thickness=2)
        #     # cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)

        cv2.line(imagecon, (int(bbox[0][0][0]), int(bbox[0][0][1])), (int(bbox[0][1][0]), int(bbox[0][1][1])), color=(255, 0, 0), thickness=2)
        cv2.line(imagecon, (int(bbox[0][1][0]), int(bbox[0][1][1])), (int(bbox[0][2][0]), int(bbox[0][2][1])), color=(255, 0, 0), thickness=2)
        cv2.line(imagecon, (int(bbox[0][2][0]), int(bbox[0][2][1])), (int(bbox[0][3][0]), int(bbox[0][3][1])), color=(255, 0, 0), thickness=2)
        cv2.line(imagecon, (int(bbox[0][3][0]), int(bbox[0][3][1])), (int(bbox[0][0][0]), int(bbox[0][0][1])), color=(255, 0, 0), thickness=2)
        # cv2.line(img, (int(15.2), int(25.4)), (int(45.6), int(65.7)), color=(255, 0, 0), thickness=2)
        x= int(bbox[0][0][0])
        y = int(bbox[0][0][1])
        w = int(bbox[0][1][0]) - int(bbox[0][0][0])
        h = int(bbox[0][1][1]) - int(bbox[0][0][1])
        if data:
            print("[+] QR Code detected, data:", data)
            try:
                num = int(data)
                print("Serial: "+ str(num))
                # cv2.putText(imagecon, str(num), ((x+w)+5, y), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0,0,240),1)
                ser, soc = lg_r.info_read_vis(num)
                print("SOC: "+ str(soc))
                ser  = "Serial: " + str(ser)
                pers=int(soc)
                soc_1  = str(soc) +"%"
                # cv2.putText(imagecon, ser, ((x+w)+5, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)
                # cv2.putText(imagecon, soc, ((x+w)+5, y+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)
                pow = pers*3.6
                print(pow)
                det_num = det_num + 1

                if(det_num%2 == 1):
                    cv2.line(imagecon, ((x+w), y), ((x+w)+20,y-20), (0 ,0 ,255), 1,)
                    cv2.line(imagecon, ((x+w)+20,y-20), ((x+w)+200,y-20), (0 ,0 ,255), 1,)
                    cv2.putText(imagecon, ser, ((x+w)+20,y-25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    cv2.putText(imagecon, soc_1, ((x+w)+30,y+50+6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    cv2.ellipse(imagecon, ((x+w)+60,y+50), (50, 50), 0, 0, pow, (31, 81, 255), 3)
                else:
                    cv2.line(imagecon, ((x), y), ((x)-20,y-20), (0 ,0 ,255), 1,)
                    cv2.line(imagecon, ((x)-20,y-20), ((x)-200,y-20), (0 ,0 ,255), 1,)
                    cv2.putText(imagecon, ser, ((x)-200,y-25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    cv2.putText(imagecon, soc_1, ((x)-100,y+50+6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    cv2.ellipse(imagecon, ((x)-60,y+50), (50, 50), 0, 0, pow, (31, 81, 255), 3)
            except ValueError:
                # cv2.putText(imagecon, ser, ((x+w)+5, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)
                # cv2.putText(imagecon, soc, ((x+w)+5, y+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)
                det_num = det_num + 1

                if(det_num%2 == 1):
                    cv2.line(imagecon, ((x+w), y), ((x+w)+20,y-20), (0 ,0 ,255), 1,)
                    cv2.line(imagecon, ((x+w)+20,y-20), ((x+w)+200,y-20), (0 ,0 ,255), 1,)
                    cv2.putText(imagecon, data, ((x+w)+20,y-25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    # cv2.putText(imagecon, soc_1, ((x+w)+30,y+50+6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    # cv2.ellipse(imagecon, ((x+w)+60,y+50), (50, 50), 0, 0, pow, (31, 81, 255), 3)
                else:
                    cv2.line(imagecon, ((x), y), ((x)-20,y-20), (0 ,0 ,255), 1,)
                    cv2.line(imagecon, ((x)-20,y-20), ((x)-200,y-20), (0 ,0 ,255), 1,)
                    cv2.putText(imagecon, data, ((x)-200,y-25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    # cv2.putText(imagecon, soc_1, ((x)-100,y+50+6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
                    # cv2.ellipse(imagecon, ((x)-60,y+50), (50, 50), 0, 0, pow, (31, 81, 255), 3)


sh = 0
r=0
is_alive = 1
real_rate = 0

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(0)
    # cap.set(3,600) # 3 is width setting id
    # cap.set(4,400) # 4 is height setting id
    cap.set(10, 200) # 10 is bightness setting id
    # kernel = np.ones((5,5),np.uint8) #for dilation matrix
    f = 0
    # print(f)
    # sh = frame_rate(f)
    threading.Thread(target=frame_rate).start()
    detector = cv2.QRCodeDetector()
    while True:
        f=f+1
        success, img = cap.read()
        # imgresize = cv2.resize(img,(640, 480)) #Resize image
        imgresize = img #Resize image
        # imgresize = cv2.resize(img,(1920, 1080)) #Resize image
        imagecon = imgresize.copy()

        # grey = gry_img(imgresize)
        # g_blur = Gausian_Blur(grey,7,7,0)
        # lower, upper = track_values()
        # imgresize1 = Canny(g_blur, lower[0], upper[0])


        get_contours(imgresize) # Tesseract OCR


        # qr_det() # Qr code reader native

        # imgHSV = cv2.cvtColor(imgresize, cv2.COLOR_BGR2HSV)
        # lower, upper = track_values() # Inrange values from trackbar
        # print(imgresize.shape)
        # gry_img(imgresize) # Grayscale image function
        # Gausian_Blur(imgresize) # GausianBlur image function

        # mask = cv2.inRange(img,lower,upper)
        # imgresult = cv2.bitwise_and(imgresize, imgresize, mask = mask)
        # imgcnny = cv2.Canny(img, huemin, huemax)
        # imgdialation = cv2.dilate(imgcnny, kernel, iterations = 1) # dilates the image after canny affect to make lines bigger
        # lim = np.vstack(img, img)
        # imgresize2 = cv2.resize(gry,(640, 360)) #Resize image
        # imgstk = np.vstack((imgresize, mask))
        # cv2.imshow("HSV", imgHSV)
        # cv2.imshow("Results",imgresult)
        # cv2.imshow("Mask", mask)
        # print(hue)
        # cv2.imshow("Original", imgresize)
        if(r==1):
            # print('alive')
            real_rate = f
            r = 0
            f = 0
        # cv2.putText(imagecon, str(f), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        cv2.putText(imagecon, str(real_rate), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        cv2.imshow("cont", imagecon)
        det_num = 0
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            # threading.Thread(target=frame_rate).join()
            is_alive = 0
            break
