from cProfile import label
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import database



class GUI:
    def __init__(self, root, account):
        self.window = root
        self.window.title("3D Printer Machine Management Application")
        self.window.geometry("1920x1080")
        self.window.grid()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # This variable to open different accounts
        self.account = account

        # Variable
        self.name = StringVar()
        self.manufacturer = StringVar()
        self.model = StringVar()
        self.serial_num = StringVar()
        self.firmware_vers = StringVar()
        self.calibration =  StringVar()
        self.printing_status = StringVar()

        self.menu_frame = Frame(self.window, bg="#e5e5e5")
        self.menu_frame.place(x=0, y=0, width=400, height=1080, relwidth=1, relheight=1)
        

        self.manage_frame = Frame(self.window, bg="#f2f2f2")
        self.manage_frame.place(x=400, y=0, relwidth=1, relheight=1)
        
        self.printing_frame = Frame(self.window, bg="#f2f2f2")
        
        

        
        # Button and text in the menu frame
        Label(self.menu_frame, text="Options", highlightthickness=0, bg="#e5e5e5", font=('Helvetica', 40,'bold')).place(x=50, y=100)
        self.manage = Button(self.menu_frame, text="Manage", highlightthickness=0, bg="#e5e5e5", command=self.open_manage_frame, bd=0, font=('Helvetica', 25,'bold')).place(x=0, y=250, width=400, height=75)
        self.printing = Button(self.menu_frame, text="Printing", highlightthickness=0, bg="#e5e5e5", command=self.open_printing_frame,bd=0, font=('Helvetica', 25,'bold')).place(x=0, y=325, width=400, height=75)
        Button(self.menu_frame, text="Sign Out", highlightthickness=0, fg="#fb5870", bg="#e5e5e5", command=self.logout, bd=0, font=('Helvetica', 25,'bold')).place(x=0, y=825, width=400, height=75)
        Button(self.menu_frame, text="Quit", highlightthickness=0, fg="#fb5870", bg="#e5e5e5", command=self.on_closing, bd=0, font=('Helvetica', 25,'bold')).place(x=0, y=900, width=400, height=75)
        
        
        #Buttons & Widgets in the manage frame
        self.type_of_search = StringVar()
        self.search = StringVar()
        
        self.search_printer = Button(self.manage_frame, text="Search", font=('Helvetica', 12, 'bold'), highlightthickness=0, bg="#33b249",fg="#ffffff", command=self.search_data,bd=0).place(x=1250, y=150, width=125, height=30)
        self.search_printer_text = Entry(self.manage_frame, font=('Helvetica', 12, 'bold'), width=404, justify=LEFT, textvariable=self.search).place(x=150, y=150, width=1000, height=30)

        
        self.search_choose = ttk.Combobox(self.manage_frame, width=39, font=('Helvetica', 12), state='readonly', textvariable=self.type_of_search)
        self.search_choose['values'] = ('Option', 'ID', 'Name', 'Manufacturer', 'Model', 'Serial Number', 'Calibration')
        self.search_choose.current(0)
        self.search_choose.place(x=1150, y=150, width=100, height=30)

       


        # Middle Frame that contain input information of the 3D printer machine
        self.mid_frame = Frame(self.manage_frame, bg="#e5e5e5")
        self.mid_frame.place(x=150, y=200, width=1225, height=303)

        

        # Widget for the middle frame
        Label(self.manage_frame, text="Manage", highlightthickness=0, bg="#f2f2f2", font=('Helvetica', 40,'bold')).place(x=150, y=80)
        self.printer_name = Label(self.mid_frame, text="3D Printer Name", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=15, width=120, height=30)
        self.printer_manufacturer = Label(self.mid_frame, text="Manufacturer", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=55, width=120, height=30)
        self.printer_model = Label(self.mid_frame, text="Model", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=95, width=120, height=30)
        self.printer_serial_num = Label(self.mid_frame, text="Serial Number", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=135, width=120, height=30)
        self.printer_firmware_vers = Label(self.mid_frame, text="Firmware Version", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=175, width=120, height=30)
        self.printer_calibration = Label(self.mid_frame, text="Calibration", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=215, width=120, height=30)

        #Function Button
        self.save_printer = Button(self.mid_frame, text="Add a new printer ", highlightthickness=0, bg="#fbfbfb", command=self.save_data,bd=0).place(x=1000, y=15, width=175, height=30)
        self.update_printer = Button(self.mid_frame, text="Update a printer", highlightthickness=0, bg="#fbfbfb", command=self.update_data,bd=0).place(x=1000, y=55, width=175, height=30)
        self.delete_printer = Button(self.mid_frame, text="Delete a printer", highlightthickness=0, bg="#fbfbfb", command=self.delete_data,bd=0).place(x=1000, y=95, width=175, height=30)
        Button(self.mid_frame, text="Show all", highlightthickness=0, bg="#fbfbfb", command=self.display_data,bd=0).place(x=1000, y=135, width=175, height=30)
        self.reset_printer = Button(self.mid_frame, text="Reset", highlightthickness=0, fg="#ffffff", bg="#fb5870", command=self.delete_all_data, bd=0).place(x=1000, y=215, width=175, height=30)

        
        # Entry for the middle frame
        self.printer_name_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.name)
        self.printer_name_text.place(x=159, y=15, width=800, height=30)

        self.manufacturer_text = Entry(self.mid_frame, font=('arial', 12, 'bold'),  width=404, justify=LEFT, textvariable=self.manufacturer)
        self.manufacturer_text.place(x=159, y=55, width=800, height=30)

        self.model_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.model)
        self.model_text.place(x=159, y=95, width=800, height=30)

        self.serial_num_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.serial_num)
        self.serial_num_text.place(x=159, y=135, width=800, height=30)

        self.firmware_vers_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.firmware_vers)
        self.firmware_vers_text.place(x=159, y=175, width=800, height=30)


        self.calibration_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT).place(x=159, y=215, width=400, height=30)
        self.calibration_choose = ttk.Combobox(self.mid_frame, width=39, font=('Century Gothic', 12), state='readonly', textvariable=self.calibration)
        self.calibration_choose['values'] = ('Bed Leveling',
                                             'Extruder',
                                             'Temperature',
                                             'Flow Rate',
                                             'Retraction',
                                             'Z-axis')

        self.calibration_choose.current()
        self.calibration_choose.place(x=159, y=215, width=800, height=30)



        # Bottom Frame that list information of 3D printer
        self.bottom_frame = Frame(self.manage_frame, bg="#e5e5e5")
        self.bottom_frame.place(x=150, y=500, width=1225, height=475)

        # -------------------------------Treeview-------------------------------
        scroll_x = Scrollbar(self.bottom_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.bottom_frame, orient=VERTICAL)

        columns = ('ID', 'name', 'manufacturer', 'model', 'serial_num', 'firmware_vers', 'calibration')
        self.printer_list = ttk.Treeview(self.bottom_frame, height=12,
                                           columns=columns,
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set,)
        

        scroll_x.config(command = self.printer_list.xview)
        scroll_y.config(command = self.printer_list.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.printer_list.pack(fill = BOTH, expand = 1)

        self.printer_list.heading('ID', text='ID')
        self.printer_list.heading('name', text='Name')
        self.printer_list.heading('manufacturer', text='Manufacturer')
        self.printer_list.heading('model', text='Model')
        self.printer_list.heading('serial_num', text='Serial')
        self.printer_list.heading('firmware_vers', text='Firmware')
        self.printer_list.heading('calibration', text='Calibration')


        self.printer_list['show'] = 'headings'
        self.printer_list.column('ID', width=1)
        self.printer_list.column('name', width=100)
        self.printer_list.column('manufacturer', width=100)
        self.printer_list.column('model', width=40)
        self.printer_list.column('serial_num', width=30)
        self.printer_list.column('firmware_vers', width=20)
        self.printer_list.column('calibration', width=100)
        self.printer_list.pack(fill=BOTH, expand=1)

        self.printer_list.bind('<ButtonRelease-1>', self.clicker)
        self.display_data()

        self.choose_row()

        
        #Printing Frame
        Label(self.printing_frame, text="Printing", highlightthickness=0, bg="#f2f2f2", font=('Helvetica', 40,'bold')).place(x=150, y=80)

            # Search in printing
        
        self.search_printer = Button(self.printing_frame, text="Search", font=('Helvetica', 12, 'bold'), highlightthickness=0, bg="#33b249",fg="#ffffff", command=self.search_data,bd=0).place(x=1250, y=150, width=125, height=30)
        self.search_printer_text = Entry(self.printing_frame, font=('Helvetica', 12, 'bold'), width=404, justify=LEFT, textvariable=self.search).place(x=150, y=150, width=1000, height=30)
        self.search_choose = ttk.Combobox(self.printing_frame, width=39, font=('Helvetica', 12), state='readonly', textvariable=self.type_of_search)
        self.search_choose['values'] = ('ID')
        self.search_choose.current(0)
        self.search_choose.place(x=1150, y=150, width=100, height=30)

            #Mid frame in printing
        self.mid_frame = Frame(self.printing_frame, bg="#e5e5e5")
        self.mid_frame.place(x=150, y=200, width=1225, height=303)

            # Widget for the middle frame in printing
        
        self.printing_name = Label(self.mid_frame, text="3D Printer Name", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=15, width=120, height=30)
        self.printing_manufacturer = Label(self.mid_frame, text="Manufacturer", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=55, width=120, height=30)
        self.printing_model = Label(self.mid_frame, text="Model", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=95, width=120, height=30)
        self.printing_serial_num = Label(self.mid_frame, text="Serial Number", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=135, width=120, height=30)
        self.printing_firmware_vers = Label(self.mid_frame, text="Firmware Version", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=175, width=120, height=30)
        self.printing_calibration = Label(self.mid_frame, text="Calibration", highlightthickness=0, bg="#e5e5e5", anchor = "w").place(x=15, y=215, width=120, height=30)
        

            # Entry for the middle frame in printing
        self.printing_name_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.name)
        self.printing_name_text.place(x=159, y=15, width=800, height=30)

        self.manufacturer_text = Entry(self.mid_frame, font=('arial', 12, 'bold'),  width=404, justify=LEFT, textvariable=self.manufacturer)
        self.manufacturer_text.place(x=159, y=55, width=800, height=30)

        self.model_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.model)
        self.model_text.place(x=159, y=95, width=800, height=30)

        self.serial_num_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.serial_num)
        self.serial_num_text.place(x=159, y=135, width=800, height=30)

        self.firmware_vers_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.firmware_vers)
        self.firmware_vers_text.place(x=159, y=175, width=800, height=30)


        self.calibration_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT).place(x=159, y=215, width=800, height=30)

            #Function Button in printing
        self.print = Button(self.mid_frame, text="Print", command=self.print, highlightthickness=0, fg="#ffffff", bg="#33b249",bd=0).place(x=1000, y=15, width=175, height=50)
        self.stop_printing = Button(self.mid_frame, text="Stop", command=self.stop_printing, highlightthickness=0, fg="#ffffff", bg="#fb5870", bd=0).place(x=1000, y=75, width=175, height=50)
        self.maintain = Button(self.mid_frame, text="Maintain & Repair", command=self.maintain, highlightthickness=0, bg="#fbfbfb",bd=0).place(x=1000, y=135, width=175, height=45)
        self.maintain = Button(self.mid_frame, text="Show all", command=self.display_printing_data, highlightthickness=0, bg="#fbfbfb",bd=0).place(x=1000, y=213, width=175, height=30)
        
            #Bottom Frame in printing
        self.bottom_frame = Frame(self.printing_frame, bg="#e5e5e5")
        self.bottom_frame.place(x=150, y=500, width=1225, height=475)

            #Treeview in printing
        scroll_x = Scrollbar(self.bottom_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.bottom_frame, orient=VERTICAL)

        columns = ('ID', 'name', 'printing_status')
        self.printing_list = ttk.Treeview(self.bottom_frame, height=12,
                                           columns=columns,
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set,)
        

        scroll_x.config(command = self.printer_list.xview)
        scroll_y.config(command = self.printer_list.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.printing_list.pack(fill = BOTH, expand = 1)

        self.printing_list.heading('ID', text='ID')
        self.printing_list.heading('name', text='Name')
        self.printing_list.heading('printing_status', text='Status')
        
        


        self.printing_list['show'] = 'headings'
        self.printing_list.column('ID', width=100)
        self.printing_list.column('name', width=400)
        self.printing_list.column('printing_status', width=400)
        
        
        self.printing_list.pack(fill=BOTH, expand=1)

        self.printing_list.bind('<ButtonRelease-1>', self.printing_clicker)
        self.display_printing_data()

        self.choose_row_printing()
        
       
        

    def save_data(self):
        if self.name.get() == "" or self.manufacturer.get() == "" or self.model.get() == "" or self.serial_num.get() == "" or self.firmware_vers.get() == "" or self.calibration.get() == "":
            tkinter.messagebox.askokcancel(title='Error',
                                           message='Please enter valid data!')
        else:
            try:
                database.add(self.account,
                             self.name.get(),
                             self.manufacturer.get(),
                             self.model.get(),
                             self.serial_num.get(),
                             self.firmware_vers.get(),
                             self.calibration.get()
                             )
               
                self.display_data()
                self.display_printing_data()
                

                tkinter.messagebox.showinfo(title='Message',
                                            message='Sucessful added printer!')
                self.printer_name_text.delete(0, END)
                self.manufacturer_text.delete(0, END)
                self.model_text.delete(0, END)
                self.serial_num_text.delete(0, END)
                self.firmware_vers_text.delete(0, END)
                #self.calibration_text.delete(0, END)

            except Exception as es:
                tkinter.messagebox.showerror(title='Error',
                                             message=f'Because {str(es)}')

    def display_data(self):
        """Display all data by fetch data"""
        data = database.display(account=self.account)
        if len(data) >= 0:
            self.printer_list.delete(*self.printer_list.get_children())
            for i in data:
                self.printer_list.insert("", END, value=i)

    def display_printing_data(self):
        printing_data = database.display_printing(account=self.account)
        if len(printing_data) >= 0:
            self.printing_list.delete(*self.printing_list.get_children())
            for i in printing_data:
                self.printing_list.insert("", END, value=i)

    def choose_row_printing(self):
        self.printer_name_text.delete(0, END)
        self.manufacturer_text.delete(0, END)
        self.model_text.delete(0, END)
        self.serial_num_text.delete(0, END)
        self.firmware_vers_text.delete(0, END)
      

        choose_row_printing = self.printing_list.focus()
        self.printing_data = self.printing_list.item(choose_row_printing, 'value')
        try:
            self.id = self.printing_data[0]
            self.name.set(self.printing_data[1])
            self.printing_status.set(self.printing_data[2])
        except:
            pass


    

    def choose_row(self):
        """Choose a row and return values into entries"""
        self.printer_name_text.delete(0, END)
        self.manufacturer_text.delete(0, END)
        self.model_text.delete(0, END)
        self.serial_num_text.delete(0, END)
        self.firmware_vers_text.delete(0, END)

        # Choose a value of a row
        choose_row = self.printer_list.focus()
        # Grab the value of the chosen row
        self.data = self.printer_list.item(choose_row, 'value')
        try:
            self.id = self.data[0]
            self.name.set(self.data[1])
            self.manufacturer.set(self.data[2])
            self.model.set(self.data[3])
            self.serial_num.set(self.data[4])
            self.firmware_vers.set(self.data[5])
            self.calibration.set(self.data[6])
        except:
            pass

    def printing_clicker(self, event):
        self.choose_row_printing()

    def clicker(self, event):
        """Click handler when you click into a row"""
        self.choose_row()
        

    def update_data(self):
        if self.name.get() == "" or self.manufacturer.get() == "" or self.model.get() == "" or self.serial_num.get() == "" or self.firmware_vers.get() == "" or self.calibration.get() == "":
            tkinter.messagebox.askretrycancel(title='Error', message='Please choose a data!')
        else:
            try:
                answer = tkinter.messagebox.askyesno("Confirmation", "Do you want to update information?")
                if answer:
                    database.update(self.account,
                                    self.id,
                                    self.name.get(),
                                    self.manufacturer.get(),
                                    self.model.get(),
                                    self.serial_num.get(), 
                                    self.firmware_vers.get(),
                                    self.calibration.get()
                                    )

                else:
                    if not update:
                        return
                self.display_data()
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Because of {str(e)}")

        # Fill in empty into the entries
        self.printer_name_text.delete(0, END)
        self.manufacturer_text.delete(0, END)
        self.model_text.delete(0, END)
        self.serial_num_text.delete(0, END)
        self.firmware_vers_text.delete(0, END)
        
    def delete_data(self):
        if not self.printer_list.selection():
            tkinter.messagebox.showwarning("Error", "Please choose a data you want to delete!")
        else:
            answer = tkinter.messagebox.askyesno("Delete data", "Are you sure you want to permanently delete this?")
            if answer:
                database.delete(self.account, self.id)
                self.display_data()
                self.display_printing_data()
                self.printer_name_text.delete(0, END)
                self.manufacturer_text.delete(0, END)
                self.model_text.delete(0, END)
                self.serial_num_text.delete(0, END)
                self.firmware_vers_text.delete(0, END)
                tkinter.messagebox.showinfo("Delete", "You deleted the data")
    
    def open_manage_frame(self):
        self.manage_frame.place(x=400, y=0, width=400, height=1080, relwidth=1, relheight=1)
        self.mid_frame.place(x=150, y=200, width=1225, height=303)
        self.bottom_frame.place(x=150, y=500, width=1225, height=475)
        self.printing_frame.place_forget()
        

    def open_printing_frame(self):
        self.manage_frame.place_forget()
        #self.mid_frame.place_forget()
        #self.bottom_frame.place_forget()
        self.printing_frame.place(x=400, y=0, width=400, height=1080,relwidth=1, relheight=1)

            
    def delete_all_data(self):
        """A function to delete all data and drop table"""
        answer = tkinter.messagebox.askyesno("Warning", "Are you sure you want to permanently delete ALL data?")
        if answer:
            database.delete_all(self.account)
            self.display_data()
            self.display_printing_data()
            # Fill in empty into the entries
            self.printer_name_text.delete(0, END)
            self.manufacturer_text.delete(0, END)
            self.model_text.delete(0, END)
            self.serial_num_text.delete(0, END)
            self.firmware_vers_text.delete(0, END)

    def on_closing(self):
        quit()

    def search_data(self):
        if self.type_of_search == "Option" or self.search == "":
            tkinter.messagebox.showwarning("Error", "Please choose the attribute!")
        else:
            try:
                data = database.search(self.account, self.type_of_search.get(), self.search.get())
                if len(data) >= 0:
                    self.printer_list.delete(*self.printer_list.get_children())
                    for i in data:
                        self.printer_list.insert("", END, value=i)
                    self.printing_list.delete(*self.printing_list.get_children())
                    for i in data:
                        self.printing_list.insert("", END, value=i)
            except:
                tkinter.messagebox.showwarning("Warning", "Please choose the attribute!")

    def print(self):
        if self.printing_status == "Ready":
            answer = tkinter.messagebox.askokcancel("Confirmation", "Do you want to print?")
            if answer:
                printing_data = database.print(self.account, 
                                                self.id, 
                                                self.name, 
                                                self.printing_status
                                                )
                self.display_printing_data()
        else:
            tkinter.messagebox.showwarning("Warning", "Selected printer is printing or need to maintain!")


    def stop_printing(self):
        if self.printing_status != "Printing...":
            answer = tkinter.messagebox.askokcancel("Confirmation", "Do you want to stop printing?")
            if answer:
                printing_data = database.stop_printing(self.account, 
                                                        self.id, 
                                                        self.name, 
                                                        self.printing_status
                                                        )
                self.display_printing_data()
        else:
            tkinter.messagebox.showwarning("Warning", "Selected printer is not printing!")

    def maintain(self):
        if self.printing_status == "Stopped/Maintenance Needed!":
            answer = tkinter.messagebox.askokcancel("Confirmation", "Do you want to maintain this printer?")
            if answer:
                printing_data = database.maintain(self.account, 
                                                self.id, 
                                                self.name, 
                                                self.printing_status
                                                )
            self.display_printing_data()                                   
        else:
            tkinter.messagebox.showwarning("Warning", "Selected printer is currently running or in a good condition!")

    def logout(self):
        self.window.destroy()    
window = Tk()
obj = GUI(window, "dang")
window.mainloop()