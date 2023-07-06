import subprocess
import platform
import os


# 传入程序路径,保存程序名和路径
def set_program_path_and_name(program_path):
    program_name = '"' + program_path.split('\\')[-1] + '"'
    global path
    path = program_path
    global name
    name = program_name

# 传入程序路径，打开程序
def start_program():
    subprocess.Popen([path])

    
# 传入程序名，关闭程序
def stop_program():
    os.system('taskkill /f /im ' + name)

# 传入程序名，重启程序
def restart_program():
    stop_program()
    start_program()




