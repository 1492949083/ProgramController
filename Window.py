import subprocess
import platform
import os
import yaml
from tkinter import *
from tkinter import ttk
import Controller

# 创建根窗口
root = Tk()
# 设置窗口标题
root.title("程序控制器")
# 设置窗口大小
root.geometry("320x240")

# 读取list.yml文件
with open("list.yml") as file:
    try:
        data = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)
        data = []

# 保存选中的软件路径
selected_programs = []

# 根据list.yml文件创建多选框和按钮
def create_widgets():
    # 创建多选框
    for item in data:
        text = item.get('text', '')
        path = item.get('path', '')
        if text and path:
            var = IntVar()
            checkbox = Checkbutton(root, text=text, variable=var, command=lambda p=path, v=var: handle_checkbox(p, v))
            checkbox.pack()

    # 创建启动、重启和关闭按钮
    start_button = Button(root, text="启动", command=start_programs)
    start_button.pack()
    restart_button = Button(root, text="重启", command=restart_programs)
    restart_button.pack()
    stop_button = Button(root, text="关闭", command=stop_programs)
    stop_button.pack()

# 选中/取消选中多选框时的处理函数
def handle_checkbox(program_path, var):
    if var.get() == 1:
        selected_programs.append(program_path)
    else:
        selected_programs.remove(program_path)

# 启动选中的软件
def start_programs():
    for program_path in selected_programs:
        Controller.set_program_path_and_name(program_path)
        Controller.start_program()

# 重启选中的软件
def restart_programs():
    for program_path in selected_programs:
        Controller.set_program_path_and_name(program_path)
        Controller.restart_program()

# 关闭选中的软件
def stop_programs():
    for program_path in selected_programs:
        Controller.set_program_path_and_name(program_path)
        Controller.stop_program()

# 创建界面组件
create_widgets()

# 启动主事件循环
root.mainloop()
