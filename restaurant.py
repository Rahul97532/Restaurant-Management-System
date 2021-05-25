from tkinter import*
from tkinter import messagebox as mb
import random
import time

from reportlab.pdfgen import canvas



root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Billing System")

Tops = Frame(root,width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'Helvetica' ,30, 'bold' ),text="Restaurant Billing System",fg="blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'Helvetica' ,20, ),text=localtime,fg="blue",anchor=W)
lblinfo.grid(row=1,column=0)

#---------------Calculator------------------
text_Input=StringVar()
operator =""

txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Receipt_generate():

    ordno=rand.get()
    cust_name=Name.get()
    ph=Phone.get()
    if ordno=='' or cust_name=='' or ph=='':
        mb.showerror('error','Please place an order!!!')
        return
    
    if Fries.get()=='':
        cof=0;
    else:
        cof =float(Fries.get())
    if Largefries.get()=='':
        colfries=0;
    else:
        colfries =float(Largefries.get())
    if Burger.get()=='':
        cob=0;
    else:
        cob =float(Burger.get())
    if Filet.get()=='':
        cofi=0;
    else:
        cofi =float(Filet.get())
    if Cheese_burger.get()=='':
        cochee=0;
    else:
        cochee =float(Cheese_burger.get())
    if Drinks.get()=='':
        codr=0;
    else:
        codr =float(Drinks.get())

    #---------Order details dictionary--------------------
    #keys conatin item name and value conatin list of qty and price of all items
    Purchases={'Fries': [cof, 50 ] ,'Large Fries': [colfries, 80 ] ,'Burger': [cob, 50 ] ,'Pizza': [cofi, 220 ] ,'Cheese Burger': [cochee, 80 ] ,'Drinks': [codr, 70 ]}




    #-----------------Generate PDF----------------------------------------

    # Creating Canvas
    f_name=f"Invoice{ordno}.pdf"
    c = canvas.Canvas(f_name,pagesize=(200,250),bottomup=0)
    # Logo Section
    # Setting th origin to (10,40)
    c.translate(10,40)
    # Inverting the scale for getting mirror Image of logo
    c.scale(1,-1)
    # Inserting Logo into the Canvas at required position


    c.drawImage("logo.jpg",0,0,width=50,height=30)


    # Title Section
    # Again Inverting Scale For strings insertion
    c.scale(1,-1)
    # Again Setting the origin back to (0,0) of top-left
    c.translate(-10,-40)
    # Setting the font for Name title of company
    c.setFont("Helvetica-Bold",10)
    # Inserting the name of the company
    c.drawCentredString(125,20,"XYZ Food Court")
    # For under lining the title
    c.line(70,22,180,22)
    # Changing the font size for Specifying Address
    c.setFont("Helvetica-Bold",5)
    c.drawCentredString(125,30,"Block No. 101, Triveni Apartments, Pitam Pura,")
    c.drawCentredString(125,35,"New Delhi - 110034, India")
    # Changing the font size for Specifying GST Number of firm
    c.setFont("Helvetica-Bold",6)
    c.drawCentredString(125,42,"GSTIN : 07AABCS1429B1Z")
    # Line Seprating the page header from the body
    c.line(5,45,195,45)
    # Document Information
    # Changing the font for Document title
    c.setFont("Courier-Bold",8)
    c.drawCentredString(100,55,"TAX-INVOICE")
    # This Block Consist of Costumer Details
    c.roundRect(15,63,170,40,10,stroke=1,fill=0)
    c.setFont("Times-Bold",5)
    c.drawRightString(70,70,"INVOICE No. :")
    c.drawRightString(70,80,"DATE & TIME :")
    c.drawRightString(70,90,"CUSTOMER NAME :")
    c.drawRightString(70,100,"PHONE No. :")
    # This Block Consist of Item Description
    c.roundRect(15,108,170,130,10,stroke=1,fill=0)
    c.line(15,120,185,120)
    c.drawCentredString(25,118,"SR No.")
    c.drawCentredString(75,118,"ITEM")
    c.drawCentredString(125,118,"QTY")
    c.drawCentredString(148,118,"RATE")
    c.drawCentredString(173,118,"TOTAL")
    # Drawing table for Item Description
    c.line(15,210,185,210)
    c.line(35,108,35,220)
    c.line(115,108,115,220)
    c.line(135,108,135,220)
    c.line(160,108,160,220)
    # Declaration and Signature
    c.line(15,220,185,220)
    c.line(100,220,100,238)
    c.drawString(20,225,"We declare that above mentioned")
    c.drawString(20,230,"information is true.")
    c.drawString(20,235,"(This is system generated invoice)")
    c.drawRightString(180,235,"Authorised Signatory")
    
    localtime=time.asctime(time.localtime(time.time()))

    c.drawString(90,70,rand.get())
    c.drawString(90,80,localtime)
    c.drawString(90,90,Name.get())
    c.drawString(90,100,Phone.get())


    counter=0
    #----res_pur is dictionary of ordered items-----------
    res_pur={}

    
    for x,y in Purchases.items():
        if y[0]==0:
            continue
        res_pur[x]=y
    length=len(res_pur)
    item_names=list(res_pur.keys())
    item_descs=list(res_pur.values())
    if counter<length:
        counter+=1
        c.drawCentredString(28,125,str(counter))
        c.drawCentredString(65,125,str(item_names[0]))
        c.drawCentredString(127,125,str(item_descs[0][0]))
        c.drawCentredString(148,125,str(item_descs[0][1]))
        c.drawCentredString(170,125,str(item_descs[0][0]*item_descs[0][1]))
    if counter<length:
        counter+=1
        c.drawCentredString(28,135,str(counter))
        c.drawCentredString(65,135,str(item_names[1]))
        c.drawCentredString(127,135,str(item_descs[1][0]))
        c.drawCentredString(148,135,str(item_descs[1][1]))
        c.drawCentredString(170,135,str(item_descs[1][0]*item_descs[1][1]))
    if counter<length:
        counter+=1
        c.drawCentredString(28,145,str(counter))
        c.drawCentredString(65,145,str(item_names[2]))
        c.drawCentredString(127,145,str(item_descs[2][0]))
        c.drawCentredString(148,145,str(item_descs[2][1]))
        c.drawCentredString(170,145,str(item_descs[2][0]*item_descs[2][1]))
    if counter<length:
        counter+=1
        c.drawCentredString(28,155,str(counter))
        c.drawCentredString(65,155,str(item_names[3]))
        c.drawCentredString(127,155,str(item_descs[3][0]))
        c.drawCentredString(148,155,str(item_descs[3][1]))
        c.drawCentredString(170,155,str(item_descs[3][0]*item_descs[3][1]))
    if counter<length:
        counter+=1
        c.drawCentredString(28,165,str(counter))
        c.drawCentredString(65,165,str(item_names[4]))
        c.drawCentredString(127,165,str(item_descs[4][0]))
        c.drawCentredString(148,165,str(item_descs[4][1]))
        c.drawCentredString(170,165,str(item_descs[4][0]*item_descs[4][1]))
    if counter<length:
        counter+=1
        c.drawCentredString(28,175,str(counter))
        c.drawCentredString(65,175,str(item_names[5]))
        c.drawCentredString(127,175,str(item_descs[5][0]))
        c.drawCentredString(148,175,str(item_descs[5][1]))
        c.drawCentredString(170,175,str(item_descs[5][0]*item_descs[5][1]))

    s_charge=Service_Charge.get()
    gst=Tax.get()
    tc=Total.get()
    print(s_charge)
    c.drawCentredString(65,200,"Service Charge")
    c.drawCentredString(65,208,"GST")
    c.drawCentredString(65,218,"Total")
    c.drawCentredString(170,200,s_charge[9:len(s_charge)-2])
    c.drawCentredString(170,208,gst[9:len(gst)-2])
    c.drawCentredString(170,218,tc[9:len(tc)-2])
        

        

        ## Maintain a count to count diff items also check the price calculate it and display total.
        # End the Page and Start with new
    c.showPage()
        # Saving the PDF
    c.save()

    mb.showinfo("Success",f"Receipt for Order No: {ordno} generated..")


