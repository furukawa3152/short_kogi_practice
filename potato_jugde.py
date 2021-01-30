import cv2

import numpy as np
import matplotlib as plt
list = []
for i in range(8352,8563):
    # image = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potechi{}.jpg".format(i))
    image = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potato-chips\kyusyu-shoyu\IMG_{}.jpg".format(i))
    template = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potateboysample.jpg")  # 横長切り取り
    # template.resize(50*100)
    # template2 = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potato_boy2.jpg")  # 縦長切り取り
    # template3 = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potate_boy3.jpg")
    # template4 = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potato_boy4.jpg")

    result1 = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)
    # result2 = cv2.matchTemplate(image, template2, cv2.TM_CCOEFF)
    # min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
    # result3 = cv2.matchTemplate(image, template3, cv2.TM_CCOEFF)
    # min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
    # result4 = cv2.matchTemplate(image, template4, cv2.TM_CCOEFF)
    # min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4)
    max_val = max([max_val1])
    if max_val >30000000:
        list.append((i,max_val))
    else:
        list.append((i, max_val))
# print(cv2.minMaxLoc(result))
#     print(max_val)
#     _,w,h = template.shape[::-1]
#
#     top_left = max_loc1
#     btm_right = (top_left[0]+w,top_left[1]+h)
#     cv2.rectangle(image,top_left,btm_right,255,2)
#     cv2.imshow("test",image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
print(list.count("True"))
print(list)

#[25031566.0, 43212640.0, 48577008.0, 28657642.0, 27756220.0, 25754406.0, 30121652.0, 33067934.0]





