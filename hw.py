import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="LightGoldenrod1")

root = tk.Tk()
root.title("Лист задач") #Название Окна
# background — это атрибут, аргумент функции, который мы можем менять.
# Название цвета, которое можно использовать, мы находим на сайте https://letpy.com/handbook/tkinter-colors/
root.configure(background="grey19") # Меняем цвет баграунд

text1 = tk.Label(root, text="Введеите вашу задачу", bg="grey19", fg='#fff') # bg="grey19" - цвет фона под текстом, fg='#fff' - цвет самого текста
text1.pack(pady=10) #pady — перемещение элементов вверх-вниз, паддинг сверху и снизу;
                    #padx — перемещение элементов влево-вправо, паддинг слева и справа.

task_entry = tk.Entry(root, width=30, bg="grey79")  # Добовляем поле для ввода, width=30 - отступы
task_entry.pack(pady=5)           # Отриссовываем поле для ввода на экране

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task) # Добовляем кнопку
add_task_button.pack(pady=5)                             # Отриссовываем кнопку на экране

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task) # Добовляем кнопку
delete_button.pack(pady=5)              # Отриссовываем кнопку на экране

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task) # Добовляем кнопку
mark_button.pack(pady=5)              # Отриссовываем кнопку на экране

text2 = tk.Label(root, text="Список задач", bg="grey19", fg='#fff')
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="grey99") # Добовляем список
task_listBox.pack(pady=10)

root.mainloop() # Запускаем главный цикл окна, так окно будет отображаться