def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    if Fries.get()=='':
        cof=0;
    else:
        cof =float(Fries.get())
    if Largefries.get()=='':
        colfries=0;
    else:
        colfries =float(Largefries.get())
    if Burger.get()=='':
        cob=0;
    else:
        cob =float(Burger.get())
    if Filet.get()=='':
        cofi=0;
    else:
        cofi =float(Filet.get())
    if Cheese_burger.get()=='':
        cochee=0;
    else:
        cochee =float(Cheese_burger.get())
    if Drinks.get()=='':
        codr=0;
    else:
        codr =float(Drinks.get())

    costoffries = cof*50
    costoflargefries = colfries*80
    costofburger = cob*50
    costoffilet = cofi*220
    costofcheeseburger = cochee*80
    costofdrinks = codr*70

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.18)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)*.01)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str('%.2f'%( PayTax + Totalcost + Ser_Charge))
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")
    Name.set("")
    Phone.set("")


#---------------------------Calculator coding-----------------------------------------


btn7=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="powder blue", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="8",bg="powder blue", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="9",bg="powder blue", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="+",bg="powder blue", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="4",bg="powder blue", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="5",bg="powder blue", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="6",bg="powder blue", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="-",bg="powder blue", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="1",bg="powder blue", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="2",bg="powder blue", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="3",bg="powder blue", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="*",bg="powder blue", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="0",bg="powder blue", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="c",bg="powder blue", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="black", font=('ariel', 20 ,'bold'),text="=",bg="powder blue",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text=".",bg="powder blue", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="/",bg="powder blue", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)
status = Label(f2,font=('aria', 15, 'bold'),width = 16, text="-Thank You!!!",bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)

