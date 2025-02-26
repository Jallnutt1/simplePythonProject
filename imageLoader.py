import sys
import cv2
print ('imported sys & cv2')

img = cv2.imread("emilyB.jpeg", cv2.IMREAD_ANYCOLOR)

cv2.imshow("Emily", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


from matplotlib import pyplot as plt
from matplotlib import image as mpimg
print("imported Matplotlib")


plt.title("Emily Again")
plt.xlabel("X Pixel Scaling")
plt.ylabel("Y Pixel Scaling")
print("created window")

image = mpimg.imread("emily2.jpg")
plt.imshow(image)
plt.show()
print("image should show")

print("Script Complete!") 

