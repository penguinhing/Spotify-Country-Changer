import sys


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import tkinter.messagebox as msgbox
import threading
from PENGUIN.Function import *
import PENGUIN.extension.GUI_Support
import os.path
import webbrowser
from random import randint

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Spotify (root)
    PENGUIN.extension.GUI_Support.init(root, top)
    root.mainloop()

w = None
def create_Spotify(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Spotify(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Spotify (w)
    extension.GUI_Support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Spotify():
    global w
    w.destroy()
    w = None

class Spotify(Function):
    def __init__(self, top=None):


        Function.__init__(self)

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("400x200+814+321")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0,  0)
        top.title("Spotify Country Changer v1.1")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.iconbitmap('PENGUIN/icon/spotify.ico')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.05, rely=0.0, height=41, width=184)
        self.Label1.configure(activebackground="#f0f0f0f0f0f0")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Verdana} -size 22 -weight bold")
        self.Label1.configure(foreground="#0080ff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Login Info''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.075, rely=0.2, height=31, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Candara} -size 14 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''User ID:''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.088, rely=0.35, height=27, relwidth=0.485)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Microsoft New Tai Lue} -size 14 -weight bold")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="#02b002")
        self.Entry1.configure(insertbackground="#000000")
        self.Entry1.configure(selectbackground="black")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.configure(validate="focus")

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.088, rely=0.55, height=31, width=84)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#ffffff")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Candara} -size 14 -weight bold")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Password:''')

        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(relx=0.088, rely=0.7, height=27, relwidth=0.485)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="-family {Microsoft New Tai Lue} -size 14 -weight bold")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="#02b002")
        self.Entry1_1.configure(insertbackground="#000000")
        self.Entry1_1.configure(selectbackground="black")
        self.Entry1_1.configure(selectforeground="white")
        self.Entry1_1.configure(validate="focus")
        self.Entry1_1.configure(show="●")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button1 = tk.Button(top, command=self.Run)
        self.Button1.place(relx=0.625, rely=0.7, height=44, width=127)
        self.Button1.configure(activebackground="red")
        self.Button1.configure(activeforeground="#FFFFFF")
        self.Button1.configure(background="#1ed760")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Arial Black} -size 18 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="ridge")
        self.Button1.configure(text='''START''')

        self.Button2 = tk.Button(top, command=self.disable_window)
        self.Button2.place(relx=0.65, rely=0.14, height=104, width=107)
        self.Button2.configure(activebackground="#FFFFFF")
        self.Button2.configure(activeforeground="#FFFFFF")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        photo_location = os.getcwd() + '\\PENGUIN\\img\\logo.png'
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Button2.configure(image=_img0)
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="flat")
        self.Button2.configure(text='''Button''')
    
    def Run(self):
        with open('PENGUIN/temp.txt', 'r') as FILE:
            count = FILE.readline()
            if count == '0':
                msgbox.showinfo("제작: 펭귄", "반드시 파이어폭스를 설치한 후에 이용하여 주세요.")
                with open('PENGUIN/temp.txt', 'w') as FILE2:
                    FILE2.write(str(int(count)+1))

        self.ID = self.Entry1.get()
        self.PW = self.Entry1_1.get()

        if len(self.ID) <= 5 or len(self.PW) <= 5:
            msgbox.showwarning("계정 정보 확인", "아이디 혹은 비밀번호를 제대로 입력해주세요!")
            return 0

        self.Button1.configure(command=self.STOP)
        self.Button1.configure(text="STOP")
        self.Button1.configure(background="red")
        self.Entry1.configure(state="disable")
        self.Entry1_1.configure(state="disable")

        th1 = threading.Thread(target=self.showProgress)
        th1.daemon = True
        th1.start()

        th2 = threading.Thread(target=self.setSpotify)
        th2.daemon = True
        th2.start()

    def STOP(self):
        th3 = threading.Thread(target=self._STOP)
        th3.daemon = True
        th3.start()

    def _STOP(self):
        try:
            self.root2.destroy()
            self.driver.quit()
        except Exception:
            pass
        self.Entry1.configure(state="normal")
        self.Entry1_1.configure(state="normal")
        self.Button1.configure(command=self.Run)
        self.Button1.configure(background="#1ed760")
        self.Button1.configure(text="START")


    def disable_window(self):
        webbrowser.open("https://blog.naver.com/unknown134959")
        pass


    def showProgress(self):
        self.root2 = tk.Toplevel()
        self.root2.protocol("WM_DELETE_WINDOW", self.disable_window)
        self.root2.iconbitmap('PENGUIN/icon/penguin.ico')
        self.root2.resizable(False, False)
        self.root2.geometry("+814+360")
        self.root2.title("0 %")
        self.p_var = tk.IntVar()
        self.progressbar = ttk.Progressbar(self.root2, maximum=100, length=400, mode='determinate', variable=self.p_var)
        self.progressbar.pack()

    def set_progess(self, value, text=''):
        for i in range(self.p_var.get(), value+1):
            time.sleep(0.01)
            self.p_var.set(i)
            self.root2.title("{0} % {1}".format(self.p_var.get(), text))
            self.progressbar.update()


    # 1: 성공,  0: 실패,    2: 알 수 없는 오류 발생
    def setSpotify(self):
        self.driver = webdriver.Firefox(executable_path=os.getcwd() + '\\PENGUIN\\geckodriver.exe',options=self.options)
        self.driver.maximize_window()
        self.set_progess(randint(5, 10))
        try:
            if self.get_extension_id() == 2 and self.extension_id == None:
                msgbox.showerror("Extension Error", "애드온 ID 획득에 실패했습니다.")
                return 0

            self.set_progess(randint(10, 30))

            # 연결
            var = self.onVPN()
            if var == 0:
                msgbox.showerror("Connected Failed", "VPN 에 연결하는 데 문제가 발생하였습니다.")
                return 0
            elif var == 2:
                msgbox.showerror("Error", "연결 중 알 수 없는 오류가 발생하였습니다.")
                return 0
            self.set_progess(randint(30, 60), text='(1 ~ 3분 소요)')

            # 로그인
            var = self.Login()
            if var == 0:
                msgbox.showerror("Login Failed", "아이디 혹은 패스워드를 잘못입력하셨습니다.")
                return 0
            elif var == 2:
                msgbox.showerror("Error", "로그인 중 알 수 없는 오류가 발생하였습니다.")
                return 0
            self.set_progess(randint(60, 90))

            # 국적 변경
            var = self.ChangeCountry()
            if var == 2:
                msgbox.showerror("Error", "국가 변경 중 알 수 없는 오류가 발생하였습니다.")
                return 0
            
            self.set_progess(100)
            msgbox.showinfo("Complete!", "계정의 국적 변경이 완료되었습니다!")
        finally:
            self.STOP()

if __name__ == '__main__':
    vp_start_gui()





