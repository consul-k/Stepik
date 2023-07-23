from tkinter import Frame, Canvas, Button, Tk, filedialog, Scrollbar, Label, Menu
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

    def brightness_click(self):
        pass

    def contrast_click(self):
        pass

    def rgb_balans_click(self):
        pass

    def choice_big(self):
        pass

    def choice_small(self):
        pass
    
    def choice_rotation(self):
        pass
    
    def negativ_clic(self):
        pass

    def rnd_noise_click(self):
        pass

    def gray_click(self):
        pass

    def sepia_click(self):
        pass

    def black_white_click(self):
        pass

    def rnd_red_click(self):
        pass

    def rnd_green_click(self):
        pass

    def rnd_blue_click(self):
        pass

    def rnd_biruza_click(self):
        pass

    def rnd_fiol_click(self):
        pass

    def rnd_lilov_click(self):
        pass

    def random_color_click(self):
        pass

    def create_menu(self):
        menu = Menu(self.parent)
        self.file_menu = Menu(menu)
        self.filters_menu = Menu(menu)
        self.parametr_menu = Menu(menu)

        menu.add_cascade(label="Файл", menu=self.file_menu)
        menu.add_cascade(label="Параметры", menu=self.parametr_menu)
        menu.add_cascade(label="Фильтры", menu=self.filters_menu)
        
        self.file_menu.add_command(label="Открыть", command=self.open)
        self.file_menu.add_command(label="Сохранить", command=self.save, state='disabled')
        self.file_menu.add_command(label="Очистить", command=self.clear, state='disabled')
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.close)

        self.parametr_menu.add_command(label="Яркость", command=self.brightness_click,
        state='disabled')
        self.parametr_menu.add_command(label="Контрастность",
        command=self.contrast_click, state='disabled')
        self.parametr_menu.add_command(label="Цветовой баланс",
        command=self.rgb_balans_click, state='disabled')
        self.parametr_menu.add_command(label="Увеличить", command=self.choice_big,
        state='disabled')
        self.parametr_menu.add_command(label="Уменьшить", command=self.choice_small,
        state='disabled')
        self.parametr_menu.add_command(label="Повернуть", command=self.choice_rotation,
        state='disabled')
        
        self.filters_menu.add_command(label="Негатив", command=self.negativ_clic,
        state='disabled')
        self.filters_menu.add_command(label="Шум", command=self.rnd_noise_click,
        state='disabled')
        self.filters_menu.add_command(label="Оттенки серого", command=self.gray_click,
        state='disabled')
        self.filters_menu.add_command(label="Сепия", command=self.sepia_click,
        state='disabled')
        self.filters_menu.add_command(label="Черно-белый",
        command=self.black_white_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки красного",
        command=self.rnd_red_click, state='disabled')
        
        self.filters_menu.add_command(label="Оттенки зеленого",
        command=self.rnd_green_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки синего",
        command=self.rnd_blue_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки бирюзового",
        command=self.rnd_biruza_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки фиолетового",
        command=self.rnd_fiol_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки лилового",
        command=self.rnd_lilov_click, state='disabled')
        self.filters_menu.add_command(label="Случайные цвета",
        command=self.random_color_click, state='disabled')   
        

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
        
        self.parent.config(menu=menu)
 
if __name__ == '__main__':
    root = Tk()
    root.title("Графический редактор")
    root.geometry("825x500+250+100")
    app = Example(root)
    root.mainloop()
