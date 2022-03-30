import os
import tkinter as tk
import tkinter.ttk
from tkinter import messagebox
from tkinter import filedialog
import ast

if os.path.exists('loc.set'):
    grand = open('loc.set','r')
    setting = ast.literal_eval(grand.readline())
    grand.close()
    print(setting)
else:setting = {'ifkey':True,'key':'123456','ifui':True,'chance':5,'name':'name','background':'#ffffcc','fg':False}#是否设置密码，密码，是否需要UI，密码尝试次数,文件名，颜色
self_path = os.getcwd()
path_list = []
window = tk.Tk()
window.title("File Packager")
window.geometry("840x630")
try:window.config(bg=setting['background'])
except:
    messagebox.showerror('Error','[ERROR]:Wrong colour : "'+setting['background']+'" .')
    setting['background'] = '#ffffcc'
    window.config(bg=setting['background'])
a = setting['background'].replace('#','')
if setting['fg']:
    def coutwo(x):
        if len(x) == 2:return x
        elif len(x) == 1:return '0'+x
        else:return '00'
    fontcolour = '#' + coutwo(hex(255-int(a[:2],16))[2:]) + coutwo(hex(255-int(a[2:4],16))[2:]) + coutwo(hex(255-int(a[-2:],16))[2:])
else:
    if int(a[:2],16) >= 160 or int(a[2:4],16) >= 160 or int(a[-2:],16) >= 160:fontcolour = '#000000'
    else:fontcolour = '#FFFFFF'
del a
window.iconbitmap('./icon/icon.ico')
def opfile():
    pth = filedialog.askopenfilenames()
    for apath in pth:
        if apath != '':
            if apath in list(msgw.get(0,msgw.size()-1)):messagebox.showwarning('Warning','[WARN]:"' + apath+'" has been imported.')
            else:msgw.insert(tk.END,str(apath))
def delete():
    index = msgw.curselection()
    if len(index) == 1:msgw.delete(index)
    elif len(index) == 0:pass
    else:
        for a,b in zip(list(index),range(len(index))):msgw.delete(int(a-b))
def run():
    try:os.mkdir(self_path+'/building/')
    except:pass
    grand = open(self_path+'/building/ui.py','w',encoding='utf-8')
    if setting['ifkey'] and not(setting['ifui']):grand.write('def wr():\n    if input(\'password:\') == '+setting['key']+'\n        thing_list=[')
    else:grand.write('def wr():\n    thing_list=[')
    length = len(list(msgw.get(0,msgw.size()-1)))
    for file,k in zip(list(msgw.get(0,msgw.size()-1)),range(1,length+1,1)):
        redfile = open(file,'rb')
        im = redfile.readline()
        grand.write('\'\'\'')
        while im != b'':
            grand.write(str(im.hex()))
            im = redfile.readline()
        grand.write('\'\'\',')
        pa['value'] = k*90//length
        window.update()
        #step
    fname = []
    for i in list(msgw.get(0,msgw.size()-1)):fname.append('./'+str(i.split('/')[-1]))
    if setting['ifkey'] and not(setting['ifui']):
        grand.write(']\n        name_list='+str(fname)+'''\n        for a,b in zip(thing_list,name_list):\n           grand=open(b,'wb')\n           grand.write(bytes.fromhex(a))\n            grand.close()\n''')
        grand.close()
        os.chdir(self_path)
        os.system('pyinstaller -c -F -n "'+setting['name']+'" .\\building\\ui.py -i .\icon\icon.ico')
    else:grand.write(']\n    name_list='+str(fname)+'''\n    for a,b in zip(thing_list,name_list):\n        grand=open(b,'wb')\n        grand.write(bytes.fromhex(a))\n        grand.close()\n''')
    pa['value'] = 95
    window.update()
    if setting['ifui'] and setting['ifkey']:
        grand.write('l = '+str(setting['chance'])+'\np = \''+ str(setting['key']) +'\'\nname = \''+setting['name']+'\'\n')
        grand.write('''
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
        wr()
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
                g.write('taskkill /F /T /IM "'+name+'.exe"\\ndel /F /Q "'+name+'.exe"\\nstart del /f /q end.bat')
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
window.mainloop()''')
        grand.close()
        os.chdir(self_path)
        os.system('pyinstaller -w -F -n "'+setting['name']+'" .\\building\\ui.py -i .\icon\icon.ico')
    elif setting['ifui'] and not(setting['ifkey']):
        grand.write('l = '+str(setting['chance'])+'\np = \''+ str(setting['key']) +'\'\n')
        grand.write('''
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
    wr()
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
''')
        grand.close()
        os.chdir(self_path)
        os.system('pyinstaller -w -F -n "'+setting['name']+'" .\\building\\ui.py -i .\icon\icon.ico')
    pa['value'] = 100
    window.update()
    messagebox.showinfo('imformation','Packed successfully.')
