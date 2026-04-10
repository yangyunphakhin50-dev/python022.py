print("สคริปสุ่มเลข 1 ถึง 100")
print("")

import random

num = int(input("เลข(1 - 100) : "))
result = random.randint(1, 100)

while True:
    if num == result:
        print("ถูกต้อง")
        break
    elif num <= result:
        print("น้อยไป")
        num = int(input("ทายอีกครั้ง: "))
    elif num >= result:
        print("มากไป")
        num = int(input("ทายอีกครั้ง"))
    else:
        print("error")
        int(input("try again : "))
