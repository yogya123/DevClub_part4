import cv2
import numpy as np 
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
def rescaleFrame(frame):
    width=500
    height=500
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)


a1= cv2.imread("a1.jpg",1)
a3= cv2.imread("a3.jpg",1)
a2= cv2.imread("a2.jpg",1)
a4= cv2.imread("a4.jpg",1)
a5= cv2.imread("a5.jpg",1)
a6= cv2.imread("a6.jpg",1)
resize1=rescaleFrame(a1)
resize2=rescaleFrame(a2)
resize3=rescaleFrame(a3)
resize4=rescaleFrame(a4)
resize5=rescaleFrame(a5)
resize6=rescaleFrame(a6)


ans = np.zeros((1000,1500,3),dtype= np.uint8)

for i in range(1000):
    for j in range(1500):
        if(i<500 and j<500):
            ans[i][j] = resize1[i][j]
        elif(i<500 and j>=500 and j<1000):
            ans[i][j] = resize2[i][j-500]
        elif(i<500 and j>=1000 and j<1500):
            ans[i][j] = resize3[i][j-1000]
        elif(i>=500 and j<500):
            ans[i][j] = resize4[i-500][j]
        elif(i>=500 and j>=500 and j<1000):
            ans[i][j] = resize5[i-500][j-500]        
        elif(i>=500 and j>=1000 and j<1500):
            ans[i][j] = resize6[i-500][j-1000]
cv2.putText(ans,'Year Book 2020', (300,520), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5.0, (0,0,0), thickness=10)

cv2.imshow("image",ans)
cv2.waitKey(0)