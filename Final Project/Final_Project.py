#basic aruco
import cv2
import numpy as np
from aruco_detect import aruco_sorter #imorting User defined function
image = cv2.imread(r"CVtask.jpg")
blank = np.zeros(image.shape,np.uint8)


image1 = cv2.imread(r"XD.jpg")
image2 = cv2.imread(r"Ha.jpg")
image3 = cv2.imread(r"HaHa.jpg")
image4 = cv2.imread(r"LMAO.jpg")
Dict = {1:image1,2:image2,3:image3,4:image4} #Storing Arucos in Dictionary
Dict = aruco_sorter(Dict) #Sorting Arucos
#print(Dict.keys())


size = image.shape # 1 = height,0 = width
image = cv2.resize(image,(512,512))
def bounding_boxes(img,tl,th):
    if len(img) == 3:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    #cv2.imshow("gray",gray)
    #thresh = cv2.threshold(gray,228,255,cv2.THRESH_BINARY)[1]
    canny = cv2.Canny(gray,tl,th)
    contour = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[0]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11,11))
    canny = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
    contour = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[0]
    #cv2.imshow("canny",canny)
    
    return contour



def find_approx_contour(contour):
    approx_list = list()
    area_list = list()
    for cnt in contour:
        peri = cv2.arcLength(cnt,True)
        area_list.append(cv2.contourArea(cnt))
        approx = cv2.approxPolyDP(cnt,peri*0.01,True)
        approx_list.append(approx)
        
    
    return approx_list,area_list

def aruco_rect(approx_list,area_list):
    max_area = 0
    index = 0
    for i in range(0,len(area_list)):
        if area_list[i] > max_area:
            max_area = area_list[i]
            index = i
    return approx_list[i]

#Function for Square finding
def is_square(list_coordinate):
##    print(list_coordinate[0])
##    print(list_coordinate[1])
##    print(list_coordinate[2])
##    print(list_coordinate[3])
    x1,y1 = list_coordinate[1][0][0],list_coordinate[1][0][1]
    x2,y2 = list_coordinate[2][0][0],list_coordinate[2][0][1]
    x3,y3 = list_coordinate[3][0][0],list_coordinate[3][0][1]
    x4,y4 = list_coordinate[0][0][0],list_coordinate[0][0][1]

    a1 = ((x1-x2)**2+(y1-y2)**2)**0.5
    a2 = ((x2-x3)**2+(y2-y3)**2)**0.5
    a3 = ((x3-x4)**2+(y3-y4)**2)**0.5
    a4 = ((x4-x1)**2+(y4-y1)**2)**0.5
    #print(a1,a2,a3,a4,"--")
    if abs(a1-a3) < 25 and abs(a2-a4) < 25:
        return True
    else :
        return False

    
def draw_aruco(image_aruco,image,original_image):
    copy_image_aruco = image_aruco.copy()
    blank = np.zeros(image_aruco.shape,np.uint8)
    lst = bounding_boxes(image_aruco,228,255)
    approx_list,area_list = find_approx_contour(lst)
    big_box = aruco_rect(approx_list,area_list)
    ##### rotating the image ##########
    pts1 = np.array(big_box)
    x,y,w,h = cv2.boundingRect(big_box)

    pts2 = np.array([[w,h],[0,h],[0,0],[w,0]])
    matrix = cv2.findHomography(pts1,pts2)[0]
    modified_aruco = cv2.warpPerspective(image_aruco,matrix,(w,h))

    list_all_squares = bounding_boxes(image,250,255)
    app_list_all_squares,area_list = find_approx_contour(list_all_squares)
    #is_square(app_list_all_squares)
    for index in range(0,len(area_list)):       
        if area_list[index] > 1000 and index%2 == 1:
            #print(is_square(app_list_all_squares[index]),": Truth Value")
            if len(app_list_all_squares[index]) == 4 and is_square(app_list_all_squares[index]):
                
                
                pts1 = np.array(app_list_all_squares[index])
                matrix = cv2.findHomography(pts2,pts1)[0]
                copy_image_aruco = cv2.warpPerspective(modified_aruco,matrix,(image.shape[1],image.shape[0]))
                cv2.imshow("image_aruco",copy_image_aruco)
                cv2.imshow("aruco",cv2.bitwise_or(copy_image_aruco,original_image))
                original_image = cv2.bitwise_or(copy_image_aruco,original_image)
                cv2.waitKey(0)
                #cv2.destroyAllWindows()
               
    return original_image
def segregate_color(img,hmi,hma,smi,sma,vmi,vma):
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([hmi,smi,vmi])
    upper = np.array([hma,sma,vma])
    mask = cv2.inRange(img_hsv,lower,upper)
    bitand = cv2.bitwise_and(img,img,mask=mask)
    return mask

image_orange = segregate_color(image,3,17,210,255,48,255)
image_green = segregate_color(image,36,56,33,255,0,255)
image_black = segregate_color(image,0,179,0,255,0,55)
image_peachpink = segregate_color(image,10,34,0,33,51,241)

image = draw_aruco(Dict[2],image_orange,image)
image = draw_aruco(Dict[1],image_green,image)
image = draw_aruco(Dict[3],image_black,image)
image = draw_aruco(Dict[4],image_peachpink,image)

cv2.imshow("blank",image)
cv2.imwrite("modified.jpg",image)

cv2.imwrite("1.jpg",Dict[1])
cv2.imwrite("2.jpg",Dict[2])
cv2.imwrite("3.jpg",Dict[3])
cv2.imwrite("4.jpg",Dict[4])
cv2.waitKey(0)
cv2.destroyAllWindows()