#---------------------------------------- Restaurant order screen -----------------------------------------------
Name=StringVar()
Phone=StringVar()
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblname = Label(f1, font=( 'aria' ,16, 'bold' ),text="Customer Name",fg="steel blue",bd=10,anchor='w')
lblname.grid(row=0,column=0)
lblname = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Name , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
lblname.grid(row=0,column=1)


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=1,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtreference.grid(row=1,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries",fg="steel blue",bd=10,anchor='w')
lblfries.grid(row=2,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=2,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Large Fries",fg="steel blue",bd=10,anchor='w')
lblLargefries.grid(row=3,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=3,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger",fg="steel blue",bd=10,anchor='w')
lblburger.grid(row=4,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtburger.grid(row=4,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza",fg="steel blue",bd=10,anchor='w')
lblFilet.grid(row=5,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtFilet.grid(row=5,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese Burger",fg="steel blue",bd=10,anchor='w')
lblCheese_burger.grid(row=6,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=6,column=1)

#--------------------------------------------------------------------------------------
lblph = Label(f1, font=( 'aria' ,16, 'bold' ),text="Phone No.",fg="steel blue",bd=10,anchor='w')
lblph.grid(row=0,column=2)
lblph = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Phone , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
lblph.grid(row=0,column=3)

lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')
lblDrinks.grid(row=1,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=1,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="steel blue",bd=10,anchor='w')
lblcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=2,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w')
lblService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=3,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="GST",fg="steel blue",bd=10,anchor='w')
lblTax.grid(row=4,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=4,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10,anchor='w')
lblSubtotal.grid(row=5,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtSubtotal.grid(row=5,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
lblTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=6,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=7,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('Helvetica' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=8, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('Helvetica' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=8, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('Helvetica' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=8, column=3)
lblemp = Label(f1,text="---------------------",fg="white")
lblemp.grid(row=9,column=3)
btnreceipt=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('Helvetica' ,16,'bold'),width=10, text="RECEIPT", bg="powder blue",command=Receipt_generate)
btnreceipt.grid(row=10, columnspan=4)


### -----------     PRICE LIST WINDOW ------------------------------------------------------------------------------
def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Large Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="80", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="220", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="80", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="70", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('Helvetica' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
btnprice.grid(row=8, column=0)

root.mainloop()

