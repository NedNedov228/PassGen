from tkinter import *
from tkinter import ttk
import functions as f
import accountsList as al
from accounts import global_password
# from encryption import set_password

# def create_account_frame(label_text):
#     frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
#     # добавляем на фрейм метку
#     label = ttk.Label(frame, text=label_text)
#     label.pack(anchor=NW)
#     # добавляем на фрейм текстовое поле
#     entry = ttk.Entry(frame)   
#     entry.pack(anchor=NW)
#     # возвращаем фрейм из функции
#     return frame


def main():
    password = ""
    root = Tk()
    root.title("PassGen")
    root.geometry("400x500+500+100")
    root.resizable(False, False)
    # root.attributes("-toolwindow", True)
    root.iconbitmap("icon.ico")

    logo = PhotoImage(file="icon.png")
    
    errmsg = StringVar()

    logo = logo.subsample(2,2)
    logo_label = ttk.Label(root, image=logo,text="PassGen", compound=LEFT, padding=8, foreground="#777777", font= "20")
    logo_label.pack()

    acc_text = ttk.Label(root, text="Enter the password to get access to the account list:", padding=8)
    acc_text.pack()
    entry = ttk.Entry(show="•",justify=CENTER)
    entry.pack()


    # if global_password == "":
    #     acc_text['text'] = "Set the password to get access to the account list:"
    #     set_password(entry.get())

    def login(event=None):
        password = entry.get()  # Get the entered password
        entry.delete(0, END)  # Delete the entered password
        # Check if the username and password are correct
        if password == global_password:
            al.accountsList()
        else:
            errmsg.set("Invalid username or password.")



    entry.bind("<Return>", login)
    error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
    error_label.pack(padx=5, pady=5, anchor=NW)
    label = ttk.Label(text=f"{password}", padding=8)
    label.pack(expand=True)
    btn = ttk.Button(root, text="Generate", command=lambda: label.config(text=f.generate_password(16)))
    btn.pack()
    copy_btn = ttk.Button(root, text="Copy", command=lambda: f.copy_to_clipboard(root, label["text"]))
    copy_btn.pack(pady=8)
    
   


    mainloop()


if __name__ == "__main__":
    main()