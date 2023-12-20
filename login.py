from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root =Tk()
root.title('Login')
root.geometry('925x500+150+100')
root.configure(bg='#fff')
root.resizable(False, False)


def sign_in():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == 'password':
        global img2  
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+150+100')
        screen.config(bg='white')
        
        heading2 = Label(screen, text='Welcome to E-Volve!', bg='#fff', fg='#00008B',font=('Calibri(Body)', 25, 'bold'))
        heading2.place(x=300, y=10)

        image2 = Image.open("Images\excess.png")
        resize_image2 = image2.resize((850, 500))
        img2 = ImageTk.PhotoImage(resize_image2)
        Label(screen, image=img2, bg='white').place(x=20,y=50)

        screen.mainloop()



image = Image.open("Images\experience.png")
resize_image = image.resize((500, 500))
img = ImageTk.PhotoImage(resize_image)
Label(root, image=img, bg='white').place(x=20,y=10)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign In', fg='#36454F', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=200, y=5)

###########################------------------------------------------
def on_enter(e): 
    user.delete(0, 'end')

def on_exit(e):
    name=user.get()
    if not name:
        user.insert(0, 'Username')

user =Entry(frame, width=25, fg='#6F4E37', border=0, bg='white', font=('Microsoft Yahei UI Light', 11, 'bold'))
user.place(x=130, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_exit)

Frame(frame, width=295, height=2, bg='#6E260E').place(x=125, y=107)
###########################------------------------------------------
def on_enter_code(e):
    code.delete(0, 'end')

def on_exit_code(e):
    name = code.get()
    if not name:
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='#6F4E37', border=0, bg='white', font=('Microsoft Yahei UI Light', 11, 'bold'))
code.place(x=130, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_code)
code.bind('<FocusOut>', on_exit_code)

Frame(frame, width=295, height=2, bg='#6E260E').place(x=125, y=177)
###########################------------------------------------------
Button(frame, width=20, pady=7, text='Sign in', anchor="center", bg="#E5AA70", fg='white', border=0, cursor='hand2', font=('Microsoft Yahei UI Light', 13, 'bold'), command=sign_in).place(x=135, y=204)
label = Label(frame, text="Don't have an account?", fg='#36454F', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=155, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#8B0000')
sign_up.place(x=295, y=270)



root.mainloop()