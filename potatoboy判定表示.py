import cv2
from PIL import Image
import numpy as np
import matplotlib as plt
list = []
for i in range(1,10):
    image = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potechi{}.jpg".format(i))
    # image = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potato-chips\kyusyu-shoyu\IMG_{}.jpg".format(i))
    template = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\shoyu-mayologo.jpg")
    # template=template.resize(50*100)


    result1 = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)

    max_val = max([max_val1])
    if max_val >30000000:
        list.append((i,max_val))
    else:
        list.append((i, max_val))
# print(cv2.minMaxLoc(result1))
    print(max_val1)
    _,w,h = template.shape[::-1]

    top_left = max_loc1
    btm_right = (top_left[0]+w,top_left[1]+h)
    cv2.rectangle(image,top_left,btm_right,255,2)
    cv2.imshow("test",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
print(list.count("True"))
print(list)

#[(1, 24011842.0), (2, 22542268.0), (3, 21713228.0), (4, 22008724.0), (5, 21774488.0), (6, 21949382.0), (7, 22397214.0)]