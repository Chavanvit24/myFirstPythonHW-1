from suds.client import Client
gas = {"Gasoline 95": 29.16,"Gasoline 91":25.30,"Gasohol 91":21.68,"Gasohol E20":20.2,"Gasohol 95":21.2,"Diesel":21.1}
#ดึงเว็บเข้าloopน้ำมัน
client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
OilPrice = client.service.CurrentOilPrice(Language='thai')
import xmltodict,json
OilPrice = xmltodict.parse (OilPrice)
price= eval(json.dumps(OilPrice))
for i in price["PTTOR_DS"]["FUEL"]:
    if("gas" in i):
        oil_price[i["PRODUCT"]] = float(i["PRICE"])


print(OilPrice)
print(type(OilPrice))
print("#"*120)
print("#" + (" " * 118) + "#")
print("#" + (" " * 118) + "#")
print("#" + (" " * 118) + "#")
print("#" + (" " * 118) + "#")
print("#" + (" " * 118) + "#")
print("#" + (" " * 45) + "HELLO THIS IS GAS STATION" + (" " * 48) + "#")
print("#" + (" " * 118) + "#")
print("#" + (" " * 118) + "#")
print("#" + (" " * 118) + "#")
print("#" + (" " * 118) + "#")
print("#" + (" " * 118) + "#")
print("#" + (" " * 118) + "#")
print("#"*120)

print(OilPrice)
print(type(OilPrice))
while True:
    print("#"*120)
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + " list  " + (" " * 66) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + " 1.Gasoline 95 = " + 
                str(gas["Gasoline 95"])+"  " + (" " * 49) + "#")
    print("#" + (" " * 45) + " 2.Gasoline 91 = " + 
                str(gas["Gasoline 91"])+"  " + (" " * 50) + "#")
    print("#" + (" " * 45) + " 3.Gasohol 91  =" + 
                str(gas["Gasohol 91"])+"   " + (" " * 49) + "#")
    print("#" + (" " * 45) + " 4.Gasohol E20 =" + 
                str(gas["Gasohol E20"])+"  " + (" " * 51) + "#")
    print("#" + (" " * 45) + " 5.Gasohol 95  =" + 
                str(gas["Gasohol 95"])+"    " + (" " * 49) + "#")
    print("#" + (" " * 45) + "  6.Diesel      =" + 
                str(gas["Diesel"])+"       " + (" " * 45) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#"*120)

    oil = int(input("ประเภทของน้ำมัน"))

    print("#"*120)
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + "  เลือกเงินเป็นลิตร   " + (" " * 55) + "#")
    print("#" + (" " * 45) + "  1.เงินเป็นลิตร       " + (" " * 53) + "#") 
    print("#" + (" " * 45) + "   2.ลิตรเป็นเงิน      " + (" " * 53) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#"*120)

    select = int(input("1.เงินเป็นลิตรหรือ 2.ลิตรเป็นเงิน"))
    price =int(input("เติม"))

    print("#"*120)
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + "  THANKYOU  " + (" " * 61) + "#")
    print("#" + (" " * 45) + "  THANKYOU  " + (" " * 61) + "#") 
    print("#" + (" " * 45) + "  THANKYOU  " + (" " * 61) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#"*120)

    fee = 0
    if (select == 1):
        fee = (price / gas[list(gas.keys())[oil-1]])
        print("จำนวนลิตร %.2f ลิตร" %(fee))
    elif (select == 2):
        fee = (price * gas[list(gas.keys())[oil-1]])
        print("จำนวนเงิน %.2f บาท" %(fee))
        
        print("1 - exit,  2 - back the menu. ")
        f = "1"
        # กด 1 จะออก
        print("1 - exit,  2 - back the menu. ")
        s = "2"
        # กด 2กลับเข้าเมนู
        e = input()
        if(e != s):
            break
