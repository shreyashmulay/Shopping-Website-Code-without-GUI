print("*******************************************************************************************************************************")
print("\tProgram is written by Shreyash Mulay  in 2021.\n\tNOTE: As this program doesn't contail database you have to register every time you run the code before you loging. ")
print("*******************************************************************************************************************************")
import sys # importing system module for exit.

#Creating Dictionary for Products.
Electronic=[{"id":1,"Name":"Air Conditioners","lga":"L.G.","voltas":"Voltas","tcl":"TCL","sac":"Smart A.C.","la1":"2.0 Ton  with 3 star inverter split A.C.","la2":"1.5 Ton  with 5 star inverter split A.C.","la3":"1.5 Ton  with 4 star inverter split A.C.","la4":"1.0 Ton  with 5 star inverter split A.C.","lc1":49700,"lc2":41490,"lc3":37490,"lc4":32000,"v1":"1.4 Ton  with 5 star inverter split A.C.","v2":"1.4 Ton  with 3 star Fixed speed split A.C.","v3":"1.4 Ton  with 5 star Fixed speed window  A.C.","v4":"1.4 Ton  with 3 star Fixed speed window A.C.","vc1":35000,"vc2":30000,"vc3":27000,"vc4":25000,"tc1":"2.0 Ton  with 3 star ultra inverter split A.C.","tc2":"1.5 Ton  with 3 star ultra inverter split A.C.","tc3":"1.0 Ton  with 3 star ultra inverter split A.C.","tcc1":37000,"tcc2":29000,"tcc3":26000,"sac1":"panasonic 2.0 Ton  with 5 star wifi twin cool inverter split A.C.","sac2":"panasonic 1.5 Ton  with 5 star wifi twin cool inverter split A.C.","sac3":"Hisense	1.5 Ton  with 5 star wifi twin cool inverter split A.C.","sac4":"Hisense 1.0 Ton  with 5 star wifi twin cool inverter split A.C.","sacc1":53000,"sacc2":40000,"sacc3":37000,"sacc4":37000},
            {"id":2,"Name":"Television","samsung":"Samsung","lgt":"L.G.","sony":"Sony","mi":"Mi","s1":"Samsung UA65TUE60AK 65 inch 4K (Ultra HD) Smart LED","s2":"Samsung UA55TUE60FK 55 inch 4K (Ultra HD) Smart LED","s3":"Samsung UA50TUE60AK 50 inch 4K (Ultra HD) Smart LED","s4":"Samsung UA32TE40FAK 32 inch HD Ready Smart LED","sc1":87990,"sc2":49990,"sc3":47990,"sc4":16790,"lt1":"LG 55UM7290PTD 55 inch LED 4K TV","lt2":"LG 50UM7290PTD 50 inch LED 4K TV","lt3":"LG 43UM7290PTF 43 inch LED 4K TV","lt4":"LG 32LM565BPTA 32 inch LED HD-Ready TV","lc1":49990,"lc2":44999,"lc3":34990,"lc4":16999,"so1":"Sony BRAVIA KD-55X7400H 55 inch 4K (Ultra HD) Smart LED","so2":"Sony BRAVIA KD-55X7002G 55 inch 4K (Ultra HD) Smart LED","so3":"Sony BRAVIA KD-43X7002G 43 inch 4K (Ultra HD) Smart LED","so4":"Sony KDL-43W6603 43 inch Full HD Smart LED","soc1":63999,"soc2":59990,"soc3":39999,"soc4":34990,"m1":"4A pro 108cm(43 inches) FHD android led with data saver black","m2":"4A 100cm(40 inches) FHD android led smart with data saver Black","m3":"4A pro 80cm(32 inches) hd android led with data saver black","m4":"4A Horozon edition 80cm(32 inches) hd android led Grey","mc1":24000,"mc2":20000,"mc3":15000,"mc4":15000},
            {"id":3,"Name":"Washing Machine","samsung":"Samsung","whirlpool":"Whirlpool","lgw":"L.G.","sw1":"Samsung 7.5 Kg Fully Automatic Top Load Washing Machine (WA75A4022FS)","sw2":"Samsung 7 Kg Fully Automatic Top Load Washing Machine (WA70A4002GS)","sw3":"Samsung 6.5 Kg Fully Automatic Top Load Washing Machine (WA65A4002VS)","swc1":18990,"swc2":16790,"swc3":14190,"ww1":"Whirlpool 6.2 Kg Fully Automatic Top Load Washing Machine (Whitemagic Royale 6212SD)","ww2":"Whirlpool 7.5 Kg Semi Automatic Top Load Washing Machine (ACE 7.5 SUPREME)","ww3":"Whirlpool 6.2 Kg Semi Automatic Top Load Washing Machine (Superb Atom 62I)","wwc1":12990,"wwc2":9990,"wwc3":8990,"lw1":"LG 6 Kg Fully Automatic Top Load Washing Machine (FHM1006ADW)","lw2":"LG 7.0 Kg Fully Automatic Top Load Washing Machine (T65SKSF4Z)","lw3":"LG 6.5 Kg Fully Automatic Top Load Washing Machine (T7585NDDLGA)","lc1":23990,"lc2":19490,"lc3":14990},
            {"id":4,"Name":"Cameras","n":"Nikon","c":"Canon","f":"FujiFilm","s":"Sony","n1":"Nikon Z5 Mirrorless Camera (Body Only)","n2":"Nikon Z50 Mirrorless Camera with 16-50 mm Lens","n3":"Nikon D5600 DSLR Camera (AF-P 18-55mm VR Lens)","n4":"Nikon D3500 DSLR Camera (AF-P 18-55mm Lens)","nc1":90034,"nc2":72999,"nc3":46999,"nc4":32500,"c1":"Canon EOS R6","c2":"Canon PowerShot SX60HS 16.1MP Digital Camera","c3":"Canon PowerShot SX620HS 20.2MP Digital Camera","c4":"Canon EOS Rebel T5 18MP DSLR Camera","cc1":215995,"cc2":50000,"cc3":15500,"cc4":14000,"f1":"Fujifilm XT3 24.3MP DSLR Camera","f2":"Fujifilm XT2 24.3MP DSLR Camera","f3":"Fujifilm X-T30 Digital Camera","f4":"Fujifilm XT20 20MP DSLR Camera","fc1":96000,"fc2":78000,"fc3":70000,"fc4":67000,"sc1":"Sony ILCE 3500JY 20.1MP DSLR Camera","sc2":"Sony ILCE 3500J 20.1MP DSLR Camera","sc3":"Sony CyberShot DSC W220B 12.1MP DSLR Camera","sc4":"Sony CyberShot DSC W690 16.1MP Digital Camera","scc1":33000,"scc2":27000,"scc3":24000,"scc4":11000},
            {"id":5,"Name":"Refrigerators","samsung":"Samsung","whirlpool":"Whirlpool","haier":"Haier","lgf":"L.G.","sr1":"Samsung RR22R373YR8 215 L 4 Star Direct Cool Single Door Refrigerator","sr2":"Samsung RR21T2G2W9R 198 L 5 Star Inverter Direct Cool Single Door Refrigerator","sr3":"Samsung RR20A1Z2YU8 192 L 3 Star Direct Cool Single","src1":18000,"src2":17000,"src3":15000,"wr1":"Whirlpool IF CNV 278 ELT 265 L 3 Star Frost Free Double Door Refrigerator","wr2":"Whirlpool WDE 205 ROY 4S 190 L 4 Star Direct Cool Single Door Refrigerator","wr3":"Whirlpool WDE 205 PRM 4S 190 L 4 Star Inverter Direct Cool Double Door Refrigerator","wrc1":22000,"wrc2":15000,"wrc3":14000,"hr1":"Haier HRD-2204BS-R 220 L 4 Star Direct Cool Single Door Refrigerator","hr2":"Haier HRD-1955CSS-E 195 L 5 Star Direct Cool Single Door Refrigerator","hr3":"Haier HRD-1953CKS-E 195 L 3 Star Direct Cool Single Door Refrigerator","hrc1":16000,"hrc2":15000,"hrc3":14000,"lr1":"LG GL-I292RPZL 260 L 4 Star Inverter Frost Free Double Door Refrigerator","lr2":"LG GL-B201ASPY 190 L 5 Star Direct Cool Single Door Refrigerator","lr3":"LG GL-D201ABPY 190 L 4 Star Direct Cool Single Door Refrigerator","lrc1":24000,"lrc2":17000,"lrc3":16000}]
