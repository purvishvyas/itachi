# GUI - Graphical User Interphase

# Liberarirs
########################
# 1. Tkinter
# 2. PyQt
# 3. Turtle

import tkinter as ttk
app = ttk.Tk()
app.title('my app')
app.geometry('600x400')
msg = ttk.Variable(app)
print(msg.get())
ttk.Label(app, text = 'A Simple Text Label').place(x=50,y=50) 
ttk.Label(app, textvariable=msg).place(x=100,y=70)

def abc():
    print('wow')
    msg.set()
    ttk.Button(app,text = 'Isko Click Karo',Command=abc).place(x=100,y=100)
    ttk.Button(app,text = 'Yeh Wala Bhi Hai',Command=lambda:msg.set('pata nhi')).place(x=100,y=150)
    app.mainloop()