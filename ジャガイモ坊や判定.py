import cv2
#合致面積から数字を出すため、複数画像からは不可能（同じサイズならありか？）
for i in range(9236,9470):
    # image = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potechi{}.jpg".format(i))
    image = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potato-chips\consomme-punch\IMG_{}.jpg".format(i))
    template = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potato_boy1.jpg")#横長切り取り
    # template2 = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potato_boy2.jpg")#縦長切り取り
    # template3 = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potate_boy3.jpg")
    # template4 = cv2.imread(r"C:\Users\user\PycharmProjects\short_kogi_practice\potato_boy4.jpg")

    result1 = cv2.matchTemplate(image,template,cv2.TM_CCOEFF)
    min_val1,max_val1,min_loc1,max_loc1 = cv2.minMaxLoc(result1)
    # result2 = cv2.matchTemplate(image,template2,cv2.TM_CCOEFF)
    # min_val2,max_val2,min_loc2,max_loc2 = cv2.minMaxLoc(result2)
    # result3 = cv2.matchTemplate(image,template3,cv2.TM_CCOEFF)
    # min_val3,max_val3,min_loc3,max_loc3 = cv2.minMaxLoc(result3)
    # result4 = cv2.matchTemplate(image,template4,cv2.TM_CCOEFF)
    # min_val4,max_val4,min_loc4,max_loc4 = cv2.minMaxLoc(result4)
    max_val=max([max_val1])
    if max_val >29000000:
        cv2.imwrite(r"C:\Users\user\PycharmProjects\short_kogi_practice\potate_test\{}.jpg".format(max_val),image)


#コンソメパンチ＝potatoboy1:30000000
#九州醤油＝potateboysample:27000000
#のりしお＝potatoboy1:30000000
#のりしおパンチ＝potatoboy1:30000000
#幸せバタ-＝potatoboy1:30000000
#醤油マヨ＝logo1:100000000
#うすしお＝potatoboy1:30000000