Sports=[{"id":1,"Name":"Football","fb1":"Gear Pro-tec Gear Pro-tec Razor Football Shoulder Pads","fb2":"Nivia Dominator Football Shin Guard","fb3":"Adidas  Football Size '5'","fb4":"Pepup Training Marker Cones 6 inch Set Of 6","fbc1":25558,"fbc2":3480,"fbc3":1290,"fbc4":229},
        {"id":2,"Name":"Cricket","ck1":"SG English Willow Complete Premium Cricket Kit for Professionals","ck2":"Leather Ball set of 3","ck3":"Ceat Ct S6 Popular Bat With Ball Grip Head And Wrist Band Cricket Kit","ck4":"Se Sports Batting Right Hand Batting Gloves","ck5":"Diamond Tournament Stumps","ckc1":8990,"ckc2":699,"ckc3":599,"ckc4":289,"ckc5":220},
        {"id":3,"Name":"Camping & Hiking","ch1":"Camping tent with poles for 4 Person with 1 Bedroom","ch2":"professional hiking urvival kit of 5 Pieces","ch3":"Sahyadri Sleeping Bags","ch4":"Gear Compass with Hanging Ring Gift","chc1":7999,"chc2":3231,"chc3":1199,"chc4":384},
        {"id":4,"Name":"Swimming","sw1":"Swimming Gear Set","sw2":"Intex Swimming Pool 15ft x 48'' Round with Accessories","sw3":"Swimming Goggles Xbase L Clear Lenses - Black","sw4":"Swimming Safety Tube  Blue color","swc1":3830,"swc2":31900,"swc3":299,"swc4":249},
        {"id":5,"Name":"Basketball","bk1":"basketball equipment for training 12 Boxes","bk2":"Deluxe 12 Ball Carrier (royal Blue)","bk3":"Nike Accessories Dominate 8p 7","bk4":"Gts Basketball Size With Net Basketball Ring","bkc1":7010,"bkc2":6572,"bkc3":1132,"bkc4":578}]
Mobiles=[{"id":1,"Name":"Apple","a1":"iphone 7","a2":"iphone 7 plus","a3":"iphone X","a4":"iphone XR","a5":"iphone 12 mini","a6":"iphone 12 pro","a7":"iphone 12","ac1":15000, "ac2":22000, "ac3":50000, "ac4":50000, "ac5":64000, "ac6":76000,"ac7": 118000},
        {"id":2,"Name":"Samsung","s1":"Galaxy M10","s2":"Galaxy A20","s3":"Galaxy A51","s4":"Galaxy Note 10","s5":"Galaxy S20","s6":"Galaxy Z flip","s7":"Galaxy S20 ultra","sc1":9000,"sc2":12000,"sc3":21000,"sc4":30000,"sc5":50000,"s6":"Galaxy Z flip","sc6":70000,"sc7":86000},
        {"id":3,"Name":"Realme","r1":"5 pro","r2":"Narzo 20","r3":"6 pro","r4":"7 Pro","r5":"X7","r6":"X3","r7":"X50 pro","rc1":14000,"rc2":15000,"rc3":18000,"rc4":20000,"rc5":20000,"rc6":25000,"rc7":42000},
        {"id":4,"Name":"Redmi","x1":"Mi 8A","x2":"Mi 9 prime","x3":"Mi Note 9 pro","x4":"Mi K30","x5":"Mi 10i","x6":"Mi 10T","x7":"Mi 10T pro","cx1":7000,"cx2":10000,"cx3":14000,"cx4":20000,"cx5":22000,"cx6":33000,"cx7":40000}]
Toys=[{"id":1,"Name":"Teddy","td1":"teddy bear 5 feet pink","td2":"teddy bear 3 feet panda","td3":"teddy bear 30 cm pack of 2 yellow","td4":"teddy bear 30 cm orange","tdc1":1700,"tdc2":700,"tdc3":400,"tdc4":300},
        {"id":2,"Name":"Hot Wheels","hw1":"Hot wheels Ultimate Gator Car Wash","hw2":"Hot Wheels Thrill Drivers Corkscrew","hw3":"Hot Wheels Color Shifters Sharkport Showdown, Multi Color","hw4":"Hot wheels 5 car gift pack","hwc1":6000,"hwc2":2500,"hwc3":1500,"hwc4":400},
        {"id":3,"Name":"RC Toys","rt1":"RC Robot","rt2":"RC Car","rt3":"RC Monster truck","rt4":"RC Helicopter","rct1":3500,"rct2":1500,"rct3":1200,"rct4":700},
        {"id":4,"Name":"Dolls","do1":"Barbie girls flying wings fairy doll Multi color","do2":"Doll House play set","do3":"Barbie Doll & Playset with Hair Styling Accessories","do4":"Beautiful Doll with foldable hands and make up accessories (Pink)","doc1":13000,"doc2":800,"doc3":600,"doc4":500},
        {"id":5,"Name":"Puzzle Games","pg1":"Jigsaw puzzle 4 in 1","pg2":"Frank Solar System Puzzle","pg3":"The Jungle Puzzle","pg4":"Negi Drop Puzzle Game","pgc1":250,"pgc2":250,"pgc3":150,"pgc4":100}]            
Books=[{"id":1,"Name":"Fiction Books","fb1":"Wings of Fire: An Autobiography of Abdul Kalam","fb2":"The Secret Of The Nagas (Shiva Trilogy-2)","fb3":"The Alchemist by Paulo Coelho","fb4":"Wuthering Heights by Emily Brontë","fbc1":400,"fbc2":300,"fbc3":200,"fbc4":100},
        {"id":2,"Name":"Religious Books","rb1":"The Art of Happiness","rb2":"The Book of Life","rb3":"The Prophet","rb4":"Bhagavad Gita","rbc1":300,"rbc2":300,"rbc3":200,"rbc4":200},
        {"id":3,"Name":"Story Books","sb1":"Harry Potter set of all 8 books","sb2":"Moral Story Books for Kids (Pack of 10 Books)","sb3":"The Complete Novels of Sherlock Holmes","sb4":"101 Fairy Tales Book","sbc1":2000,"sbc2":250,"sbc3":150,"sbc4":150},
        {"id":4,"Name":"Children Books","cb1":"Grandma's Bag of Stories","cb2":"Children's Encyclopedia","cb3":"101 Panchatantra Stories","cb4":"Space - My Knowledge Book","cbc1":200,"cbc2":150,"cbc3":150,"cbc4":100},
        {"id":5,"Name":"Programming Books","pb1":"Mastering Swift 5.3","pb2":"Core Java: An Integrated Approach","pb3":"Object-Oriented Programming with C++","pb4":"Learning with Python","pbc1":2000,"pbc2":550,"pbc3":500,"pbc4":300}]
