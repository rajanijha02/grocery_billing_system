from tkinter import*
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry(1350+700+0+0)
        self.root.title("Billing Software")



root=Tk()
obj = Bill_App(root)
root.mainloop()
