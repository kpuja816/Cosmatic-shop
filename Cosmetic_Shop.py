# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:19:02 2021

@author: pooja bca
"""

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

import time
import datetime
import random
#import tkMessageBox

root =Tk()
root.geometry("1350x750+0+0")

root.title("COSMETIC SHOP")
root.configure(background='firebrick')

Tops = Frame(root,bg='firebrick',bd=20,pady=5,relief=RAISED)
Tops.pack(side=TOP,fill=X, expand=YES)

img1 = Image.open("make1.jpg")
img = ImageTk.PhotoImage(img1)
photo2 = Label(Tops,image=img,width=200,height=140)
photo2.grid(row=0,column=0)

lblTitle=Label(Tops,font=('arial',60,'bold'),text='         COSMETIC SHOP         ',bd=10,padx=10,bg='indianred',fg='darkgreen',justify=CENTER)
lblTitle.grid(row=0,column=1)
############################images#########
''''
Tops1 = Frame(root,bg='lightyellow',bd=10,pady=2,relief=RAISED)
Tops1.pack(side=TOP,fill=X, expand=YES)



img2 = Image.open("body.jpg")
img = ImageTk.PhotoImage(img2)
photo3 = Label(Tops1,image=img,width=200)
photo3.pack( side = LEFT)
'''

######################

ReceiptCal_F = Frame(root,bg='indianred',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='indianred',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='indianred',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)


Receipt_F=Frame(ReceiptCal_F,bg='indianred',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)




MenuFrame = Frame(root,bg='indianred',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='indianred',bd=4)
Cost_F.pack(side=BOTTOM)
skin_care_F=Frame(MenuFrame,bg='indianred',bd=4)
skin_care_F.pack(side=TOP)


skin_care_F=Frame(MenuFrame,bg='indianred',bd=4,relief=RIDGE)
skin_care_F.pack(side=LEFT)
Make_up_kit_F=Frame(MenuFrame,bg='indianred',bd=4,relief=RIDGE)
Make_up_kit_F.pack(side=RIGHT)
###################################################variables################################################

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofMake_up_kit = StringVar()
Costofskin_care = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Organic_Indigo_Powder = StringVar()
E_Silk_Body_Cream = StringVar()
E_Facial_Tonic = StringVar()
E_The_Body_Shop = StringVar()
E_Tea_Tree_Oil = StringVar()
E_Hair_Cleanser = StringVar()
E_Henna_Powder = StringVar()
E_Shower_Cream = StringVar()

E_Foundation_Makeup_Brush = StringVar()
E_Cosmetic_Combo_Kit = StringVar()
E_Lipbalm = StringVar()
E_Face_Glow_Make_Up_Kit = StringVar()
E_Elle_18_Colleg_Ready = StringVar()
E_Oil_Free_Foundation = StringVar()
E_Wedding_Make_Up_Kit = StringVar()
E_Maybelline_Make_Up_Kit = StringVar()

E_Organic_Indigo_Powder.set("0")
E_Silk_Body_Cream.set("0")
E_Facial_Tonic.set("0")
E_The_Body_Shop.set("0")
E_Tea_Tree_Oil.set("0")
E_Hair_Cleanser.set("0")
E_Henna_Powder.set("0")
E_Shower_Cream.set("0")

E_Foundation_Makeup_Brush.set("0")
E_Cosmetic_Combo_Kit.set("0")
E_Lipbalm.set("0")
E_Face_Glow_Make_Up_Kit.set("0")
E_Elle_18_Colleg_Ready.set("0")
E_Oil_Free_Foundation.set("0")
E_Wedding_Make_Up_Kit.set("0")
E_Maybelline_Make_Up_Kit.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

#############z#############################Function Declaration####################################################

def iExit():
    iExit=messagebox.askyesno("Exit Cosmetic Shop","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofMake_up_kit.set("")
    Costofskin_care.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


    E_Organic_Indigo_Powder.set("0")
    E_Silk_Body_Cream.set("0")
    E_Facial_Tonic.set("0")
    E_The_Body_Shop.set("0")
    E_Tea_Tree_Oil.set("0")
    E_Hair_Cleanser.set("0")
    E_Henna_Powder.set("0")
    E_Shower_Cream.set("0")

    E_Foundation_Makeup_Brush.set("0")
    E_Cosmetic_Combo_Kit.set("0")
    E_Lipbalm.set("0")
    E_Face_Glow_Make_Up_Kit.set("0")
    E_Elle_18_Colleg_Ready.set("0")
    E_Oil_Free_Foundation.set("0")
    E_Wedding_Make_Up_Kit.set("0")
    E_Maybelline_Make_Up_Kit.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtOrganic_Indigo_Powder.configure(state=DISABLED)
    txtSilk_Body_Cream.configure(state=DISABLED)
    txtFacial_Tonic.configure(state=DISABLED)
    txtThe_Body_Shop.configure(state=DISABLED)
    txtTea_Tree_Oil.configure(state=DISABLED)
    txtHair_Cleanser.configure(state=DISABLED)
    txtHenna_Powder.configure(state=DISABLED)
    txtShower_Cream.configure(state=DISABLED)
    txtFoundation_Makeup_Brush.configure(state=DISABLED)
    txtCosmetic_Combo_Kit.configure(state=DISABLED)
    txtLipbalm.configure(state=DISABLED)
    txtFace_Glow_Make_Up_Kit.configure(state=DISABLED)
    txtElle_18_Colleg_Ready.configure(state=DISABLED)
    txtOil_Free_Foundation.configure(state=DISABLED)
    txtWedding_Make_Up_Kit.configure(state=DISABLED)
    txtMaybelline_Make_Up_Kit.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Organic_Indigo_Powder.get())
    Item2=float(E_Silk_Body_Cream.get())
    Item3=float(E_Facial_Tonic.get())
    Item4=float(E_The_Body_Shop.get())
    Item5=float(E_Tea_Tree_Oil.get())
    Item6=float(E_Hair_Cleanser.get())
    Item7=float(E_Henna_Powder.get())
    Item8=float(E_Shower_Cream.get())

    Item9=float(E_Foundation_Makeup_Brush.get())
    Item10=float(E_Cosmetic_Combo_Kit.get())
    Item11=float(E_Lipbalm.get())
    Item12=float(E_Face_Glow_Make_Up_Kit.get())
    Item13=float(E_Elle_18_Colleg_Ready.get())
    Item14=float(E_Oil_Free_Foundation.get())
    Item15=float(E_Wedding_Make_Up_Kit.get())
    Item16=float(E_Maybelline_Make_Up_Kit.get())

    Priceofskin_care =(Item1 * 70) + (Item2 * 75) + (Item3 * 99) + (Item4 * 60) + (Item5 * 160) + (Item6 * 75) + (Item7 * 75) + (Item8 * 340)

    PriceofMake_up_kit =(Item9 * 143) + (Item10 * 120) + (Item11 * 40) + (Item12 * 290) + (Item13 * 190) + (Item14 * 110) + (Item15 * 270) + (Item16 * 135)

    skin_carePrice = "Rs",str('%.2f'%(Priceofskin_care))
    Make_up_kitPrice =  "Rs",str('%.2f'%(PriceofMake_up_kit))
    CostofMake_up_kit.set(Make_up_kitPrice)
    Costofskin_care.set(skin_carePrice)
    SC = "Rs",str('%.2f'%(2.11))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Rs",str('%.2f'%(Priceofskin_care + PriceofMake_up_kit + 2.11))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs",str('%.2f'%((Priceofskin_care + PriceofMake_up_kit + 2.11) * 0.18))
    PaidTax.set(Tax)

    TT=((Priceofskin_care + PriceofMake_up_kit + 2.11) * 0.18)
    TC="Rs",str('%.2f'%(Priceofskin_care + PriceofMake_up_kit + 2.11 + TT))
    TotalCost.set(TC)


def chkOrganic_Indigo_Powder():
    if(var1.get() == 1):
        txtOrganic_Indigo_Powder.configure(state = NORMAL)
        txtOrganic_Indigo_Powder.focus()
        txtOrganic_Indigo_Powder.delete('0',END)
        E_Organic_Indigo_Powder.set("")
    elif(var1.get() == 0):
        txtOrganic_Indigo_Powder.configure(state = DISABLED)
        E_Organic_Indigo_Powder.set("0")

def chkSilk_Body_Cream():
    if(var2.get() == 1):
        txtSilk_Body_Cream.configure(state = NORMAL)
        txtSilk_Body_Cream.focus()
        txtSilk_Body_Cream.delete('0',END)
        E_Silk_Body_Cream.set("")
    elif(var2.get() == 0):
        txtSilk_Body_Cream.configure(state = DISABLED)
        E_Silk_Body_Cream.set("0")

def chk_Facial_Tonic():
    if(var3.get() == 1):
        txtFacial_Tonic.configure(state = NORMAL)
        txtFacial_Tonic.delete('0',END)
        txtFacial_Tonic.focus()
    elif(var3.get() == 0):
        txtFacial_Tonic.configure(state = DISABLED)
        E_Facial_Tonic.set("0")

def chk_The_Body_Shop():
    if(var4.get() == 1):
        txtThe_Body_Shop.configure(state = NORMAL)
        txtThe_Body_Shop.delete('0',END)
        txtThe_Body_Shop.focus()
    elif(var4.get() == 0):
        txtThe_Body_Shop.configure(state = DISABLED)
        E_The_Body_Shop.set("0")

def chk_Tea_Tree_Oil():
    if(var5.get() == 1):
        txtTea_Tree_Oil.configure(state = NORMAL)
        txtTea_Tree_Oil.delete('0',END)
        txtTea_Tree_Oil.focus()
    elif(var5.get() == 0):
        txtTea_Tree_Oil.configure(state = DISABLED)
        E_Tea_Tree_Oil.set("0")

def chk_Hair_Cleanser():
    if(var6.get() == 1):
        txtHair_Cleanser.configure(state = NORMAL)
        txtHair_Cleanser.delete('0',END)
        txtHair_Cleanser.focus()
    elif(var6.get() == 0):
        txtHair_Cleanser.configure(state = DISABLED)
        E_Hair_Cleanser.set("0")

def chk_Henna_Powder():
    if(var7.get() == 1):
        txtHenna_Powder.configure(state = NORMAL)
        txtHenna_Powder.delete('0',END)
        txtHenna_Powder.focus()
    elif(var7.get() == 0):
        txtHenna_Powder.configure(state = DISABLED)
        E_Henna_Powder.set("0")

def chk_Shower_Cream():
    if(var8.get() == 1):
        txtShower_Cream.configure(state = NORMAL)
        txtShower_Cream.delete('0',END)
        txtShower_Cream.focus()
    elif(var8.get() == 0):
        txtShower_Cream.configure(state = DISABLED)
        E_Shower_Cream.set("0")

def chk_Foundation_Makeup_Brush():
    if(var9.get() == 1):
        txtFoundation_Makeup_Brush.configure(state = NORMAL)
        txtFoundation_Makeup_Brush.delete('0',END)
        txtFoundation_Makeup_Brush.focus()
    elif(var9.get() == 0):
        txtFoundation_Makeup_Brush.configure(state = DISABLED)
        E_Foundation_Makeup_Brush.set("0")

def chk_Cosmetic_Combo_Kit():
    if(var10.get() == 1):
        txtCosmetic_Combo_Kit.configure(state = NORMAL)
        txtCosmetic_Combo_Kit.delete('0',END)
        txtCosmetic_Combo_Kit.focus()
    elif(var10.get() == 0):
        txtCosmetic_Combo_Kit.configure(state = DISABLED)
        E_Cosmetic_Combo_Kit.set("0")

def chk_Lipbalm():
    if(var11.get() == 1):
        txtLipbalm.configure(state = NORMAL)
        txtLipbalm.delete('0',END)
        txtLipbalm.focus()
    elif(var11.get() == 0):
        txtLipbalm.configure(state = DISABLED)
        E_Lipbalm.set("0")

def chk_Face_Glow_Make_Up_Kit():
    if(var12.get() == 1):
        txtFace_Glow_Make_Up_Kit.configure(state = NORMAL)
        txtFace_Glow_Make_Up_Kit.delete('0',END)
        txtFace_Glow_Make_Up_Kit.focus()
    elif(var12.get() == 0):
        txtFace_Glow_Make_Up_Kit.configure(state = DISABLED)
        E_Face_Glow_Make_Up_Kit.set("0")

def chk_Elle_18_Colleg_Ready():
    if(var13.get() == 1):
        txtElle_18_Colleg_Ready.configure(state = NORMAL)
        txtElle_18_Colleg_Ready.delete('0',END)
        txtElle_18_Colleg_Ready.focus()
    elif(var13.get() == 0):
        txtElle_18_Colleg_Ready.configure(state = DISABLED)
        E_Elle_18_Colleg_Ready.set("0")

def chk_Oil_Free_Foundation():
    if(var14.get() == 1):
        txtOil_Free_Foundation.configure(state = NORMAL)
        txtOil_Free_Foundation.delete('0',END)
        txtOil_Free_Foundation.focus()
    elif(var14.get() == 0):
        txtOil_Free_Foundation.configure(state = DISABLED)
        E_Oil_Free_Foundation.set("0")

def chk_Wedding_Make_Up_Kit():
    if(var15.get() == 1):
        txtWedding_Make_Up_Kit.configure(state = NORMAL)
        txtWedding_Make_Up_Kit.delete('0',END)
        txtWedding_Make_Up_Kit.focus()
    elif(var15.get() == 0):
        txtWedding_Make_Up_Kit.configure(state = DISABLED)
        E_Wedding_Make_Up_Kit.set("0")

def chk_Maybelline_Make_Up_Kit():
    if(var16.get() == 1):
        txtMaybelline_Make_Up_Kit.configure(state = NORMAL)
        txtMaybelline_Make_Up_Kit.delete('0',END)
        txtMaybelline_Make_Up_Kit.focus()
    elif(var16.get() == 0):
        txtMaybelline_Make_Up_Kit.configure(state = DISABLED)
        E_Maybelline_Make_Up_Kit.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)


    txtReceipt.insert(END,'Receipt Ref:   \t'+Receipt_Ref.get() +'\t\t\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'Organic_Indigo_Powder:\t\t\t\t\t' + E_Organic_Indigo_Powder.get() +'\n')
    txtReceipt.insert(END,'Silk_Body_Cream:\t\t\t\t\t'+ E_Silk_Body_Cream.get()+'\n')
    txtReceipt.insert(END,'Facial_Tonic:\t\t\t\t\t'+ E_Facial_Tonic.get()+'\n')
    txtReceipt.insert(END,'The_Body_Shop:\t\t\t\t\t'+ E_The_Body_Shop.get()+'\n')
    txtReceipt.insert(END,'Tea_Tree_Oil:\t\t\t\t\t'+ E_Tea_Tree_Oil.get()+'\n')
    txtReceipt.insert(END,'Hair_Cleanser:\t\t\t\t\t'+ E_Hair_Cleanser.get()+'\n')
    txtReceipt.insert(END,'Henna_Powder:\t\t\t\t\t'+ E_Henna_Powder.get()+'\n')
    txtReceipt.insert(END,'Shower_Cream:\t\t\t\t\t'+ E_Shower_Cream.get()+'\n')
    txtReceipt.insert(END,'Foundation Makeup Brush:\t\t\t\t\t'+ E_Foundation_Makeup_Brush.get()+'\n')
    txtReceipt.insert(END,'Cosmetic_Combo_Kit:\t\t\t\t\t'+ E_Cosmetic_Combo_Kit.get()+'\n')
    txtReceipt.insert(END,'Lipbalm:\t\t\t\t\t'+ E_Lipbalm.get()+'\n')
    txtReceipt.insert(END,'Face_Glow_Make_Up_Kit:\t\t\t\t\t'+ E_Face_Glow_Make_Up_Kit.get()+'\n')
    txtReceipt.insert(END,'Elle_18_Colleg_Ready:\t\t\t\t\t'+ E_Elle_18_Colleg_Ready.get()+'\n')
    txtReceipt.insert(END,'Oil_Free_Foundation:\t\t\t\t\t'+ E_Oil_Free_Foundation.get()+'\n')
    txtReceipt.insert(END,'Wedding_Make_Up_Kit:\t\t\t\t\t'+ E_Wedding_Make_Up_Kit.get()+'\n')
    txtReceipt.insert(END,'Maybelline_Make_Up_Kit:\t\t\t\t\t'+ E_Maybelline_Make_Up_Kit.get()+'\n')
    txtReceipt.insert(END,'Cost of skin_care:\t\t\t\t'+ Costofskin_care.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Make_up_kits:\t\t\t\t'+ CostofMake_up_kit.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")

    

#########################################Skin Care####################################################################

Organic_Indigo_Powder=Checkbutton(skin_care_F,text='Organic Indigo Powder',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='indianred',command=chkOrganic_Indigo_Powder).grid(row=0,sticky=W)
Silk_Body_Cream=Checkbutton(skin_care_F,text='Silk Body Cream',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='indianred',command=chkSilk_Body_Cream).grid(row=1,sticky=W)
Facial_Tonic=Checkbutton(skin_care_F,text='Facial Tonic',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='indianred',command=chk_Facial_Tonic).grid(row=2,sticky=W)
The_Body_Shop=Checkbutton(skin_care_F,text='The Body Shop',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='indianred',command=chk_The_Body_Shop).grid(row=3,sticky=W)
Tea_Tree_Oil=Checkbutton(skin_care_F,text='Tea Tree Oil',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='indianred',command=chk_Tea_Tree_Oil).grid(row=4,sticky=W)
Hair_Cleanser=Checkbutton(skin_care_F,text='Hair Cleanser',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='indianred',command=chk_Hair_Cleanser).grid(row=5,sticky=W)
Henna_Powder=Checkbutton(skin_care_F,text='Henna Powder',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='indianred',command=chk_Henna_Powder).grid(row=6,sticky=W)
Shower_Cream=Checkbutton(skin_care_F,text='Shower Cream',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='indianred',command=chk_Shower_Cream).grid(row=7,sticky=W)
##############################################Drink Entry###############################################################

txtOrganic_Indigo_Powder = Entry(skin_care_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Organic_Indigo_Powder)
txtOrganic_Indigo_Powder.grid(row=0,column=1)

txtSilk_Body_Cream = Entry(skin_care_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Silk_Body_Cream)
txtSilk_Body_Cream.grid(row=1,column=1)

txtFacial_Tonic = Entry(skin_care_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Facial_Tonic)
txtFacial_Tonic.grid(row=2,column=1)

txtThe_Body_Shop= Entry(skin_care_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_The_Body_Shop)
txtThe_Body_Shop.grid(row=3,column=1)

txtTea_Tree_Oil = Entry(skin_care_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Tea_Tree_Oil)
txtTea_Tree_Oil.grid(row=4,column=1)

txtHair_Cleanser = Entry(skin_care_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Hair_Cleanser)
txtHair_Cleanser.grid(row=5,column=1)

txtHenna_Powder = Entry(skin_care_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Henna_Powder)
txtHenna_Powder.grid(row=6,column=1)

txtShower_Cream = Entry(skin_care_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Shower_Cream)
txtShower_Cream.grid(row=7,column=1)
#############################################MakeUp Kit######################################################################

Foundation_Makeup_Brush = Checkbutton(Make_up_kit_F,text="Foundation Makeup Brush Set",variable=var9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='indianred',command=chk_Foundation_Makeup_Brush).grid(row=0,sticky=W)
Cosmetic_Combo_Kit = Checkbutton(Make_up_kit_F,text="Cosmetic Combo Kit",variable=var10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='indianred',command=chk_Cosmetic_Combo_Kit).grid(row=1,sticky=W)
Lipbalm = Checkbutton(Make_up_kit_F,text="Lipbalm kit",variable=var11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='indianred',command=chk_Lipbalm).grid(row=2,sticky=W)
Face_Glow_Make_Up_Kit = Checkbutton(Make_up_kit_F,text="Face Glow Make Up Kit",variable=var12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='indianred',command=chk_Face_Glow_Make_Up_Kit).grid(row=3,sticky=W)
Elle_18_Colleg_Ready = Checkbutton(Make_up_kit_F,text="Elle 18 College Ready",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='indianred',command=chk_Elle_18_Colleg_Ready).grid(row=4,sticky=W)
Oil_Free_Foundation = Checkbutton(Make_up_kit_F,text="Oil Free Foundation ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='indianred',command=chk_Oil_Free_Foundation).grid(row=5,sticky=W)
Wedding_Make_Up_Kit = Checkbutton(Make_up_kit_F,text="Wedding Make Up Kit ",variable=var15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='indianred',command=chk_Wedding_Make_Up_Kit).grid(row=6,sticky=W)
Maybelline_Make_Up_Kit = Checkbutton(Make_up_kit_F,text="Maybelline Make Up Kit",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='indianred',command=chk_Maybelline_Make_Up_Kit).grid(row=7,sticky=W)
################################################Entry Box##########################################################
txtFoundation_Makeup_Brush=Entry(Make_up_kit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Foundation_Makeup_Brush)
txtFoundation_Makeup_Brush.grid(row=0,column=1)

txtCosmetic_Combo_Kit=Entry(Make_up_kit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Cosmetic_Combo_Kit)
txtCosmetic_Combo_Kit.grid(row=1,column=1)

txtLipbalm=Entry(Make_up_kit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Lipbalm)
txtLipbalm.grid(row=2,column=1)

txtFace_Glow_Make_Up_Kit=Entry(Make_up_kit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Face_Glow_Make_Up_Kit)
txtFace_Glow_Make_Up_Kit.grid(row=3,column=1)

txtElle_18_Colleg_Ready=Entry(Make_up_kit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Elle_18_Colleg_Ready)
txtElle_18_Colleg_Ready.grid(row=4,column=1)

txtOil_Free_Foundation=Entry(Make_up_kit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Oil_Free_Foundation)
txtOil_Free_Foundation.grid(row=5,column=1)

txtWedding_Make_Up_Kit=Entry(Make_up_kit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Wedding_Make_Up_Kit)
txtWedding_Make_Up_Kit.grid(row=6,column=1)

txtMaybelline_Make_Up_Kit=Entry(Make_up_kit_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Maybelline_Make_Up_Kit)
txtMaybelline_Make_Up_Kit.grid(row=7,column=1)
###########################################ToTal Cost################################################################################
lblCostofskin_care=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Skin care\t',bg='indianred',
                fg='black',justify=CENTER)
lblCostofskin_care.grid(row=0,column=0,sticky=W)
txtCostofskin_care=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=Costofskin_care,state=DISABLED)
txtCostofskin_care.grid(row=0,column=1)

lblCostofMake_up_kit=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Make Up Kit ',bg='indianred',
                fg='black',justify=CENTER)
lblCostofMake_up_kit.grid(row=1,column=0,sticky=W)
txtCostofMake_up_kit=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofMake_up_kit,state=DISABLED)
txtCostofMake_up_kit.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='indianred',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge,state=DISABLED)
txtServiceCharge.grid(row=2,column=1)
###########################################################Payment information###################################################

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='indianred',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax,state=DISABLED)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='indianred',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal,state=DISABLED)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='indianred',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost,state=DISABLED)
txtTotalCost.grid(row=2,column=3)

#############################################RECEIPT###############################################################################

txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
#txtReceipt=Entry(Receipt_F,state=DISABLED,width=46,bg='white',bd=4,font=('arial',12,'bold'))

txtReceipt.grid(row=0,column=0)


###########################################BUTTONS################################################################################
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='firebrick',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='firebrick',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='firebrick',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='firebrick',command=iExit).grid(row=0,column=3)

###################################Calculator Display################################################################################




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




#############################################Calculator###############################################################################

txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")


###########################################CALCULATOR BUTTONS################################################################################
btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='firebrick',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='firebrick',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='firebrick',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='firebrick',command=lambda:btnClick('+')).grid(row=2,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='firebrick',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='firebrick',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='firebrick',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='firebrick',command=lambda:btnClick('-')).grid(row=3,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='firebrick',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='firebrick',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='firebrick',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='firebrick',command=lambda:btnClick('*')).grid(row=4,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='firebrick',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='firebrick',command=btnClear).grid(row=5,column=1)
btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='firebrick',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='firebrick',command=lambda:btnClick('/')).grid(row=5,column=3)


root.mainloop()
