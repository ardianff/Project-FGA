from tkinter import *
import tkinter.messagebox as msg 
class LoginRegisterUser :
    def __init__(self, gui, header) :
        self.gui = gui 
        self.gui.geometry("400x350")
        self.gui.title(header)
        self.gui.resizable(True, True)
        self.main_screen()
    def login(self) :
        screen1 = Toplevel(app)
        screen1.title("Login")
        screen1.geometry("350x160")
        Label(screen1, text='Username ').pack()
        self.entryUser = Entry(screen1, width=30)
        self.entryUser.pack()
        Label(screen1, text='Password').pack()
        self.entryPass = Entry(screen1, show='*',width=30)
        self.entryPass.pack()
        self.check = IntVar() 
        self.showPass = Checkbutton(screen1, text='Lihat Password', 
            variable=self.check, command=self.open_password).pack(expand = False, fill = BOTH,padx=10,pady=5)
        self.showPass
        self.btnLogin = Button(screen1, text='Login', command=self.do_login).pack(side = LEFT, expand = True, fill = BOTH,padx=10,pady=5)
        self.btnRegister = Button(screen1, text='Register', command=self.register).pack(side = LEFT, expand = True, fill = BOTH,padx=10,pady=5)
        self.btnCancel = Button(screen1, text='Cancel', command=self.close_gui).pack(side = LEFT, expand = True, fill = BOTH,padx=10,pady=5)
    def register(self) :
        global screen1
        screen1 = Toplevel(app)
        screen1.title("Register")
        screen1.geometry("350x200")
        Label(screen1, text='Nama').pack()
        self.entryUserName = Entry(screen1, width=30)
        self.entryUserName.pack()
        Label(screen1, text='Username').pack()
        self.entryUser = Entry(screen1, width=30)
        self.entryUser.pack()
        Label(screen1, text='Password').pack()
        self.entryPass = Entry(screen1, show='*',width=30)
        self.entryPass.pack()
        self.check = IntVar() 
        self.showPass = Checkbutton(screen1, text='Lihat Password', 
            variable=self.check, command=self.open_password).pack(expand = False, fill = BOTH,padx=10,pady=5)
        self.showPass
        self.btnRegister = Button(screen1, text='Register', command=self.register_user).pack(side = LEFT, expand = True, fill = BOTH,padx=10,pady=5)
        self.btnLogin = Button(screen1, text='Login', command=self.login).pack(side = LEFT, expand = True, fill = BOTH,padx=10,pady=5)
        self.btnCancel = Button(screen1, text='Cancel', command=self.close_gui).pack(side = LEFT, expand = True, fill = BOTH,padx=10,pady=5)
    def register_user(self): 
        get_name = self.entryUserName.get()
        get_username = self.entryUser.get()
        get_password = self.entryPass.get() 
        file = open('D:\Project\login_gui\database.txt','a')
        file.write("\n"+get_name+","+get_username+","+get_password)
        file.close()
        self.entryUserName.delete(0,END)
        self.entryUser.delete(0,END)
        self.entryPass.delete(0,END)
        Label(screen1, text="Registrasi Sukses",fg="green", font=("calibri", 11)).pack(side = BOTTOM)
    def do_login(self) :
        get_username = self.entryUser.get()
        get_password = self.entryPass.get() 
        sukses =False
        file = open('D:\Project\login_gui\database.txt','r')
        for i in file :
            nama,username,password = i.split(',')
            password = password.strip()
            if get_username == username and get_password == password:
                sukses = True 
                break
        if (sukses) :
            msg.showinfo("Berhasil Login", "Selamat Datang %s"%(nama), parent=self.gui) 
            self.close_gui()
        elif get_username=='' or get_password=='' :
            msg.showwarning('Gagal', 'Username Atau Password Anda Tidak Boleh KOsong', parent=self.gui) 
            self.entryUser.focus_set()
        else: 
            msg.showerror('Gagal', "Username Atau Password Yang Anda Masuukan Salah SIlahkan Periksa Kembali", parent=self.gui) 
            self.delete_data()
    def delete_data(self):
        self.entryUser.delete(0,END)
        self.entryPass.delete(0,END)
        self.entryUser.focus_set()
    def open_password(self) :
        Show = self.check.get() 
        if Show == 1 : 
            self.entryPass['show'] = ''
        else :
            self.entryPass['show'] = '*'
    def close_gui(self) :
        self.gui.destroy()
    def main_screen(self) :
        Label(text = "Selamat Datang Di Sistem Aplikasiku", bg = "blue", width = "300", height = "2", font = ("Calibri", 13), fg="white").pack()
        Label(text = "").pack()
        Button(text = "Login User", height = "2", width = "30", command = self.login).pack()
        Label(text = "").pack()
        Button(text = "Register User",height = "2", width = "30", command = self.register).pack()     
if __name__ == '__main__':
    global app
    app = Tk()
    start = LoginRegisterUser(app, "Aplikasiku")
    app.mainloop() 