import tkinter as tk

root = tk.Tk()
root.geometry("250x200")
root.title("Кнопки")
root.configure(background="#003344")

show_button = tk.Button(root, text="Показать", width=12, height=3)
show_button.config(font=("Courier", 15))
show_label = tk.Label(root, bg='#443344', fg='white', width=10, height=2)
show_label.config(font=("Courier", 20))

def show(event):
    num = 111
    show_label['text'] = num


show_label.pack()
show_button.pack()
show_button.bind('<Button-1>', show)

root.mainloop()