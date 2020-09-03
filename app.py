import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import date

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.place(relx = 0.5, rely = 0.5, anchor=CENTER)
        self.createWidgets()

    # def get_date_format(self):
    #     today = str(date.today())
    #     for _ in range(2):
    #         print("x")
    #         today = today.replace("/", "")
    #     return today

    def show_codes(self):
        msg = messagebox.showinfo("Currency Codes", """
        01	דולר​	ארצות הברית​
        02​	לירה​	בריטניה​
        03​	כתר​	שוודיה​
        05​	פרנק​	שוויץ​
        06​	דולר​	קנדה​
        12​	כתר​	דנמרק​
        17​	רנד​	דרום אפריקה​
        18​	דולר​	אוסטרליה​
        27​	אירו​	האיחוד המוניטרי האירופי​
        28​	כתר​	נורווגיה​
        31​	יין​	יפן​
        69​	דינר​	ירדן (שטרי כסף)​
        70​	לירה​	לבנון (שטרי כסף)​
        79​	לירה​	מצרים (שטרי כסף)
        """)

    def createWidgets(self):
        # -= Currency Code Row =-
        c_code_text = Label(self.master, text="Currency Code ", font=("Fixedsys", 16))
        c_code_text.place(relx = 0.4, rely = 0.4, anchor=CENTER)

        c_code_val = tk.StringVar()
        c_code = Entry(self.master, width=15, textvariable = c_code_val, font=("fixedsys", 12))
        c_code.insert(0, "01")
        c_code.place(relx = 0.55, rely = 0.4, anchor=CENTER)

        dict_btn = Button(self.master, text="?", font=("Fixedsys", 12), command = self.show_codes)
        dict_btn.place(relx = 0.65, rely = 0.4, anchor=CENTER)
    
        # -= Date of Currency Row =-
        date_text = Label(self.master, text="Date ", font=("Fixedsys", 16))
        date_text.place(relx = 0.4, rely = 0.45, anchor=CENTER)

        date_entry_val = tk.StringVar()
        date_entry = Entry(self.master, width=15, textvariable = date_entry_val, font=("fixedsys", 12))
        date_entry.insert(0, "DD/MM/YYYY")
        date_entry.place(relx = 0.55, rely = 0.45, anchor=CENTER)
        
        example_text = Label(self.master, text="i.e. 30/11/2005", font=("Fixedsys", 16))
        example_text.place(relx = 0.72, rely = 0.45, anchor=CENTER)

        # -= Search Button =-
        search_btn = Button(self.master, text="Search", font=("Fixedsys", 12))
        search_btn.place(relx = 0.55, rely = 0.50, anchor=CENTER)
        
# WINDOW LOOP START
root = Tk()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

width = 800
height = 600

x = (ws/2) - (width/2)
y = (hs/2) - (height/2)

app = Application(master=root)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.title("Currency API")

app.mainloop()
# WINDOW LOOP END
root.destroy()
