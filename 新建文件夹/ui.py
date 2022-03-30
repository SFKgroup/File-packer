l = 10
p = '114514'
name = 'name'
import tkinter as tk
import os
import tkinter.ttk
self_path = os.getcwd()
window = tk.Tk()
window.title(name)
window.geometry("400x200")
window.config(bg='#ffffcc')
w = 0
n = tk.StringVar()
n.set('File Packager')
lb = tk.Label(window, textvariable=n,bg='#ffffcc',bd=10,font=('consolas',30))
lb.pack(side=tk.TOP)
v=tk.StringVar()
e=tk.Entry(window,textvariable=v,show='*',font=('consolas',20))
e.pack(side=tk.TOP)
def u():
    global w
    if v.get() == p:
        n.set('File Packager')
        lb.config(font=('consolas',35),fg='#000000')
        pa['value'] = 10
        window.update()
        import file
        for i in range(10,101,1):
            pa['value'] = i
            window.update()
        lb.config(font=('consolas',35),fg='#00ff00')
        n.set('Done!')
    else:
        v.set('')
        if l != None:
            if l-w>3:
                lb.config(font=('consolas',35),fg='#ff0000')
                n.set('Wrong!')
            else:
                lb.config(font=('consolas',20),fg='#ff0000')
                n.set('Wrong! You have ' + str(l-w) + ' chance.')
            w += 1
            if w > l:
                g = open(self_path+'/end.bat','w')
                g.write('taskkill /F /T /IM "'+name+'.exe"\ndel /F /Q "'+name+'.exe"\nstart del /f /q end.bat')
                g.close()
                os.chdir(self_path)
                os.system('start end.bat')
        else:
            lb.config(font=('consolas',35),fg='#ff0000')
            n.set('Wrong!')
def us():window.destroy()
pa = tk.ttk.Progressbar(window,length=300)
pa.pack(side=tk.TOP,pady=5)
pa['maximum'] = 100
pa['value'] = 0
tk.Button(window,text='Unpack',command=u,width=19).pack(side=tk.LEFT)
tk.Button(window,text='Quit',command=us,width=19).pack(side=tk.LEFT)
window.mainloop()