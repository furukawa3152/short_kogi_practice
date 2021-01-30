# import time
# for count in range(1,4):
#     time.sleep(1)
#     print(f"{count}秒経過")

# import time
# for count in range(1,31):
#     if count%3 == 0:
#         time.sleep(1)
#         print(f"python最高（{count}秒）")
#     else:
#         time.sleep(1)
#         print(f"{count}秒経過")

# import numpy as np
# test = np.array([0,1,2,3,4,5])
# test_2 =test.reshape(2, 3)
#
# print(test_2)
# print(np.linspace(0,3.14,10))

import numpy as np

# array_a = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
# array_a =np.arange(15)
# array_b = array_a.reshape(3,5)
# print(array_b)
# print(array_a.shape)#形状確認
# print(array_b.shape)
# a = np.arange(5)
# b = np.arange(3,8)
# print(np.add(a,b))

# mondai1 = np.arange(1, 11)
# mondai2 = (mondai1.reshape(2, 5))
# a = mondai2[0]
# b = mondai2[1]
# print(np.add(a, b))
# print(a-b)
# print(a*b)
# print(a/b)

mondai1= np.arange(1, 26).reshape(5,5)
print(mondai1)
print(mondai1[1:3,2:5])#１行目から２行目の2番目から4番目