Gaming=[{"id":1,"Name":"Gaming Consoles","xbox":"XBOX series","ps":"Play Station Series","nintendo":"Nintendo","xb1":"Microsoft Xbox One X 1TB Gaming Console (With Gold Rush Special Edition)","xb2":"Microsoft Xbox One X 1TB Gaming Console","xb3":"Microsoft Xbox One S 1TB Gaming Console","xb4":"Microsoft Xbox One S 500GB Gaming Console","xbc1":50000,"xbc2":41000,"xbc3":29000,"xbc4":25000,"ps1":"Sony PlayStation 5 (PS5) 1TB","ps2":"Sony PlayStation 4 (Black, 1TB)","ps3":"Sony PlayStation 4 (Black, 500GB)","ps4":"Sony Playstation 3 (500GB) with 3 Games","psc1":50000,"psc2":31000,"psc3":28000,"psc4":26000,"ni1":"Nintendo Switch Fortnite Special Edition Bundle","ni2":"Nintendo Switch with Neon Red & Neon Blue bundled (black)","ni3":"Nintendo Switch Lite - Gray","ni4":"Nintendo Switch Lite - Turquoise","nic1":40000,"nic2":32000,"nic3":20000,"nic4":20000},
        {"id":2,"Name":"Video Games","vg1":"Bully: Scholarship Edition","vg2":"Grand Theft Auto V – Premium","vg3":"Need For Speed: Rivals Hits","vg4":"Call of Duty: Ghosts","vgc1":2500,"vgc2":1500,"vgc3":1500,"vgc4":200},
        {"id":3,"Name":"Gaming Accessories","gc1":"Cosmic Byte GS410 Headphones with Mic","gc2":"Fireblade Gaming Wired Keyboard with LED Backlit","gc3":"Zebronics USB Gaming Mouse with LED Effect(Black)","gc4":"GO OFFER (2 pcs) Pubg Anti-Slip Thumb Sleeve","gcc1":1000,"gcc2":1000,"gcc3":400,"gcc4":100}]

#Declaring empty lists to store data.
price=[] 
user_name=[]
mobile_number=[]
password=[]
#Defining  functions for Dictionaries.
def electronics():
    print("Id\tName")
    print("------------------------------")
    for m in Electronic:
            print(m["id"],'\t',m["Name"])
    print("------------------------------")
    ch=input("Select:")
    if ch=='1':
        ac()
    elif ch=='2':
        tv()
    elif ch=='3':
        washmac()
    elif ch=='4':
        cam()  
    elif ch=='5':
        ref()                      
    else: 
        print("Please Select Proper number:")
        return electronics()
def sports():
    print("Id\tName")
    print("------------------------------")
    for m in Sports:
            print(m["id"],'\t',m["Name"])
    print("------------------------------")
    ch=input("Select:")
    if ch=='1':
        football()
    elif ch=='2':
        cricket()
    elif ch=='3':
        camp()
    elif ch=='4':
        swimming()
    elif ch=='5':
        basketball()                     
    else:  
        print("Please Select Proper number:")
        return sports()
def mobile():
    print("Id\tName")
    print("------------------------------")
    for m in Mobiles:
            print(m["id"],'\t',m["Name"])
    print("------------------------------")
    ch=input("Select:")
    if ch=='1':
        appl()
    elif ch=='2':
        samsung()
    elif ch=='3':
        realme()
    elif ch=='4':
        redmi()                     
    else:  
        print("Please Select Proper number:")
        return mobile()
def toys():
    print("Id\tName")
    print("------------------------------")
    for m in Toys:
            print(m["id"],'\t',m["Name"])
    print("------------------------------")
    ch=input("Select:")
    if ch=='1':
        teddy()
    elif ch=='2':
        hotwheels()
    elif ch=='3':
        rc()
    elif ch=='4':
        doll() 
    elif ch=='5':
        puzzle()                     
    else:  
        print("Please Select Proper number:")
        return toys()
def books():
    print("Id\tName")
    print("------------------------------")
    for m in Books:
            print(m["id"],'\t',m["Name"])
    print("------------------------------")
    ch=input("Select:")
    if ch=='1':
        fiction()
    elif ch=='2':
        religious()
    elif ch=='3':
        story()
    elif ch=='4':
        children()  
    elif ch=='5':
        programming()                   
    else:  
        print("Please Select Proper number:")
        return books()
def gaming():
    print("Id\tName")
    print("------------------------------")
    for m in Gaming:
            print(m["id"],'\t',m["Name"])
    print("------------------------------")
    ch=input("Select:")
    if ch=='1':
        console()
    elif ch=='2':
        video()
    elif ch=='3':
        accessories()                     
    else:  
        print("Please Select Proper number:")
        return gaming()

#Defining functions for Electronics.
def ac():
    print("-------------------------------------")
    print("Id\tName")
    print("-------------------------------------")
    for d in Electronic:
        try:
            print(f'1.\t{d["lga"]}\n2.\t{d["voltas"]}\n3.\t{d["tcl"]}\n4.\t{d["sac"]}')    
        except KeyError:
            pass
    print("-------------------------------------")
    ch=input("Select:")
    if ch=='1':
        lg()
    elif ch=='2':
        voltas()
    elif ch=='3':
        tcl()
    elif ch=='4':
        smartac()                     
    else:  
        print("Please Select Proper number!")
        return ac()
def tv():
    print("-------------------------------------")
    print("Id\tName")
    print("-------------------------------------")
    for d in Electronic:
        try:
            print(f'1.\t{d["samsung"]}\n2.\t{d["lgt"]}\n3.\t{d["sony"]}\n4.\t{d["mi"]}')    
        except KeyError:
            pass
    print("-------------------------------------")
    ch=input("Select:")
    if ch=='1':
        samsungtv()
    elif ch=='2':
        lgtv()
    elif ch=='3':
        sonytv()
    elif ch=='4':
        mitv()                     
    else:  
        print("Please Select Proper number!")
        return tv()
def washmac():
    print("-------------------------------------")
    print("Id\tName")
    print("-------------------------------------")
    for d in Electronic:
        try:
            print(f'1.\t{d["samsung"]}\n2.\t{d["whirlpool"]}\n3.\t{d["lgw"]}')    
        except KeyError:
            pass
    print("-------------------------------------")
    ch=input("Select:")
    if ch=='1':
        samsungwm()
    elif ch=='2':
        whirlpoolwm()
    elif ch=='3':
        lgwm()                    
    else:  
        print("Please Select Proper number!")
        return washmac()
def cam():
    print("-------------------------------------")
    print("Id\tName")
    print("-------------------------------------")
    for d in Electronic:
        try:
            print(f'1.\t{d["n"]}\n2.\t{d["c"]}\n3.\t{d["f"]}\n4.\t{d["s"]}')    
        except KeyError:
            pass
    print("-------------------------------------")
    ch=input("Select:")
    if ch=='1':
        nikon()
    elif ch=='2':
        canon()
    elif ch=='3':
        fujifilm()
    elif ch=='4':
        sonycam()                     
    else:  
        print("Please Select Proper number!")
        return cam()
