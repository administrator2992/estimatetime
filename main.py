from tkinter import *
from tkinter.font import *
from package import *
from tkinter import messagebox
from tkinter.ttk import Frame
from tkinter.ttk import Style

class MainFrame(Frame):

    def __init__(self, main):
        super().__init__()
        self.main = main

        self.fsedang = Font(family= 'aerial', weight= 'bold', size=9)
        self.fnol = Font(family= 'aerial', weight= 'bold', size=15)

        self.frame = Frame(self.main, width=200, height=400)
        self.frame.pack(fill='both', padx=10, pady=5, expand=True)

        self.bar = Frame(self.frame, width=1, height=5)
        self.bar.pack(fill='both', padx=5, pady=5, expand=True)

        self.e = Entry(self.bar)
        self.e.pack(pady=5)

        pilihan = [
            "Detik",
            "Menit",
            "Jam",
            "Hari",
            "Minggu",
            "Bulan",]

        self.clicked = StringVar()
        self.clicked.set("Choose a Time")

        drop = OptionMenu(self.bar, self.clicked, *pilihan)
        drop.pack(pady=(0,10))

        self.butt = Frame(self.bar, width=100, height=80)
        self.butt.pack()

        self.button = Button(self.butt, text="Convert", command=self.show, width=10, font=self.fsedang).pack(side=LEFT, padx=5)

        self.button2 = Button(self.butt, text="Clear", command=self.clear, width=10, font=self.fsedang).pack(side=LEFT)

        Label(self.bar, text="format : y:m:w:d:h:m:s\n--------").pack()

        self.num = StringVar()
        self.label = Label(self.bar, textvariable=self.num, font=self.fnol)
        self.label.pack()
        self.num.set("0:0:0:0:0:0:0")

        self.initUI()

    def initUI(self):

        self.master.title('Estimasi Waktu')
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        icon = PhotoImage(file = 'img/icon.png')
        self.master.iconphoto(False, icon)

    def centerWindow(self):

        w = 320
        h = 200

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.master.resizable(False, False)

    def show(self):
        try:
            get = self.clicked.get()
            tm = float(self.e.get())
            if tm == 0.0:
                raise ValueError("input belum diisi")
            time = float(self.e.get())
            if get == "Detik":
                detik = time
                setData = Set(0, 0, detik, 0, 0, 0, 0)
                data = setData.convert()
                self.num.set(data)
                self.e.delete(0, 'end')
            elif get == "Menit":
                menit = time
                setData = Set(0, menit, 0, 0, 0, 0, 0)
                data = setData.convert()
                self.num.set(data)
                self.e.delete(0, 'end')
            elif get == "Jam":
                jam = time
                setData = Set(jam, 0, 0, 0, 0, 0, 0)
                data = setData.convert()
                self.num.set(data)
                self.e.delete(0, 'end')
            elif get == "Hari":
                hari = time
                setData = Set(0, 0, 0, hari, 0, 0, 0)
                data = setData.convert()
                self.num.set(data)
                self.e.delete(0, 'end')
            elif get == "Minggu":
                minggu = time
                setData = Set(0, 0, 0, 0, minggu, 0, 0)
                data = setData.convert()
                self.num.set(data)
                self.e.delete(0, 'end')
            elif get == "Bulan":
                bulan = time
                setData = Set(0, 0, 0, 0, 0, bulan, 0)
                data = setData.convert()
                self.num.set(data)
                self.e.delete(0, 'end')
            else:
                raise Except("choose a time man !!!")
        except ValueError:
            messagebox.showerror("Error", "input salah atau belum diisi")
        except:
            messagebox.showerror("Error", "pilihan belum di pilih")
    def clear(self):
        self.num.set("0:0:0:0:0:0:0")        


def main():

    root = Tk()
    ex = MainFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()