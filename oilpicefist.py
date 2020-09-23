# เก็บค่าน้ำมัน
gas = {"Gasoline 95": 29.16,"Gasoline 91":25.30,"Gasohol 91":21.68,"Gasohol E20":20.2,"Gasohol 95":21.2,"Diesel":21.1}
# แสดงราคาน้ำมัน
for key in range(len(gas.keys())):
    k = list(gas.keys())[key]
    print(str(key+1)+".",k, ":", gas[k], "BAHT")
# เก็บประเภทน้ำมันเป็นตัวเลขและราคา
oil = int(input("ประเภทของน้ำมัน"))
print("เลือกลิตรหรือเงิน")
print("1.เงินเป็นลิตร")
print("2.ลิตรเป็นเงิน")
select = int(input())
price =int(input("เติม"))
# คำนวณเป็นลิตร
fee = 0
if (select == 1):
    fee = (price / gas[list(gas.keys())[oil-1]])
    print("จำนวนลิตร %.2f ลิตร" %(fee))
elif (select == 2):
    fee = (price * gas[list(gas.keys())[oil-1]])
    print("จำนวนเงิน %.2f บาท" %(fee))