def ref():
    print("-------------------------------------")
    print("Id\tName")
    print("-------------------------------------")
    for d in Electronic:
        try:
            print(f'{d["1.  samsung"]}\n2.  {d["whirlpool"]}\n3.  {d["haier"]}\n3.  {d["lgf"]}')    
        except KeyError:
            pass
    print("-------------------------------------")
    ch=input("Select:")
    if ch=='1':
        samsungrf()
    elif ch=='2':
        whirlpoolrf()
    elif ch=='3':
        haier()
    elif ch=='4':
        lgrf()                     
    else:  
        print("Please Select Proper number!")
        return ref()

#Defining functions for AC'S.
def lg():
    print("-----------------------------------------------------")
    print("Id\tModel list\t\t\t\tPrice")
    print("-----------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["la1"]}\t{d["lc1"]}\n2. {d["la2"]}\t{d["lc2"]}\n3. {d["la3"]}\t{d["lc3"]}\n4. {d["la4"]}\t{d["lc4"]}')    
        except KeyError:
            pass
    print("-----------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        lgac1=quantity*49700
        price.append(lgac1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        lgac2=quantity*41490
        price.append(lgac2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        lgac3=quantity*37490
        price.append(lgac3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        lgac4=quantity*32000
        price.append(lgac4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return lg()
def voltas():
    print("--------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\tPrice")
    print("--------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["v1"]}\t\t{d["vc1"]}\n2. {d["v2"]}\t\t{d["vc2"]}\n3. {d["v3"]}\t{d["vc3"]}\n4. {d["v4"]}\t\t{d["vc4"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        vac1=quantity*35000
        price.append(vac1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        vac2=quantity*30000
        price.append(vac2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        vac3=quantity*27000
        price.append(vac3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        vac4=quantity*25000
        price.append(vac4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return voltas()
def tcl():
    print("---------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\tPrice")
    print("---------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["tc1"]}\t{d["tcc1"]}\n2. {d["tc2"]}\t{d["tcc2"]}\n3. {d["tc3"]}\t{d["tcc3"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        tclac1=quantity*37000
        price.append(tclac1)
        total=sum(price)
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        tclac2=quantity*29000
        price.append(tclac2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        tclac3=quantity*26000
        price.append(tclac3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
        
    else:
        print("Please Select proper ID!")
        return tcl()
def smartac():
    print("--------------------------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\t\t\tPrice")
    print("--------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["sac1"]}\t\t{d["sacc1"]}\n2. {d["sac2"]}\t\t{d["sacc2"]}\n3. {d["sac3"]}\t\t{d["sacc3"]}\n4. {d["sac4"]}\t\t{d["sacc4"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        smartac1=quantity*53000
        price.append(smartac1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        smartac2=quantity*40000
        price.append(smartac2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        smartac3=quantity*37000
        price.append(smartac3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        smartac4=quantity*37000
        price.append(smartac4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return smartac()

#Defining functions for TV'S.
def samsungtv():
    print("------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\tPrice")
    print("------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["s1"]}\t\t{d["sc1"]}\n2. {d["s2"]}\t\t{d["sc2"]}\n3. {d["s3"]}\t\t{d["sc3"]}\n4. {d["s4"]}\t\t{d["sc4"]}')    
        except KeyError:
            pass
    print("------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        stv1=quantity*87990
        price.append(stv1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        stv2=quantity*49990
        price.append(stv2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        stv3=quantity*47990
        price.append(stv3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        stv4=quantity*16790
        price.append(stv4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return samsungtv()
def lgtv():
    print("--------------------------------------------------------------")
    print("Id\tModel list\t\t\t\tPrice")
    print("--------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["lt1"]}\t\t{d["lc1"]}\n2. {d["lt2"]}\t\t{d["lc2"]}\n3. {d["lt3"]}\t\t{d["lc3"]}\n4. {d["lt4"]}\t{d["lc4"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        lgtv1=quantity*49990
        price.append(lgtv1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        lgtv2=quantity*44999
        price.append(lgtv2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        lgtv3=quantity*349990
        price.append(lgtv3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        lgtv4=quantity*16999
        price.append(lgtv4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return lgtv()
def sonytv():
    print("------------------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\t\tPrice")
    print("------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["so1"]}\t\t{d["soc1"]}\n2. {d["so2"]}\t\t{d["soc2"]}\n3. {d["so3"]}\t\t{d["soc3"]}\n4. {d["so4"]}\t\t\t\t{d["soc4"]}')    
        except KeyError:
            pass
    print("------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        stv1=quantity*63999
        price.append(stv1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        stv2=quantity*59990
        price.append(stv2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        stv3=quantity*39999
        price.append(stv3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        stv4=quantity*34990
        price.append(stv4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return sonytv()
def mitv():
    print("---------------------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\t\tPrice")
    print("---------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["m1"]}\t{d["mc1"]}\n2. {d["m2"]}\t{d["mc2"]}\n3. {d["m3"]}\t\t{d["mc3"]}\n4. {d["m4"]}\t\t{d["mc4"]}')    
        except KeyError:
            pass
    print("---------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        mitv1=quantity*24000
        price.append(mitv1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        mitv2=quantity*20000
        price.append(mitv2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        mitv3=quantity*15000
        price.append(mitv3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        mitv4=quantity*15000
        price.append(mitv4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return mitv()

#Defining functions for Cameras.  
def nikon():
    print("-------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\tPrice")
    print("-------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["n1"]}\t\t{d["nc1"]}\n2. {d["n2"]}\t{d["nc2"]}\n3. {d["n3"]}\t{d["nc3"]}\n4. {d["n4"]}\t\t{d["nc4"]}')    
        except KeyError:
            pass
    print("-------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        n1=quantity*90034
        price.append(n1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        n2=quantity*72999
        price.append(n2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        n3=quantity*46999
        price.append(n3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        n4=quantity*32500
        price.append(n4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return nikon()
def canon():
    print("Id\tModel list\t\t\t\t\tPrice")
    print("--------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["c1"]}\t\t\t\t\t\t{d["cc1"]}\n2. {d["c2"]}\t\t{d["cc2"]}\n3. {d["c3"]}\t{d["cc3"]}\n4. {d["c4"]}\t\t\t{d["cc4"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        c1=quantity*215995
        price.append(c1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        c2=quantity*50000
        price.append(c2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        c3=quantity*15500
        price.append(c3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        c4=quantity*14000
        price.append(c4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return canon()
def fujifilm():
    print("Id\tModel list\t\t\tPrice")
    print("--------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["f1"]}\t{d["fc1"]}\n2. {d["f2"]}\t{d["fc2"]}\n3. {d["f3"]}\t{d["fc3"]}\n4. {d["f4"]}\t{d["fc4"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        f1=quantity*96000
        price.append(f1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        f2=quantity*78000
        price.append(f2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        f3=quantity*70000
        price.append(f3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        f4=quantity*67000
        price.append(f4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return fujifilm()
def sonycam():
    print("Id\tModel list\t\t\t\t\tPrice")
    print("--------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["sc1"]}\t\t\t{d["scc1"]}\n2. {d["sc2"]}\t\t\t{d["scc2"]}\n3. {d["sc3"]}\t\t{d["scc3"]}\n4. {d["sc4"]}\t{d["scc4"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        sc1=quantity*33000
        price.append(sc1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        sc2=quantity*27000
        price.append(sc2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        sc3=quantity*24000
        price.append(sc3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        sc4=quantity*11000
        price.append(sc4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return sonycam()

#Defining functions for Washing Machines.
def samsungwm():
    print("--------------------------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\t\t\tPrice")
    print("--------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["sw1"]}\t{d["swc1"]}\n2. {d["sw2"]}\t\t{d["swc2"]}\n3. {d["sw3"]}\t{d["swc3"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        swq1=quantity*18990
        price.append(swq1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        swq2=quantity*16790
        price.append(swq2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        swq3=quantity*14190
        price.append(swq3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return samsungwm()
def whirlpoolwm():
    print("----------------------------------------------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\t\t\t\t\tPrice")
    print("----------------------------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["ww1"]}\t\t{d["wwc1"]}\n2. {d["ww2"]}\t\t\t{d["wwc2"]}\n3. {d["ww3"]}\t\t\t{d["wwc3"]}')    
        except KeyError:
            pass
    print("----------------------------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        ww1=quantity*12990
        price.append(ww1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        ww2=quantity*9999
        price.append(ww2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        ww3=quantity*8990
        price.append(ww3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return whirlpoolwm()
def lgwm():
    print("--------------------------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\t\t\tPrice")
    print("--------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["lw1"]}\t\t{d["lc1"]}\n2. {d["lw2"]}\t\t{d["lc2"]}\n3. {d["lw3"]}\t\t{d["lc3"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        lw1=quantity*23990
        price.append(lw1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        lw2=quantity*19490
        price.append(lw2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        lw3=quantity*14990
        price.append(lw3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return lgwm()

#Defining functions for Refrigerators.
def samsungrf():
    print("--------------------------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\t\t\t       Price")
    print("--------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["sr1"]}\t\t{d["src1"]}\n2. {d["sr2"]}\t{d["src2"]}\n3. {d["sr3"]}\t\t\t\t\t{d["src3"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        sr1=quantity*18000
        price.append(sr1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        sr2=quantity*17000
        price.append(sr2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        sr2=quantity*15000
        price.append(sr2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return samsungrf()
def whirlpoolrf():
    print("--------------------------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\t\t\t       Price")
    print("--------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["wr1"]}\t\t{d["wrc1"]}\n2. {d["wr2"]}\t\t{d["wrc2"]}\n3. {d["wr3"]}\t{d["wrc3"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        wr1=quantity*22000
        price.append(wr1)
        total=sum(price)
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        wr2=quantity*15000
        price.append(wr2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        wr3=quantity*14000
        price.append(wr3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return whirlpoolrf()
def haier():
    print("--------------------------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\t\t\tPrice")
    print("--------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["hr1"]}\t\t{d["hrc1"]}\n2. {d["hr2"]}\t{d["hrc2"]}\n3. {d["hr3"]}\t{d["hrc3"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        hr1=quantity*16000
        price.append(hr1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        hr2=quantity*15000
        price.append(hr2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        hr3=quantity*14000
        price.append(hr3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return haier()
def lgrf():
    print("--------------------------------------------------------------------------------------------")
    print("Id\tModel list\t\t\t\t\t\t\t\tPrice")
    print("--------------------------------------------------------------------------------------------")
    for d in Electronic:
        try:
            print(f'1. {d["lr1"]}\t{d["lrc1"]}\n2. {d["lr2"]}\t\t{d["lrc2"]}\n3. {d["lr3"]}\t\t{d["lrc3"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        lgr1=quantity*24000
        price.append(lgr1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        lgr2=quantity*17000
        price.append(lgr2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        lgr3=quantity*16000
        price.append(lgr3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return lgrf()

#Defining functions for Sports.
def football():
    print("Id\t\tItem list \t\t\t\t\t\t Price")
    print("------------------------------------------------------------------------")
    for d in Sports:
        try:
            print(f'1 {d["fb1"]}\t{d["fbc1"]}\n2 {d["fb2"]}\t\t\t\t{d["fbc2"]}\n3 {d["fb3"]}\t\t\t\t\t{d["fbc3"]}\n4 {d["fb4"]}\t\t\t{d["fbc4"]}')    
        except KeyError:
            pass
    print("------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        f1=quantity*25558
        price.append(f1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        f2=quantity*3480
        price.append(f2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        f3=quantity*1290
        price.append(f3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        f4=quantity*229
        price.append(f4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return football()
def cricket():
    print("Id\t\tItem list \t\t\t\t\t\t Price")
    print("--------------------------------------------------------------------------------------------")
    for d in Sports:
        try:
            print(f'1 {d["ck1"]}\t\t{d["ckc1"]}\n2 {d["ck2"]}\t\t\t\t\t\t\t\t{d["ckc2"]}\n3 {d["ck3"]}\t\t{d["ckc3"]}\n4 {d["ck4"]}\t\t\t\t\t{d["ckc4"]}\n5 {d["ck5"]}\t\t\t\t\t\t\t{d["ckc5"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        cr1=quantity*8990
        price.append(cr1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        cr2=quantity*699
        price.append(cr2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        cr3=quantity*599
        price.append(cr3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        cr4=quantity*289
        price.append(cr4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==5:
        quantity = int(input("How many devices You want: "))
        cr5=quantity*220
        price.append(cr5)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return cricket()
def camp():
    print("Id\t\tItem list \t\t\t\t\t Price")
    print("------------------------------------------------------------------------")
    for d in Sports:
        try:
            print(f'1 {d["ch1"]}\t\t{d["chc1"]}\n2 {d["ch2"]}\t\t\t{d["chc2"]}\n3 {d["ch3"]}\t\t\t\t\t{d["chc3"]}\n4 {d["ch4"]}\t\t\t\t{d["chc4"]}')    
        except KeyError:
            pass
    print("------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        cp1=quantity*7999
        price.append(cp1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        cp2=quantity*3231
        price.append(cp2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        cp3=quantity*1199
        price.append(cp3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        cp4=quantity*384
        price.append(cp4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return camp()
def swimming():
    print("Id\t\tItem list \t\t\t\t\t\tPrice")
    print("------------------------------------------------------------------------")
    for d in Sports:
        try:
            print(f'1 {d["sw1"]}\t\t\t\t\t\t\t{d["swc1"]}\n2 {d["sw2"]}\t\t{d["swc2"]}\n3 {d["sw3"]}\t\t\t\t{d["swc3"]}\n4 {d["sw4"]}\t\t\t\t\t{d["swc4"]}')    
        except KeyError:
            pass
    print("------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        sw1=quantity*3830
        price.append(sw1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        sw2=quantity*31900
        price.append(sw2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        sw3=quantity*299
        price.append(sw3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        sw4=quantity*249
        price.append(sw4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return swimming()
def basketball():
    print("Id\t\tItem list \t\t\t\tPrice")
    print("------------------------------------------------------------------------")
    for d in Sports:
        try:
            print(f'1 {d["bk1"]}\t\t{d["bkc1"]}\n2 {d["bk2"]}\t\t\t{d["bkc2"]}\n3 {d["bk3"]}\t\t\t{d["bkc3"]}\n4 {d["bk4"]}\t\t{d["bkc4"]}')    
        except KeyError:
            pass
    print("------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        bk1=quantity*7010
        price.append(bk1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        bk2=quantity*6572
        price.append(bk2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        bk3=quantity*1132
        price.append(bk3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        bk4=quantity*578
        price.append(bk4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return basketball()

#Defining functions for Mobiles.
def appl():
    print("Id\tModel name \t Price")
    print("----------------------------------------------------")
    for d in Mobiles:
        try:
            print(f'1.{d["a1"]}\t{d["ac1"]}\n{d["a2"]}\t{d["ac2"]}\n{d["a3"]}\t{d["ac3"]}\n{d["a4"]}\t{d["ac4"]}\n{d["a5"]}\t{d["ac5"]}\n{d["a6"]}\t{d["ac6"]}\n5 {d["a7"]}\t{d["ac7"]}')    
        except KeyError:
            pass
    print("----------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        a1=quantity*15000
        price.append(a1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        a2=quantity*22000
        price.append(a2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        a3=quantity*50000
        price.append(a3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        a4=quantity*50000
        price.append(a4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==5:
        quantity = int(input("How many devices You want: "))
        a5=quantity*64000
        price.append(a5)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==6:
        quantity = int(input("How many devices You want: "))
        a6=quantity*76000
        price.append(a6)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==7:
        quantity = int(input("How many devices You want: "))
        a7=quantity*118000
        price.append(a7)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return appl()
def samsung():
    print("Model name \t\t Price")
    print("----------------------------------------------------")
    for d in Mobiles:
        try:
            print(f'{d["s1"]}\t\t{d["sc1"]}\n{d["s2"]}\t\t{d["sc2"]}\n{d["s3"]}\t\t{d["sc3"]}\n{d["s4"]}\t\t{d["sc4"]}\n{d["s5"]}\t\t{d["sc5"]}\n{d["s6"]}\t\t{d["sc6"]}\n{d["s7"]}\t{d["sc7"]}')    
        except KeyError:
            pass
    print("----------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        sm1=quantity*9000
        price.append(sm1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        sm2=quantity*12000
        price.append(sm2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        sm3=quantity*21000
        price.append(sm3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        sm4=quantity*30000
        price.append(sm4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==5:
        quantity = int(input("How many devices You want: "))
        sm5=quantity*50000
        price.append(sm5)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==6:
        quantity = int(input("How many devices You want: "))
        sm6=quantity*70000
        price.append(sm6)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==7:
        quantity = int(input("How many devices You want: "))
        sm7=quantity*86000
        price.append(sm7)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return samsung()
def realme():
    print("Model name \t Price")
    print("----------------------------------------------------")
    for d in Mobiles:
        try:
            print(f'{d["r1"]}\t\t{d["rc1"]}\n{d["r2"]}\t{d["rc2"]}\n{d["r3"]}\t\t{d["rc3"]}\n{d["r4"]}\t\t{d["rc4"]}\n{d["r5"]}\t\t{d["rc5"]}\n{d["r6"]}\t\t{d["rc6"]}\n{d["r7"]}\t\t{d["rc7"]}')    
        except KeyError:
            pass
    print("----------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        rm1=quantity*14000
        price.append(rm1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        rm2=quantity*15000
        price.append(rm2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        rm3=quantity*18000
        price.append(rm3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        rm4=quantity*20000
        price.append(rm4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==5:
        quantity = int(input("How many devices You want: "))
        rm5=quantity*20000
        price.append(rm5)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==6:
        quantity = int(input("How many devices You want: "))
        rm6=quantity*25000
        price.append(rm6)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==7:
        quantity = int(input("How many devices You want: "))
        rm7=quantity*42000
        price.append(rm7)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return realme()
def redmi():
    print("Model name \t Price")
    print("----------------------------------------------------")
    for d in Mobiles:
        try:
            print(f'{d["x1"]}\t\t{d["cx1"]}\n{d["x2"]}\t{d["cx2"]}\n{d["x3"]}\t{d["cx3"]}\n{d["x4"]}\t\t{d["cx4"]}\n{d["x5"]}\t\t{d["cx5"]}\n{d["x6"]}\t\t{d["cx6"]}\n{d["x7"]}\t{d["cx7"]}')    
        except KeyError:
            pass
    print("----------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        xm1=quantity*7000
        price.append(xm1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        xm2=quantity*10000
        price.append(xm2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        xm3=quantity*14000
        price.append(xm3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        xm4=quantity*20000
        price.append(xm4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==5:
        quantity = int(input("How many devices You want: "))
        xm5=quantity*22000
        price.append(xm5)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==6:
        quantity = int(input("How many devices You want: "))
        xm6=quantity*33000
        price.append(xm6)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==7:
        quantity = int(input("How many devices You want: "))
        xm7=quantity*40000
        price.append(xm7)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return redmi()

#Defining functions for Toys.
def teddy():
    print("Id\tItem list\t\t\t Price")
    print("----------------------------------------------------")
    for d in Toys:
        try:
            print(f'1. {d["td1"]}\t\t{d["tdc1"]}\n2. {d["td2"]}\t\t{d["tdc2"]}\n3. {d["td3"]}\t{d["tdc3"]}\n4. {d["td4"]}\t\t{d["tdc4"]}')    
        except KeyError:
            pass
    print("----------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        td1=quantity*1700
        price.append(td1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        td2=quantity*700
        price.append(td2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        td3=quantity*400
        price.append(td3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        td4=quantity*300
        price.append(td4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return teddy()
def hotwheels():
    print("Id\t\tItem list\t\t\t\t\t Price")
    print("-----------------------------------------------------------------------------")
    for d in Toys:
        try:
            print(f'1. {d["hw1"]}\t\t\t\t{d["hwc1"]}\n2. {d["hw2"]}\t\t\t\t{d["hwc2"]}\n3. {d["hw3"]}\t{d["hwc3"]}\n4. {d["hw4"]}\t\t\t\t\t{d["hwc4"]}')    
        except KeyError:
            pass
    print("-----------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        hw1=quantity*6000
        price.append(hw1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        hw2=quantity*2500
        price.append(hw2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        hw3=quantity*1500
        price.append(hw3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        hw4=quantity*400
        price.append(hw4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return hotwheels()
def rc():
    print("Id\tItem list\tPrice")
    print("-----------------------------------------------------------------------------")
    for d in Toys:
        try:
            print(f'1. {d["rt1"]}\t\t{d["rct1"]}\n2. {d["rt2"]}\t\t{d["rct2"]}\n3. {d["rt3"]}\t{d["rct3"]}\n4. {d["rt4"]}\t{d["rct4"]}')    
        except KeyError:
            pass
    print("-----------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        rc1=quantity*3500
        price.append(rc1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        rc2=quantity*1500
        price.append(rc2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        rc3=quantity*1200
        price.append(rc3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        rc4=quantity*700
        price.append(rc4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return rc()
def doll():
    print("Id\tItem list\t\t\t\t\t\t\tPrice")
    print("----------------------------------------------------------------------------------")
    for d in Toys:
        try:
            print(f'1. {d["do1"]}\t\t\t{d["doc1"]}\n2. {d["do2"]}\t\t\t\t\t\t\t{d["doc2"]}\n3. {d["do3"]}\t\t\t{d["doc3"]}\n4. {d["do4"]}\t{d["doc4"]}')    
        except KeyError:
            pass
    print("----------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        d1=quantity*13000
        price.append(d1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        d2=quantity*800
        price.append(d2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        d3=quantity*600
        price.append(d3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        d4=quantity*500
        price.append(d4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return doll()
def puzzle():
    print("Id\tItem list\t\tPrice")
    print("-----------------------------------------------------")
    for d in Toys:
        try:
            print(f'1. {d["pg1"]}\t\t{d["pgc1"]}\n2. {d["pg2"]}\t{d["pgc2"]}\n3. {d["pg3"]}\t\t{d["pgc3"]}\n4. {d["pg4"]}\t{d["pgc4"]}')    
        except KeyError:
            pass
    print("----------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        p1=quantity*250
        price.append(p1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        p2=quantity*250
        price.append(p2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        p3=quantity*150
        price.append(p3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        p4=quantity*100
        price.append(p4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return puzzle()

#Defining functions for Books.
def fiction():
    print("Id\tItem list\t\t\t\t\tPrice")
    print("---------------------------------------------------------------")
    for d in Books:
        try:
            print(f'1. {d["fb1"]}\t{d["fbc1"]}\n2. {d["fb2"]}\t\t{d["fbc2"]}\n3. {d["fb3"]}\t\t\t{d["fbc3"]}\n4. {d["fb4"]}\t\t\t{d["fbc4"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        f1=quantity*400
        price.append(f1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        f2=quantity*300
        price.append(f2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        f3=quantity*200
        price.append(f3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        f4=quantity*100
        price.append(f4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return fiction()
def religious():
    print("Id\tItem list\t\tPrice")
    print("-----------------------------------------------------------------------------")
    for d in Books:
        try:
            print(f'1. {d["rb1"]}\t\t{d["rbc1"]}\n2. {d["rb2"]}\t\t{d["rbc2"]}\n3. {d["rb3"]}\t\t\t{d["rbc3"]}\n4. {d["rb4"]}\t\t{d["rbc4"]}')    
        except KeyError:
            pass
    print("-----------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        rb1=quantity*300
        price.append(rb1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        rb2=quantity*300
        price.append(rb2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        rb3=quantity*200
        price.append(rb3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        rb4=quantity*200
        price.append(rb4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return religious()
def story():
    print("Id\tItem list\t\t\t\t\tPrice")
    print("-----------------------------------------------------------------------------")
    for d in Books:
        try:
            print(f'1. {d["sb1"]}\t\t\t{d["sbc1"]}\n2. {d["sb2"]}\t{d["sbc2"]}\n3. {d["sb3"]}\t\t{d["sbc3"]}\n4. {d["sb4"]}\t\t\t\t\t{d["sbc4"]}')    
        except KeyError:
            pass
    print("-----------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        sb1=quantity*2000
        price.append(sb1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        sb2=quantity*250
        price.append(sb2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        sb3=quantity*150
        price.append(sb3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        sb4=quantity*150
        price.append(sb4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return story()
def children():
    print("Id\tItem list\t\tPrice")
    print("-----------------------------------------------------------------------------")
    for d in Books:
        try:
            print(f'1. {d["cb1"]}\t\t{d["cbc1"]}\n2. {d["cb2"]}\t\t{d["cbc2"]}\n3. {d["cb3"]}\t\t{d["cbc3"]}\n4. {d["cb4"]}\t\t{d["cbc4"]}')    
        except KeyError:
            pass
    print("-----------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        cb1=quantity*200
        price.append(cb1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        cb2=quantity*150
        price.append(cb2)
        total=sum(price)
        pprint("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        cb3=quantity*150
        price.append(cb3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        cb4=quantity*100
        price.append(cb4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return children()
def programming():
    print("Id\tItem list\t\t\t\tPrice")
    print("-----------------------------------------------------------------------------")
    for d in Books:
        try:
            print(f'1. {d["pb1"]}\t\t\t\t{d["pbc1"]}\n2. {d["pb2"]}\t\t{d["pbc2"]}\n3. {d["pb3"]}\t\t{d["pbc3"]}\n4. {d["pb4"]}\t\t\t\t{d["pbc4"]}')    
        except KeyError:
            pass
    print("-----------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        pb1=quantity*2000
        price.append(pb1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        pb2=quantity*550
        price.append(pb2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        pb3=quantity*500
        price.append(pb3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        pb4=quantity*300
        price.append(pb4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return programming()

#Defining functions for Games
def console():

    print("No.\tModel name")
    print("-------------------------------------")
    for d in Gaming:
        try:
            print(f'1. {d["xbox"]}\n2. {d["ps"]}\n3. {d["nintendo"]}')    
        except KeyError:
            pass
    print("----------------------------------------------------")
    s=input("Select: ")
    if s=='1':
        xbox()
    elif s=='2':
        ps()
    elif s=='3':
        nintendo()
    else:
        print("Please Select proper ID!")
        return console()
def video():
    print("No.\tGaming C.D. list\t\tPrice")
    print("----------------------------------------------------")
    for d in Gaming:
        try:
            print(f'1. {d["vg1"]}\t\t{d["vgc1"]}\n2. {d["vg2"]}\t\t{d["vgc2"]}\n3. {d["vg3"]}\t\t{d["vgc3"]}\n4. {d["vg4"]}\t\t\t{d["vgc4"]}')    
        except KeyError:
            pass
    print("----------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        vg1=quantity*25000
        price.append(vg1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        vg2=quantity*15000
        price.append(vg2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        vg3=quantity*1500
        price.append(vg3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        vg4=quantity*200
        price.append(vg4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return video()
def accessories():
    print("No.\tAccessories list\t\t\t\t\tPrice")
    print("-------------------------------------------------------------------")
    for d in Gaming:
        try:
            print(f'1. {d["gc1"]}\t\t\t{d["gcc1"]}\n2. {d["gc2"]}\t\t{d["gcc2"]}\n3. {d["gc3"]}\t\t{d["gcc3"]}\n4. {d["gc4"]}\t\t\t{d["gcc4"]}')    
        except KeyError:
            pass
    print("-------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        ag1=quantity*1000
        price.append(ag1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        ag2=quantity*10000
        price.append(ag2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        ag3=quantity*400
        price.append(ag3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        ag4=quantity*100
        price.append(ag4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return accessories()

#Defining functions for Gaming Consoles.
def xbox():
    print("Id\tItem list\t\t\t\t\t\t\t\tPrice")
    print("--------------------------------------------------------------------------------------------")
    for d in Gaming:
        try:
            print(f'1. {d["xb1"]}\t{d["xbc1"]}\n2. {d["xb2"]}\t\t\t\t\t{d["xbc2"]}\n3. {d["xb3"]}\t\t\t\t\t{d["xbc3"]}\n4. {d["xb4"]}\t\t\t\t\t{d["xbc4"]}')    
        except KeyError:
            pass
    print("--------------------------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        xb1=quantity*50000
        price.append(xb1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        xb2=quantity*41000
        price.append(xb2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        xb3=quantity*29000
        price.append(xb3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        xb4=quantity*25000
        price.append(xb4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return xbox()
def ps():
    print("Id\tItem list\t\t\t\tPrice")
    print("-------------------------------------------------------------------")
    for d in Gaming:
        try:
            print(f'1. {d["ps1"]}\t\t\t{d["psc1"]}\n2. {d["ps2"]}\t\t{d["psc2"]}\n3. {d["ps3"]}\t\t{d["psc3"]}\n4. {d["ps4"]}\t{d["psc4"]}')    
        except KeyError:
            pass
    print("-------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        ps1=quantity*50000
        price.append(ps1)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        ps2=quantity*3100
        price.append(ps2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        ps3=quantity*28000
        price.append(ps3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        ps4=quantity*26000
        price.append(ps4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return ps()
def nintendo():

    print("Id\tItem list\t\t\t\t\t\tPrice")
    print("-----------------------------------------------------------------------------")
    for d in Gaming:
        try:
            print(f'1. {d["ni1"]}\t\t{d["nic1"]}\n2. {d["ni2"]}\t{d["nic2"]}\n3. {d["ni3"]}\t\t\t\t\t{d["nic3"]}\n4. {d["ni4"]}\t\t\t\t{d["nic4"]}')    
        except KeyError:
            pass
    print("-----------------------------------------------------------------------------")
    ch=int(input("please select device id:"))
    if ch==1:          
        quantity = int(input("How many devices You want: "))
        ng1=quantity*40000
        price.append(ng1)
        total=sum(price)
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        conti()
    elif ch==2:
        quantity = int(input("How many devices You want: "))
        ng2=quantity*32000
        price.append(ng2)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==3:
        quantity = int(input("How many devices You want: "))
        ng3=quantity*20000
        price.append(ng3)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    elif ch==4:
        quantity = int(input("How many devices You want: "))
        ng4=quantity*20000
        price.append(ng4)
        total=sum(price)
        print("-----------------------------------------")
        print("Your Selected Item Is Added To Cart!")
        print("Total price in Your cart is: ",total)
        print("-----------------------------------------")
        conti()
    else:
        print("Please Select proper ID!")
        return nintendo()

#Defining functions for user Logged screen.      
def userLogin():
    print("---------------------\n")
    print("1.Display Menu")
    print("2.Place order")
    print("3.Logout")
    print("4.Exit")
    print("\n---------------------")

#Defining functions for Display Home Screen.
def userDisplayMenu():
    print("--------------------------------------------------")
    print("Welcome to the online Store. What you want to Purchased? \n1. Electronics Appliances \n2. Sports \n3. Mobiles \n4. Toys\n5. Books\n6. Gaming\n7. Exit")
    print("--------------------------------------------------")
    select = int(input("Please, Select the number you wish for: "))
    print("--------------------------------------------------")
    if(select==1):
        electronics()
    elif(select==2):
        sports()
    elif(select==3):
        mobile()
    elif(select==4):
        toys()
    elif(select==5):
        books()
    elif(select==6):
        gaming()
    elif(select==7):
         sys.exit()
    else:
        print("Please make proper selection !")                    

#Defining functions to Place Order.
def placeOrder():
    print("Total Items added in your cart is: ",len(price)) 
    total=sum(price) 
    print("Your total price is: ",total)
    p=input("Do Your want to continue your payment?\n1.Yes\n2. No.")
    if p=="1" or "Yes" or "yes" or "y" or"Y":
        payment()
    elif p=="2" or "No" or "no" or "n" or"N":
        return(userDisplayMenu())    
    else:
        print("Please Select Proper value!!!")
        return placeOrder()

#Defining functions for Payment Options.
def payment():
    print("Please select your payment method...\n1. Cash on Delivery (COD)\n2. Debit card \n3. Credit Card.")
    w =input("Please, Select the number for Transaction mode: ")
    if (w == "1" or w =="Cash on Delivery"  or w =="cash on delivery" or w =="COD" or w =="cod"):
        print("Enter Your personal details below")
        a=input("Enter your delivery address with pin code:")
        m=input("Enter your mobile number: ")
        print("Following are your details: \n" ,"Address: ",a ,"\n" ,"Mobile no.: ",m, "\n" )   
        print("Your product will be delivered to given address soon,\n Thank Your For Shopping !!") 
        con=input("Do You want to Continue your shopping further?\n1.Yes\n2. No.")
        if con=="1" or "Yes" or "yes" or "y" or"Y":
            userDisplayMenu()    
        else:
            sys.exit()
    elif (w == "2"or w =="Debit Card" or w =="debit card"):
        d=int(input("Enter Your Debit Card number: "))
        e=input("Enter expire date: ")
        c=int(input("Enter CVV no.: "))
        a=input("Enter your delivery address with pin code:")
        m=int(input("Enter your mobile number: "))

        print("Following are your details: \n" ,"Address: ",a ,"\n" ,"Mobile no.: ",m, "\n" )
        print("Your product will be delivered to given address soon,\n Thank Your For Shopping !!")
        con=input("Do You want to Continue your shopping further?\n1.Yes\n2. No.")
        if con=="1" or "Yes" or "yes" or "y" or"Y":
            userDisplayMenu()    
        else:
            sys.exit()
    elif (w == "3" or w =="credit card"or w =="Credit Catd"):
        d=input("Enter Your Credit Card number: ")
        e=input("Enter expire date: ")
        c=input("Enter CVV no.: ")
        a=input("Enter your delivery address with pin code:")
        m=input("Enter your mobile number: ")
        print("Following are your details: \n" ,"Address: ",a ,"\n" ,"Mobile no.: ",m, "\n" )
        print("Your product will be delivered to given address soon,\n Thank Your For Shopping !!")
        con=input("Do You want to Continue your shopping further?\n1.Yes\n2. No.")
        if con=="1" or "Yes" or "yes" or "y" or"Y":
            userDisplayMenu()    
        else:
            sys.exit()
    else:
        print("Please Provide valid information.")
        return (payment())

#Defining functions User Choice.
def userChoice():
    choice=int(input("Please enter user choice : "))
    if choice==1:
        userDisplayMenu()
        print("\n---------------------------------------------------\n")
        userLogin()
        print("\n---------------------------------------------------\n")
        userChoice()
    elif choice==2:
        placeOrder()
        print("\n---------------------------------------------------\n")
        userLogin()
        print("\n---------------------------------------------------\n")
        userChoice()
    elif choice==3:
        logout()
    elif choice==4:
        sys.exit()
    else:
        print("Please select proper number")
        return userChoice()

#Defining functions for continue shopping.
def conti():
    print("Do you want to continue your shopping?\n 1. Yes\n2. No")
    con=input("Select one from above: " )
    if (con== "1" or con=="yes" or con=="Yes"):
        userDisplayMenu()
    elif (con== "2" or con=="no" or con=="No"):
        placeOrder()
    else:
        print("Select Proper number.")
        return conti()
#Defining functions for Log-Out.
def logout():
    login()

#Defining functions for login.
def login():
    print("------------------------------------------------------------------")
    print("How Do You Want to Login\n1. User Name\n2. Mobile Number: ")
    lo=input("Please Select one from above option")
    if lo=='User Name' or lo=='user name' or lo=='1':
        u=input("Enter username:")
        passw=input("Enter the password : ")
        if u in user_name and passw in password:
            userDisplayMenu()
        else:
            print("Invalid password. Please enter valid password")
            login()

    elif lo=='Mobile Number' or lo=='mobile number' or lo=="2":
        m=input("Enter mobile number:")
        passw=input("Enter the password : ")
        if m in mobile_number and passw in password:
            userDisplayMenu()
        else:
            print("Invalid password. Please enter valid password")
            login()
    else:
        print("Invalid user type. Enter valid user type")
        return login()

#Defining functions for user login or New Registration.
def new():
    print("Do You Want to Login or Register or use Guest Account ? ")
    ch=input("Select your choice: ")
    if (ch=="login" or ch=="Login" or ch=="1") :
        login()
    elif (ch== "register" or ch=="Register" or ch== "2"):
        u=input("Enter username you want to register:")
        m=input("Enter Your Mobile Number: ")
        p=input("Enter password you want to register:")
        user_name.append(u)
        mobile_number.append(m)

        password.append(p)
        print("Your User-Name is: ",user_name)
        print("Your Mobile number is: ",m)
        print("Your Password is: ", password)
        login()
    elif (ch== "guest" or ch=="Guest" or ch== "Guest Account" or ch== "guest account" or ch== "3"):
        userDisplayMenu()
    else:
        print("Please Select valid number")
        return new()
new()

# user can add these wardrobes to dictionary. if want and define following functions.
# Wardrobes=[{"id":1,"Name":"Men's Fashion"},
#             {"id":2,"Name":"Women's Fashion"},
#             {"id":3,"Name":"Kids Fashion"},
#             {"id":4,"Name":"Footwear"},
#             {"id":5,"Name":"Watches"}]
# def software():
#     pass   
# def menfas():
#     pass
# def womenfas():
#     pass
# def kidsfas():
#     pass
# def shoe():
#     pass
# def watch():
#     pass