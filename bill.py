from ast import Delete
from lib2to3.pgen2.token import GREATER
from tkinter import*
import math, random, os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title("Billing Software")
        bg_color="#000032"
        title=Label(self.root,bd=12, relief=FLAT, text="Billing Software", bg=bg_color, fg="white", font=("times new roman", 20, "bold"), pady=2).pack(fill=X)

        #========= Variables ========
            #===== Dairy ======
        self.milk=IntVar()
        self.butter=IntVar()
        self.cream_cheese=IntVar()
        self.yogurt=IntVar()
        self.sour_cream=IntVar()
        self.ice_cream=IntVar()
            #==== Beverage ======
        self.water=IntVar()
        self.juice=IntVar()
        self.soda=IntVar()
        self.coffee=IntVar()
        self.tea=IntVar()
        self.beer=IntVar()
            #==== Snacks ======
        self.cookies=IntVar()
        self.chips=IntVar()
        self.dip=IntVar()
        self.candy=IntVar()
        self.nuts=IntVar()
        self.popcorn=IntVar()
        #==== Total Product price & tax Variable ======
        self.dairy_price=StringVar()
        self.beverage_price=StringVar()
        self.snacks_price=StringVar()

        self.dairy_tax=StringVar()
        self.beverage_tax=StringVar()
        self.snacks_tax=StringVar()

        #===== customer variable========
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()


        #========= Customer Detail Frame ========
        F1=LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F1.place(x=0, y=55,relwidth=1)

        cname_lbl=Label(F1, text="Customer Name",bg=bg_color, fg= "white" ,font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=5, pady=5)
        cname_txt=Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=FLAT).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl=Label(F1, text="Phone number",bg=bg_color, fg= "white" ,font=("times new roman", 16, "bold")).grid(row=0, column=2, padx=5, pady=5)
        cphn_txt=Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=FLAT).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl=Label(F1, text="Bill Number",bg=bg_color, fg= "white" ,font=("times new roman", 16, "bold")).grid(row=0, column=4, padx=5, pady=5)
        c_bill_txt=Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=FLAT).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="Search", command=self.find_bill, width=10, bd=7, font="arial 12 bold", relief=FLAT).grid(row=0,column=6, pady=10, padx=30)


        #===========Dairy Frame=============
        F2=LabelFrame(self.root, bd=10, relief=GROOVE, text="Dairy", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F2.place(x=0, y=153,width=325, height=360)

        Milk_lbl=Label(F2, text="Milk", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        Milk_txt=Entry(F2, width=10, textvariable=self.milk, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=0, column=1, padx=10, pady=10)

        Butter_lbl=Label(F2, text="Butter", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Butter_txt=Entry(F2, width=10, textvariable=self.butter, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=1, column=1, padx=10, pady=10)

        Cream_Cheese_lbl=Label(F2, text="Cream Cheese", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Cream_Cheese_txt=Entry(F2, width=10, textvariable=self.cream_cheese, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=2, column=1, padx=10, pady=10)

        Yogurt_lbl=Label(F2, text="Yogurt", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Yogurt_txt=Entry(F2, width=10, textvariable=self.yogurt, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=3, column=1, padx=10, pady=10)

        Sour_Cream_lbl=Label(F2, text="Sour Cream", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Sour_Cream_txt=Entry(F2, width=10, textvariable=self.sour_cream, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=4, column=1, padx=10, pady=10)

        Ice_Cream_lbl=Label(F2, text="Ice Cream", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Ice_Cream_txt=Entry(F2, width=10, textvariable=self.ice_cream, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=5, column=1, padx=10, pady=10)


        #===========Beverages Frame=============
        F3=LabelFrame(self.root, bd=10, relief=GROOVE, text="Beverage", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F3.place(x=325, y=153,width=325, height=360)

        B1_lbl=Label(F3, text="Water", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        B1_txt=Entry(F3, width=10, textvariable=self.water, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=0, column=1, padx=10, pady=10)

        B2_lbl=Label(F3, text="Juice", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        B2_txt=Entry(F3, width=10, textvariable=self.juice, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=1, column=1, padx=10, pady=10)

        B3_lbl=Label(F3, text="Soda", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        B3_txt=Entry(F3, width=10, textvariable=self.soda, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=2, column=1, padx=10, pady=10)

        B4_lbl=Label(F3, text="Coffee", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        B4_txt=Entry(F3, width=10, textvariable=self.coffee, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=3, column=1, padx=10, pady=10)

        B5_lbl=Label(F3, text="Tea", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        B5_txt=Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=4, column=1, padx=10, pady=10)

        B6_lbl=Label(F3, text="Beer", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        B6_txt=Entry(F3, width=10, textvariable=self.beer, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=5, column=1, padx=10, pady=10)


        #===========Snacks Frame=============
        F4=LabelFrame(self.root, bd=10, relief=GROOVE, text="Snacks", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=650, y=153,width=325, height=360)

        C1_lbl=Label(F4, text="Cookies", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        C1_txt=Entry(F4, width=10, textvariable=self.cookies, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=0, column=1, padx=10, pady=10)

        C2_lbl=Label(F4, text="Chips", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        C2_txt=Entry(F4, width=10, textvariable=self.chips, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=1, column=1, padx=10, pady=10)

        C3_lbl=Label(F4, text="Dip", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        C3_txt=Entry(F4, width=10, textvariable=self.dip, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=2, column=1, padx=10, pady=10)

        C4_lbl=Label(F4, text="Candy", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        C4_txt=Entry(F4, width=10, textvariable=self.candy, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=3, column=1, padx=10, pady=10)

        C5_lbl=Label(F4, text="Nuts", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        C5_txt=Entry(F4, width=10, textvariable=self.nuts, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=4, column=1, padx=10, pady=10)

        C6_lbl=Label(F4, text="Popcorn", font=("times new roman", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        C6_txt=Entry(F4, width=10, textvariable=self.popcorn, font=("times new roman", 14, "bold"), bd=5, relief=FLAT).grid(row=5, column=1, padx=10, pady=10)


        #===========Bill Area=============
        F5=Frame(self.root, bd=10, relief=FLAT)
        F5.place(x=980, y=153,width=295, height=360)
        bill_title=Label(F5, text="Bill Area", font="arial 13 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5, orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #======Button Frame=======
        F6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F6.place(x=0, y=513, relwidth=1, height=140)

        m1_lbl=Label(F6, text="Total Dairy Price",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt=Entry(F6, width=18, textvariable=self.dairy_price, font="arial 10 bold", bd=7, relief=FLAT).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl=Label(F6, text="Total Beverage Price",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt=Entry(F6, width=18, textvariable=self.beverage_price, font="arial 10 bold", bd=7, relief=FLAT).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl=Label(F6, text="Total Snacks Price",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt=Entry(F6, width=18, textvariable=self.snacks_price, font="arial 10 bold", bd=7, relief=FLAT).grid(row=2, column=1, padx=10, pady=1)

        n1_lbl=Label(F6, text="Dairy Tax",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        n1_txt=Entry(F6, width=18, textvariable=self.dairy_tax, font="arial 10 bold", bd=7, relief=FLAT).grid(row=0, column=3, padx=10, pady=1)

        n2_lbl=Label(F6, text="Beverage Tax",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        n2_txt=Entry(F6, width=18, textvariable=self.beverage_tax, font="arial 10 bold", bd=7, relief=FLAT).grid(row=1, column=3, padx=10, pady=1)

        n3_lbl=Label(F6, text="Snacks Tax",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        n3_txt=Entry(F6, width=18, textvariable=self.snacks_tax, font="arial 10 bold", bd=7, relief=FLAT).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6, bd=7, bg=bg_color, relief=FLAT)
        btn_F.place(x=700, width=555, height=100)

        total_btn=Button(btn_F,command=self.total, text="Total",width=11, bd=5,font="arial 13 bold", bg="#fac830", fg="Black", pady=10).grid(row=0, column=0, padx=5, pady =5)
        Gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area ,width=11, bd=5,font="arial 13 bold", bg="#fac830", fg="Black", pady=10).grid(row=0, column=1, padx=5, pady =5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data, width=11, bd=5,font="arial 13 bold", bg="#fac830", fg="Black", pady=10).grid(row=0, column=2, padx=5, pady =5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app, width=11, bd=5,font="arial 13 bold", bg="#fac830", fg="Black", pady=10).grid(row=0, column=3, padx=5, pady =5)
        #self.welcome_bill()

    def total(self):
        self.dmp=self.milk.get()*50
        self.dbp=self.butter.get()*80
        self.dccp=self.cream_cheese.get()*80
        self.dyp=self.yogurt.get()*120
        self.dscp=self.sour_cream.get()*120
        self.dicp=self.ice_cream.get()*60
        
        self.total_dairy_price=float(
                                self.dmp+
                                self.dbp+
                                self.dccp+
                                self.dyp+
                                self.dscp+
                                self.dicp
                                )
        self.dairy_price.set("Rs. "+ str(self.total_dairy_price))
        self.d_tax=round((self.total_dairy_price*0.03), 2)
        self.dairy_tax.set("Rs. " + str(self.d_tax))

        self.bwp=self.water.get()*40
        self.bjp=self.juice.get()*60
        self.bsp=self.soda.get()*60
        self.bcp=self.coffee.get()*120
        self.btp=self.tea.get()*40
        self.bbp=self.beer.get()*200
        
        self.total_beverage_price=float(
                                self.bwp+
                                self.bjp+
                                self.bsp+
                                self.bcp+
                                self.btp+
                                self.bbp
                                )
        self.beverage_price.set("Rs. "+ str(self.total_beverage_price))
        self.b_tax=round((self.total_beverage_price*0.03), 2)
        self.beverage_tax.set("Rs. " + str(self.b_tax))

        self.scop=self.cookies.get()*80
        self.schp=self.chips.get()*20
        self.sdp=self.dip.get()*40
        self.scap=self.candy.get()*60
        self.snp=self.nuts.get()*120
        self.spp=self.popcorn.get()*60
        
        self.total_snacks_price=float(
                                self.scop+
                                self.schp+
                                self.sdp+
                                self.scap+
                                self.snp+
                                self.spp
                                )
        self.snacks_price.set("Rs. "+ str(self.total_snacks_price))
        self.s_tax=round((self.total_snacks_price*0.03), 2)
        self.snacks_tax.set("Rs. " + str(self.s_tax))

        self.Total_bill=float(  self.total_dairy_price+
                                self.total_beverage_price+
                                self.total_snacks_price+
                                self.d_tax+
                                self.b_tax+
                                self.s_tax
                                )
        

    def welcome_bill(self):
        self.txtarea.insert(END,"\t     welcome")
        self.txtarea.insert(END,f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n===============================")
        self.txtarea.insert(END,f"\nProducts\t      QTY\t       Price")
        self.txtarea.insert(END,f"\n===============================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.dairy_price.get()=="Rs. 0.0" and self.beverage_price.get()=="Rs. 0.0" and self.snacks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product purchased")
        else:
            self.welcome_bill()
            #======dairy======
            if self.milk.get()!=0:
                self.txtarea.insert(END,f"\n Milk\t\t{self.milk.get()}\t  {self.dmp}")
            if self.butter.get()!=0:
                self.txtarea.insert(END,f"\n Butter\t\t{self.butter.get()}\t  {self.dbp}")
            if self.cream_cheese.get()!=0:
                self.txtarea.insert(END,f"\n Cream Cheese\t\t{self.cream_cheese.get()}\t  {self.dccp}")
            if self.yogurt.get()!=0:
                self.txtarea.insert(END,f"\n Yogurt\t\t{self.yogurt.get()}\t  {self.dyp}")
            if self.sour_cream.get()!=0:
                self.txtarea.insert(END,f"\n Sour Cream\t\t{self.sour_cream.get()}\t  {self.dscp}")
            if self.ice_cream.get()!=0:
                self.txtarea.insert(END,f"\n Ice Cream\t\t{self.ice_cream.get()}\t  {self.dicp}")
            
            #======beverage======
            if self.water.get()!=0:
                self.txtarea.insert(END,f"\n Water\t\t{self.water.get()}\t  {self.bwp}")
            if self.juice.get()!=0:
                self.txtarea.insert(END,f"\n Juice\t\t{self.juice.get()}\t  {self.bjp}")
            if self.soda.get()!=0:
                self.txtarea.insert(END,f"\n Soda\t\t{self.soda.get()}\t  {self.bsp}")
            if self.coffee.get()!=0:
                self.txtarea.insert(END,f"\n Coffee\t\t{self.coffee.get()}\t  {self.bcp}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t  {self.btp}")
            if self.beer.get()!=0:
                self.txtarea.insert(END,f"\n Beer\t\t{self.beer.get()}\t  {self.bbp}")

            #======snacks======
            if self.cookies.get()!=0:
                self.txtarea.insert(END,f"\n Cookies\t\t{self.cookies.get()}\t  {self.scop}")
            if self.chips.get()!=0:
                self.txtarea.insert(END,f"\n Chips\t\t{self.chips.get()}\t  {self.schp}")
            if self.dip.get()!=0:
                self.txtarea.insert(END,f"\n Dip\t\t{self.dip.get()}\t  {self.sdp}")
            if self.candy.get()!=0:
                self.txtarea.insert(END,f"\n Candy\t\t{self.candy.get()}\t  {self.scap}")
            if self.nuts.get()!=0:
                self.txtarea.insert(END,f"\n Nuts\t\t{self.nuts.get()}\t  {self.snp}")
            if self.popcorn.get()!=0:
                self.txtarea.insert(END,f"\n Popcorn\t\t{self.popcorn.get()}\t  {self.spp}")

            self.txtarea.insert(END,f"\n-------------------------------")
            if self.dairy_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nDairy Tax\t\t    {self.dairy_tax.get()}")
            if self.beverage_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nBeverage Tax\t\t    {self.beverage_tax.get()}")
            if self.snacks_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nSnacks Tax\t\t    {self.snacks_tax.get()}")
            
            self.txtarea.insert(END,f"\nTotal Bill:\t        Rs. {str(round((self.Total_bill), 2))}")
            self.txtarea.insert(END,f"\n-------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txr","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()}  saved successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill number")

    def clear_data(self):
        op=messagebox.askyesno("Exit","Do you really want to clear data")
        if op>0:
                #===== Dairy ======
            self.milk.set(0)
            self.butter.set(0)
            self.cream_cheese.set(0)
            self.yogurt.set(0)
            self.sour_cream.set(0)
            self.ice_cream.set(0)
                #==== Beverage ======
            self.water.set(0)
            self.juice.set(0)
            self.soda.set(0)
            self.coffee.set(0)
            self.tea.set(0)
            self.beer.set(0)
                #==== Snacks ======
            self.cookies.set(0)
            self.chips.set(0)
            self.dip.set(0)
            self.candy.set(0)
            self.nuts.set(0)
            self.popcorn.set(0)
            #==== Total Product price & tax Variable ======
            self.dairy_price.set("")
            self.beverage_price.set("")
            self.snacks_price.set("")

            self.dairy_tax.set("")
            self.beverage_tax.set("")
            self.snacks_tax.set("")

            #===== customer variable========
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit")
        if op>0:
            self.root.destroy()


root=Tk()
obj = Bill_App(root)
root.mainloop()
