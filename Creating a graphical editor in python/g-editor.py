from tkinter import Frame, Canvas, Button, Tk, filedialog, Scrollbar, Label, messagebox
from PIL import ImageTk, Image
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.create_menu()
        
        self.image = None
        self.photo = None
        
        self.display = Canvas(self.parent, width=400, height=400, bg="gray")
        self.display_img = self.display.create_image(0, 0)
        self.display.pack()
        
    def open(self):
        self.filename = filedialog.askopenfilename()
        
        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        
        self.scr1 = Scrollbar(root,command=self.display.yview, orient='vertical')
        self.scr1.place(x = 133, y = 3)
        
        self.scr2 = Scrollbar(root,command=self.display.xview, orient="horizontal")
        self.scr2.place(x = 145, y = 452)
        
    def save(self):
        pass
    
    def clear(self):
        pass

    def close(self):
        pass

    def create_menu(self):
        label_fail = Label(root, text = 'Параметры файла')
        label_fail.place(x = 22, y = 30)
        
        self.btn_open = Button(text="Открыть", height = 2, width = 12, command=self.open)
        self.btn_open.place(x = 25, y = 60)
        
        self.btn_save = Button(text="Сохранить", height = 2, width = 12, command=self.save,
        state='disabled')
        self.btn_save.place(x = 25, y = 105)

        self.btn_clear = Button(text = 'Очистить', height = 2, width= 12, command=self.clear,
        state="disabled")
        self.btn_clear.place(x=25, y=150)

        self.btn_close = Button(text = 'Очистить', height = 2, width= 12, command=self.close,
        state="disabled")
        self.btn_close.place(x=25, y=205)
        
        
 
if __name__ == '__main__':
    root = Tk()
    root.title("Графический редактор")
    root.geometry("825x500+250+100")
    app = Example(root)
    root.mainloop()
