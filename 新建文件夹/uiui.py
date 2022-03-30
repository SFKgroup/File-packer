import tkinter as tk
import tkinter.ttk
window = tk.Tk()
window.title("File Packager")
window.geometry("400x153")
window.config(bg='#ffffcc')
n = tk.StringVar()
n.set('File Packager')
tk.Label(window, textvariable=n,bg='#ffffcc',bd=10,font=('consolas',30)).pack(side=tk.TOP)
def u():
    pa['value'] = 10
    window.update()
    import file
    for i in range(10,101,1):
        pa['value'] = i
        window.update()
    n.set('Done!')
def us():window.destroy()
pa = tk.ttk.Progressbar(window,length=300)
pa.pack(side=tk.TOP,pady=5)
pa['maximum'] = 100
pa['value'] = 0
tk.Button(window,text='Unpack',command=u,width=19).pack(side=tk.LEFT)
tk.Button(window,text='Quit',command=us,width=19).pack(side=tk.LEFT)
window.mainloop()