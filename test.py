import cv2  
def nothing(x):
   pass     
img = cv2.imread('pill2.png')
img2 = cv2.imread('pill2.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)  
      
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
      
cv2.imshow("img", img)  
cv2.imshow("img2",img)
cv2.createTrackbar('min_value','img',0,255,nothing)
cv2.createTrackbar('max_value','img',0,255,nothing)
while(1):
    cv2.imshow("img", img)  
    img[:]=255
    min_value = cv2.getTrackbarPos('min_value', 'img')
    max_value = cv2.getTrackbarPos('max_value', 'img')
    ret, binary = cv2.threshold(gray,min_value,max_value,cv2.THRESH_BINARY)   
    contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,-1,(0,0,255),3) 
    k = cv2.waitKey(37)
    if k == 27:
        break
cv2.destroyAllWindows()
