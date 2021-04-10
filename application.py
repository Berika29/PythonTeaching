import tkinter as tk
import sqlite3


def loginCheck(username, password):
    conn=createConnection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM DETAILS WHERE USERNAME=? AND PASSWORD=?",(username,password,))
    result=cur.fetchall()
    if not result:
        return False
    else:
        return True

def settingCode(code):
    print("x")

def createConnection():
    conn=None
    try:
        conn=sqlite3.connect("login.db")
    except Exception as e:
        print("error connecting")
    return conn

def loginScreen(master):
    def submit_btn_pressed():
        global username
        username=username_Var.get()
        password=password_Var.get()
        check=loginCheck(username,password)
        if check==True:
            screen_frm.grid_forget()
            screen_frm.destroy()
            startScreen(master)
        if check==False:
            error_lbl=tk.Label(master=Login_frm,text="your username/password is incorrect,try again",fg='red',bg='gray')
            error_lbl.config(font=("Courier", 12, 'bold'))
            error_lbl.place(x=250, y=400, anchor='center')

    screen_frm=tk.Frame(master=master,width="1000",height="750",)
    screen_frm.place(x=0,y=0)
    Login_frm = tk.Frame(master=screen_frm, width="500", height="500", bg="gray")
    Login_frm.place(x=500, y=375, anchor='center')
    login_lbl = tk.Label(master=screen_frm, text="log in")
    login_lbl.config(font=("Courier", 40, 'bold'))
    login_lbl.place(x=500, y=50, anchor='center')
    username_lbl = tk.Label(master=Login_frm, text="username:", bg='gray')
    username_lbl.config(font=("Courier", 16, 'bold'))
    username_lbl.place(x=50, y=125)
    password_lbl = tk.Label(master=Login_frm, text="password:", bg='gray')
    password_lbl.config(font=("Courier", 16, 'bold'))
    password_lbl.place(x=50, y=200)
    username_Var=tk.StringVar()
    password_Var = tk.StringVar()
    username_ent = tk.Entry(master=Login_frm, bg="white", width=50,textvariable=username_Var)
    username_ent.place(x=170, y=130)
    password_ent = tk.Entry(master=Login_frm, bg="white", width=50, show="*",textvariable=password_Var)
    password_ent.place(x=170, y=205)
    submit_btn = tk.Button(master=Login_frm, text="submit", width=10,command=submit_btn_pressed)
    submit_btn.place(x=250, y=300, anchor='center')

def startScreen(master):
    def task_view_btn_pressed():
        start_screen_frm.grid_forget()
        start_screen_frm.destroy()
        taskViewScreen(master)
    def settings_btn_pressed():
        start_screen_frm.grid_forget()
        start_screen_frm.destroy()
        settingsScreen(master)

    start_screen_frm=tk.Frame(master=master,width="1000",height="750",)
    start_screen_frm.place(x=0,y=0)
    start_frm=tk.Frame(master=start_screen_frm, width="500", height="500", bg="gray")
    start_frm.place(x=500, y=375, anchor='center')
    startScreen_lbl=tk.Label(master=start_screen_frm,text="Python Learning Tool")
    startScreen_lbl.config(font=("Courier", 32, 'bold'))
    startScreen_lbl.place(x=500,y=50,anchor='center')
    taskView_btn=tk.Button(master=start_frm,text="Task View",command=task_view_btn_pressed())
    taskView_btn.place(x=250,y=100,anchor='center',width=400,height=100)
    setting_btn=tk.Button(master=start_frm,text="Settings")
    setting_btn.place(x=250, y=250, anchor='center', width=400, height=100)



def taskViewScreen(master):
    print("x")

def settingsScreen(master):
    screen_frm = tk.Frame(master=master, width="1000", height="750", )
    screen_frm.place(x=0, y=0)
    setting_lbl=tk.Label(master=screen_frm,text="Enter Code:")
    setting_lbl.place(x=100,y=250)

def main():
    master=tk.Tk()
    master.geometry("1000x750")
    master.resizable(height=False, width=False)
    loginScreen(master)
    master.mainloop()

if __name__ == "__main__":
    main()