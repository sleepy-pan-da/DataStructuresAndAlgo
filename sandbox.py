from typing import List


name_1 : List[int] = [1, 2, 3]
print("id of name_1 = ", id(name_1))

name_1[0] = -1

#name_1 : List[int] = [1, 2, 3]
print("id of name_1 afer initialing with new value = ", id(name_1))