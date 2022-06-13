# Shyambabu-21JE0915-OpenCV
Identifying Square coloured boxes with and overlaying respective Aruco makers 

from the problem statement what i understand is we have to do the following::
  - Identify the square boxes with their colours
  - Paste different aruco markers according to their respective ids
  - present the output in a good way

To solve this problem following was my stratigies ::
  - Making a Aruco Sorter which can return a Dictionary
  - Making a function that can split boxes of different colors from the image
  - storing the seperated images with appropiate names
  - applying the Aruco ::
      - Finding the contours on seperated images # line1
      - creating Boundung boxes around shapes(detected) and Aruco
      - identifying the Square shapes
      - applying homography on Aruco with final size as original image size(i.e seperated image -- line 1)
          syntax -- matrix = cv2.findHomography(pts2,pts1)[0] // pts2 = aruco's bounding box, pts1 = identified square's coordinate
                    image_aruco = cv2.warpPerspective(modified_aruco,matrix,(image.shape[1],image.shape[0]))
      - applying bitwise_or on Aruco and Image_seperated(ref. line 1)
      - Showing and Storing final image
 AND THAT'S ALL FROM MY SIDE
 THANK YOU SO MUCH SENIORS FOR TEACHING ME SUCH A WONDERFUL TOPIC :)
