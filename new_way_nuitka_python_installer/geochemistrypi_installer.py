import pyautogui
import time
import os
import pyperclip
import platform
import sys


class Gpyinstaller(object):
    def __init__(self):
        self.current_directory = None
        self.rename_fir = None
        self.rename_command = "rename python.exe python39.exe"
        self.rename_command2 = "rename pythonw.exe pythonw39.exe"
        self.re_pip = None
        self.rename_pip_dir = "cd Scripts"
        self.rename_pip = "rename pip3.exe pip39.exe"
        self.dirs = None
        self.pip_words = "python39 -m pip install --no-index --find-links=wheel -r requirements.txt"
        self.next_words = "cd geochemistrypi"
        self.start_words = "python39 main.py"
        self.python_monitor = False
        self.install_python_monitor = 0
        self.install_python_monitor_binary = 0  # 判断是否直接运行

    def envs_test(self):
        # 获取当前地址
        self.current_directory = os.getcwd()
        python_version = platform.python_version()
        if python_version == "3.9.5":
            self.install_python_monitor_binary = -1
            self.current_directory = os.path.dirname(sys.executable)
        print("The current working directory is: ", self.current_directory)
        self.rename_fir = "cd" + " " + str(self.current_directory) + "\\python39"
        self.re_pip = "python39 -m pip install --upgrade --force-reinstall " + str(self.current_directory)\
                      + "\\wheel\\pip-23.3-py3-none-any.whl"
        self.dirs = "cd" + " " + str(self.current_directory)
        print(pyautogui.size())
        pyautogui.PAUSE = 0.1
        pyautogui.FAILSAFE = True

    def python_condition_monitoring(self):
        folder_path = os.getcwd()
        if self.install_python_monitor_binary == -1:
            pass
        else:
            for foldername, subfolders, filenames in os.walk(folder_path):
                if 'python39.exe' in filenames:
                    self.install_python_monitor = self.install_python_monitor + 1
                if 'pythonw39.exe' in filenames:
                    self.install_python_monitor = self.install_python_monitor + 1
                if 'python.exe' in filenames:
                    self.install_python_monitor = self.install_python_monitor + 2
                if 'pythonw.exe' in filenames:
                    self.install_python_monitor = self.install_python_monitor + 2
                if self.install_python_monitor == 2:
                    self.install_python_monitor_binary = 1
                    print("The environment meets the operating conditions！")
                    break
                if self.install_python_monitor == 4:
                    self.install_python_monitor_binary = 2
                    print("The environment meets the operating conditions！")
                    break

    def traversal_picture(self, directory):
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                button_location = pyautogui.locateOnScreen(os.path.join(directory, filename), confidence=0.75)
                if button_location:
                    break
        return button_location

    def python_installer(self):
        ##### 安装python
        #第一步
        while True:
            button_location1 = self.traversal_picture(str(self.current_directory) + "\\picture\\1")
            if button_location1 is not None:
                self.python_monitor = True
                button_point1 = pyautogui.center(button_location1)
                x, y = button_point1
                pyautogui.doubleClick(x, y)
                time.sleep(1.8)
                monitor1 = self.traversal_picture(str(self.current_directory) + "\\picture\\1.1")
                if monitor1 is not None:
                    print("The python3.9.exe file has been found ！！！")
                    break
            else:
                print("The python3.9.exe file was not found ！！！")

        # 第二步
        while True:
            button_location2 = self.traversal_picture(str(self.current_directory) + "\\picture\\2")
            if button_location2 is not None:
                button_point2 = pyautogui.center(button_location2)
                x, y = button_point2
                pyautogui.click(x, y)
                time.sleep(1.2)
                monitor2 = self.traversal_picture(str(self.current_directory) + "\\picture\\2.1")
                if monitor2 is not None:
                    print("The Add to Path button has been found ！！！")
                    break
            else:
                print("The add to Path button was not found ！！！")

        # 第三步
        while True:
            button_location3 = self.traversal_picture(str(self.current_directory) + "\\picture\\3")
            if button_location3 is not None:
                button_point3 = pyautogui.center(button_location3)
                x, y = button_point3
                pyautogui.click(x, y)
                time.sleep(1.2)
                monitor3 = self.traversal_picture(str(self.current_directory) + "\\picture\\3.1")
                if monitor3 is not None:
                    print("The next button is found ！！！")
                    break
            else:
                print("The next button was not found ！！！")

        # 第四步
        while True:
            button_location4 = self.traversal_picture(str(self.current_directory) + "\\picture\\4")
            if button_location4 is not None:
                button_point4 = pyautogui.center(button_location4)
                x, y = button_point4
                pyautogui.click(x, y)
                time.sleep(1.2)
                monitor4 = self.traversal_picture(str(self.current_directory) + "\\picture\\4.1")
                if monitor4 is not None:
                    print("The Next button is found ！！！")
                    break
            else:
                print("The Next button is not found ！！！")

        # 第五步
        while True:
            button_location0 = self.traversal_picture(str(self.current_directory) + "\\picture\\0")
            if button_location0 is not None:
                button_point0 = pyautogui.center(button_location0)
                x, y = button_point0
                pyautogui.click(x, y+20)
                time.sleep(1.2)
                pyautogui.hotkey("ctrl", "a")
                pyautogui.press("backspace")
                current_directory_words = str(self.current_directory)+"\\python39"
                pyperclip.copy(current_directory_words)
                pyautogui.hotkey("ctrl", "v")
            button_location5 = self.traversal_picture(str(self.current_directory) + "\\picture\\5")
            if button_location5 is not None:
                button_point5 = pyautogui.center(button_location5)
                x, y = button_point5
                pyautogui.click(x, y)
                time.sleep(1.2)
                monitor5 = self.traversal_picture(str(self.current_directory) + "\\picture\\5.1")
                if monitor5 is not None:
                    print("The install button has been found ！！！")
                    break
            else:
                print("The install button is not found ！！！")
        time.sleep(18)

        # 第六步
        while True:
            button_location6 = self.traversal_picture(str(self.current_directory) + "\\picture\\6")
            if button_location6 is not None:
                button_point6 = pyautogui.center(button_location6)
                x, y = button_point6
                pyautogui.click(x, y)
                print("The close button has been found ！！！")
                time.sleep(1.2)
                break
            else:
                print("The close button is not found ！！！")
                time.sleep(3)

        print("Successfully installed - Python -  ")
        time.sleep(2)

    def start_cmd(self):
        directory = os.getcwd()
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("cmd")
        pyautogui.press('enter')
        time.sleep(0.5)
        pyperclip.copy("cd " + str(directory))
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')

    def library_installer(self):
        ###### 安装相关库
        # 优化python
        print("--* Go to Step 2 to install the dependency packages *--")
        self.start_cmd()
        pyperclip.copy(self.rename_fir)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite(self.rename_command)
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.typewrite(self.rename_command2)
        pyautogui.press('enter')
        time.sleep(1.5)
        pyperclip.copy(self.re_pip)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
        time.sleep(2.5)

        pyautogui.typewrite(self.rename_pip_dir)
        pyautogui.press('enter')
        time.sleep(1.5)
        pyautogui.typewrite(self.rename_pip)
        pyautogui.press('enter')
        time.sleep(0.8)
        pyautogui.typewrite("exit")
        pyautogui.press('enter')

        # 打开cmd
        pyautogui.hotkey("winleft", "r")
        pyautogui.typewrite("cmd")
        pyautogui.press('enter')
        time.sleep(0.8)
        pyautogui.typewrite(self.dirs)
        pyautogui.press('enter')
        time.sleep(1.8)
        pyautogui.typewrite(self.pip_words)
        pyautogui.press('enter')
        time.sleep(10)

    def gpy_start(self):
        # 打开geochemistrypi
        print("---* Geochemistry π is opening *---")
        pyautogui.press('enter')
        pyautogui.typewrite(self.next_words)
        pyautogui.press('enter')
        pyautogui.typewrite(self.start_words)
        pyautogui.press('enter')



installer = Gpyinstaller()
installer.envs_test()
installer.python_condition_monitoring()
print(f"The running situation is {installer.install_python_monitor_binary}")
if installer.install_python_monitor_binary == 1:
    installer.start_cmd()
    installer.gpy_start()
elif installer.install_python_monitor_binary == 2:
    installer.library_installer()
    installer.gpy_start()
elif installer.install_python_monitor_binary == 0:
    installer.python_installer()
    installer.library_installer()
    installer.gpy_start()
elif installer.install_python_monitor_binary == -1:
    installer.library_installer()
    installer.gpy_start()
else:
    print("Error !")