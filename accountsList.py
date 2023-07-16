from tkinter import *
from tkinter import ttk
from accounts import people
 
def accountsList():
    al = Tk()
    al.tk.call('source', 'azure.tcl')
    al.tk.call('set_theme', 'dark')
    al.title("Accounts List")
    # root.geometry("250x200") 
    al.iconbitmap("icon.ico")
    al.rowconfigure(index=0, weight=1)
    al.columnconfigure(index=0, weight=1)
    
    

    columns = ("servicename", "username", "email" , "password")
    
    tree = ttk.Treeview(master=al,columns=columns, show="headings")
    tree.grid(row=0, column=0, sticky="nsew")
    

    tree.heading("servicename", text="Имя сервиса", anchor=W)
    tree.heading("username", text="Имя Пользователя", anchor=W)
    tree.heading("email", text="Email", anchor=W)
    tree.heading("password", text="Пароль", anchor=W)

    
    tree.column("#1", stretch=NO, width=100)
    tree.column("#2", stretch=NO, width=150)
    tree.column("#3", stretch=NO, width=100)
    tree.column("#4", stretch=NO, width=100)

    

    for person in people:
        tree.insert("", END, values=person)
    

    scrollbar = ttk.Scrollbar(master=al,orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")
    
    al.mainloop()


if __name__ == "__main__":
    accountsList()