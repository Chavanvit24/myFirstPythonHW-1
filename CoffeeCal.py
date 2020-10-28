# กำหนดค่า วัตถุดิบในเครื่องชงกาแฟ
W = 400
M = 540
B = 120
C = 9
m = 550

# วนลูปเมื่อเป็นไปตามเงื่อนไข Restart / Exit
y = 1
while True:
    if y == 1:

        # โชว์รายละเอียดวัตถุดิบที่มีอยู่ในเครื่องชงกาแฟ
    print("#"*120)
    print("#" + (" " * 45) + "The Coffee machine has" + (" " * 48) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) +   
                 str(W["ml of water"] + (" " * 48) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + 
                 str(M["ml of milk"] + (" " * 48) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + 
                 str(B["g of coffee beans"] + (" " * 48) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + 
                 str(C["of disposable cups"] + (" " * 48) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 45) + 
                  str(m["of money"] + (" " * 48) + "#")
    print("#" + (" " * 118) + "#")
    print("#" + (" " * 118) + "#")
    print("#"*120)

        # เลือกเมนูการใช้งาน ซื้อ/ เติม / รับเงิน
        p = input("choose one option - buy / fill/ take >")

# ทำงานตามเงื่อนไขของBuy
        if "buy" in p or "Buy" in p or "BUY" in p:

            # แสดงประเภทของกาแฟ
            print("#"*120)
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + "Choose Kind Of Coffee  " + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + "( 1 ) Espresso" + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + "( 2 ) Latte" + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + "( 3 ) Cappuccino" + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#"*120)
# กรอกประเภทของกาแฟที่ต้องการ
            c = str(input("tell me what number do you want ? >"))

# เงื่อนไข Buy ตามประเภทของกาแฟ โดยแสดง ประเภท / เงินที่ต้องจ่าย และ วัตถุดิบที่เหลือ
            if 'espresso' in c or '1' in c:
                print("#"*120)
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + "Espresso" + (" " * 48) + "#")
                print("#" + (" " * 45) + "*you must pay 4 $" + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")    
                print("#" + (" " * 45) + "**The Coffee machine has:" + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")   
                print("#" + (" " * 45) + 
                      int(W) - 250) + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + 
                      str(M)["ml of milk"]  + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")    
                print("#" + (" " * 45) + 
                      int(B) - 16)["g of coffee beans"] + (" " * 48) + "#")
                print("#" + (" " * 118) + "#") 
                print("#" + (" " * 118) + "#") 
                print("#" + (" " * 45) + 
                      int(C) - 1)["of disposable cups"] + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + 
                      int(m) + 4)["$ of money"] + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#"*120)
            elif 'latte' in c or '2' in c:
                print("#"*120)
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + "Latte" + (" " * 48) + "#")
                print("#" + (" " * 45) + "you must pay 7 $" + (" " * 48) + "#")  
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + "The Coffee machine has" + (" " * 48) + "#")  
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + 
                      int(W) - 350)["ml of water" ] + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")   
                print("#" + (" " * 45) + 
                      int(M) - 75)["ml of milk" ] + (" " * 48) + "#")  
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")  
                print("#" + (" " * 45) + 
                      int(B) - 20)["g of coffee beans" ] + (" " * 48) + "#")              
                print("#" + (" " * 118) + "#")  
                print("#" + (" " * 118) + "#")     
                print("#" + (" " * 45) + 
                      int(C) - 1)["of disposable cups" ] + (" " * 48) + "#") 
                print("#" + (" " * 118) + "#")  
                print("#" + (" " * 118) + "#")  
                print("#" + (" " * 45) + 
                      int(m) + 7)["$ of money" ] + (" " * 48) + "#") 
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#"*120)
        
            elif 'cappuccino' in c or '3' in c:
                print("#"*120)
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + "Cappuccino" + (" " * 48) + "#")
                print("#" + (" " * 45) + "you must pay 6 $" + (" " * 48) + "#")    
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + "The Coffee machine has" + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + 
                      int(W) - 200)["ml of water"] + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + 
                      int(W) - 100)["ml of milk"] + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + 
                      int(B) - 12)["g of coffee beans"] + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + 
                      int(C) - 1])["of disposable cups"] + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 45) + 
                      int(C) +6])["$ of money" ] + (" " * 48) + "#")
                print("#" + (" " * 118) + "#")
                print("#" + (" " * 118) + "#")
                print("#"*120)
            else:
                print("Error")

# เงื่อนไขการเติมวัตถุดิบ - fill
        elif "fill" in p or "Fill" in p or "FILL" in p:

            # ระบุบปริมาณวัตถุดิบต่างๆที่ต้องการเติม
            wf = int(input("write how many ml of water do you want to add:\n>"))
            Mf = int(input("write how many ml of milk do you want to add:\n>"))
            Bf = int(
                input("write how many grams of coffee beans do you want to add:\n>"))
            mf = int(
                input("write how many disposable cups do you want to add:\n>"))

# แสดงวัตถุดิบหลังจากที่เติมแล้ว
            print("#"*120)
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + "**Result" + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + "The Coffee machine has" + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + 
                      int(W) +(Wf)])["ml of water"] + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + 
                      int(M) +(Mf)])["ml of milk"] + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + 
                      int(B) +(Bf)])["g of coffee beans"] + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + 
                      int(C) +(mf)])["of disposable cups"] + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + 
                      int(m)])["$ of money"] + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#"*120)
               

# เงื่อนไขขอรับเงิน - take >> จำนวนเงินที่ได้รับ และ วัตถุดิบที่เหลือ
        elif "take" in p or "Take" in p or "TAKE" in p:
            print("#"*120)
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + " < I gave you",
                         (m)," $ > "+ (" " * 48) + "#")
            print("#" + (" " * 118) + "#")   
            print("#" + (" " * 45) + "**Result" + (" " * 48) + "#")
            print("#" + (" " * 45) + "The Coffee machine has" + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + 
                      int(W)])["ml of water"] + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + 
                      int(M)])["ml of milk"] + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + 
                      int(B)])["g of coffee beans"] + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + 
                      int(C)])["of disposable cups"] + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 118) + "#")
            print("#" + (" " * 45) + 
                      int(m)-m])["$ of money"] + (" " * 48) + "#")
            print("#" + (" " * 118) + "#")
            print("#"*120)
        else:
            print("Error")

# ป้อนคำสั่ง restart / exit
        x = input("Exit/Restart : >")
        if "Exit" in x or "exit" in x or "x" in x or "X" in x:
            y = 0
        elif "Restart" in x or "restart" in x or "R" in x or "r" in x:
            y = 1
        else:
            print("Error")
    elif y == 0:
        break
