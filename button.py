import tkinter as tk

root = tk.Tk()
root.geometry("250x315")
root.title("Кнопки")
root.configure(background="#003344")

show_button = tk.Button(root, text="Показать", width=12, height=3)
show_button.config(font=("Courier", 15))
show_label = tk.Label(root, bg='#443344', fg='white', width=10, height=2)
show_label.config(font=("Courier", 20))

def show(event):
    num = 111
    show_label['text'] = num

show_button.bind('<Button-1>', show)

inc_button = tk.Button(root, text="Увеличить", width=12, height=3)
inc_button.config(font=("Courier", 15))

def inc(event):
    num = show_label['text']
    show_label['text'] = num + 1

inc_button.bind('<Button-1>', inc)

dec_button = tk.Button(root, text="Уменьшить", width=12, height=3)
dec_button.config(font=("Courier", 15))

def вус(event):
    num = show_label['text']
    show_label['text'] = num - 1

dec_button.bind('<Button-1>', вус)

show_label.pack()
show_button.pack()
inc_button.pack()
dec_button.pack()

root.mainloop()