def setop():
    global psv,nmv,uclick,bgcolour,checkvar,chancevar,fst
    if uclick and fst:
        window.geometry("1140x700")
        psv=tk.StringVar()
        nmv=tk.StringVar()
        bgcolour=tk.StringVar()
        chancevar = tk.IntVar()
        psv.set(setting['key'])
        nmv.set(setting['name'])
        bgcolour.set(setting['background'].replace('#',''))
        chancevar.set(setting['chance'])
        tk.Label(window, text="Set password",fg = fontcolour,bg=setting['background'],bd=5,font=('consolas',10)).pack(side=tk.TOP)
        pse=tk.Entry(window,textvariable=psv,font=('consolas',10), width = 30)
        pse.pack(side=tk.TOP)
        tk.Label(window, text="Set file name",fg = fontcolour,bg=setting['background'],bd=5,font=('consolas',10)).pack(side=tk.TOP)
        nme=tk.Entry(window,textvariable=nmv,font=('consolas',10), width = 30)
        nme.pack(side=tk.TOP)
        tk.Label(window, text="Set background colour",fg = fontcolour,bg=setting['background'],bd=5,font=('consolas',10)).pack(side=tk.TOP)
        cle=tk.Entry(window,textvariable=bgcolour,font=('consolas',10), width = 30)
        cle.pack(side=tk.TOP)
        tk.Label(window, text="Set the chance to try",fg = fontcolour,bg=setting['background'],bd=5,font=('consolas',10)).pack(side=tk.TOP)
        che=tk.Entry(window,textvariable=chancevar,font=('consolas',10), width = 30)
        che.pack(side=tk.TOP)
        checkvar = tk.IntVar()
        checking = tk.Checkbutton(window, text = "Remove UI",fg = fontcolour,bg=setting['background'], variable = checkvar, onvalue = 1, offvalue = 0, height=1, width = 20)
        checking.pack(side=tk.TOP)
        tk.Button(window,text='Save for this time',fg = fontcolour,bg=setting['background'],command=getset,width=14).pack(side=tk.LEFT)
        tk.Button(window,text='Save as default',fg = fontcolour,bg=setting['background'],command=getdef,width=14).pack(side=tk.LEFT)
        uclick = False
        fst = False
        window.update()
    elif uclick and not(fst):
        window.geometry("1140x700")
        uclick = False
        window.update()
    else:
        window.geometry("840x630")
        uclick = True
        window.update()
def getset():
    gkey = psv.get()
    #print(psv.get())
    gname = nmv.get()
    gbgcl = bgcolour.get()
    ifui = checkvar.get()
    try:chance = chancevar.get()
    except:
        messagebox.showerror('Error','[ERROR]:Expected floating-point number but got a string.')
        chancevar.set(setting['chance'])
        chance = chancevar.get()
    #print(gbgcl)
    if gkey != '':setting['key'] = gkey
    else:
        setting['key'] = gkey
        setting['ifkey'] = False
    if gname != '':setting['name'] = gname
    if gbgcl != '' and setting['background'] != '#' + gbgcl:
        messagebox.showinfo('imformation','Restart to load the background colour.')
        setting['background'] = '#' + gbgcl
    if ifui == 0:setting['ifui'] = True
    else:setting['ifui'] = False
    setting['chance'] = int(chance)
    print(setting)
    window.update()
def getdef():
    global psv,nmv,window
    getset()
    grand = open('loc.set','w')
    grand.write(str(setting))
    grand.close()
uclick = True
fst = True
ph_open = tk.PhotoImage(file='./icon/open.png')
ph_del = tk.PhotoImage(file='./icon/del.png')
ph_pac = tk.PhotoImage(file='./icon/pac.png')
ph_opt = tk.PhotoImage(file='./icon/opt.png')
tk.Label(window, text="File Packager",fg = fontcolour,bg=setting['background'],bd=10,font=('consolas',30)).pack()
scy = tk.Scrollbar(window)
scy.pack(side=tk.RIGHT,fill=tk.Y)
msgw = tk.Listbox(window,width=80,height=10,fg = fontcolour,bg=setting['background'],font=('consolas',20),relief='sunken',yscrollcommand=scy.set,selectmode=tk.EXTENDED)
msgw.pack()
scx = tk.Scrollbar(window,orient='horizontal')
scx.pack(fill=tk.X)
msgw.config(xscrollcommand=scx.set)
scy.config(command=msgw.yview)
scx.config(command=msgw.xview)
pa = tk.ttk.Progressbar(window,length=800)
pa.pack(side=tk.TOP,pady=5)
pa['maximum'] = 100
pa['value'] = 0
tk.Button(window,width=200,height=124,image=ph_open,relief='ridge',command=opfile).pack(side=tk.LEFT)
tk.Button(window,width=200,height=124,image=ph_del,relief='ridge',command=delete).pack(side=tk.LEFT)
tk.Button(window,width=200,height=124,image=ph_pac,relief='ridge',command=run).pack(side=tk.LEFT)
tk.Button(window,width=200,height=124,image=ph_opt,relief='ridge',command=setop).pack(side=tk.LEFT)
window.mainloop()