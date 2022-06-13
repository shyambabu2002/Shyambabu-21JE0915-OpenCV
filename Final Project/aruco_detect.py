#identifying Aruco
import cv2
##image = cv2.imread(r"C:\Users\shyam\Documents\OPEN cv learning\open cv problem\XD.jpg")
##image2 = cv2.imread(r"C:\Users\shyam\Documents\OPEN cv learning\open cv problem\Ha.jpg")
##image3 = cv2.imread(r"C:\Users\shyam\Documents\OPEN cv learning\open cv problem\HaHa.jpg")
##image4 = cv2.imread(r"C:\Users\shyam\Documents\OPEN cv learning\open cv problem\LMAO.jpg")
##Dict = {1:image,2:image2,3:image3,4:image4}
def aruco_sorter(Dict):
    

    ARUCO_DICT = {
            "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
            "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
            "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
            "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
            "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
            "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
            "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
            "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
            "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
            "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
            "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
            "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
            "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
            "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
            "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
            "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
            "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
            "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
            "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
            "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
            "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
    }
    Sorted_Dict = {}
    num = 0
    for j in Dict:
        for i in ARUCO_DICT:
            ids = None
            #print(i)
            arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[i])
            arucoParams = cv2.aruco.DetectorParameters_create()
            (corners, ids, rejected) = cv2.aruco.detectMarkers(Dict[j], arucoDict,parameters=arucoParams)
            if ids :
                Sorted_Dict[ids[0][0]] = Dict[j] 
                print(ids[0][0])
                num+=1
                break
                
    #print(Sorted_Dict.keys())
    return Sorted_Dict

