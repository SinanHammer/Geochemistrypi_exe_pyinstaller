import pyautogui
import time
print(pyautogui.size())
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
import os
import  pyperclip

# 获取当前地址
current_directory = os.getcwd()
print("当前工作目录是：", current_directory)

##### 安装python

#第一步
# while True:
#     button_location1 = pyautogui.locateOnScreen('.\\picture\\1.png', confidence=0.8)
#     if button_location1 is not None:
#         button_point1 = pyautogui.center(button_location1)
#         x, y = button_point1
#         pyautogui.doubleClick(x, y)
#         time.sleep(1.8)
#         monitor1 = pyautogui.locateOnScreen('.\\picture\\1.1.png', confidence=0.8)
#         if monitor1 is not None:
#             break
#     else:
#         print("未找到python3.9.exe文件！！！")
#
#
# # 第二步
# while True:
#     button_location2 = pyautogui.locateOnScreen('.\\picture\\2.png', confidence=0.8)
#     if button_location2 is not None:
#         button_point2 = pyautogui.center(button_location2)
#         x, y = button_point2
#         pyautogui.click(x, y)
#         time.sleep(1.2)
#         monitor2 = pyautogui.locateOnScreen('.\\picture\\2.1.png', confidence=0.8)
#         if monitor2 is not None:
#             break
#         break
#     else:
#         print("未找到添加到系统路径的按钮 ！！！")
#
#
# # 第三步
# while True:
#     button_location3 = pyautogui.locateOnScreen('.\\picture\\3.png', confidence=0.8)
#     if button_location3 is not None:
#         button_point3 = pyautogui.center(button_location3)
#         x, y = button_point3
#         pyautogui.click(x, y)
#         time.sleep(1.2)
#         monitor3 = pyautogui.locateOnScreen('.\\picture\\3.1.png', confidence=0.8)
#         if monitor3 is not None:
#             break
#     else:
#         print("未找到安装按钮 ！！！")
#
#
# # 第四步
# while True:
#     button_location4 = pyautogui.locateOnScreen('.\\picture\\4.png', confidence=0.8)
#     if button_location4 is not None:
#         button_point4 = pyautogui.center(button_location4)
#         x, y = button_point4
#         pyautogui.click(x, y)
#         time.sleep(1.2)
#         monitor4 = pyautogui.locateOnScreen('.\\picture\\4.1.png', confidence=0.8)
#         if monitor4 is not None:
#             break
#     else:
#         print("未找到 Next 按钮 ！！！")
#
#
# # 第五步
# while True:
#     button_location0 = pyautogui.locateOnScreen('.\\picture\\0.png', confidence=0.8)
#     if button_location0 is not None:
#         button_point0 = pyautogui.center(button_location0)
#         x, y = button_point0
#         pyautogui.click(x, y+20)
#         time.sleep(1.2)
#         pyautogui.hotkey("ctrl", "a")
#         pyautogui.press("backspace")
#         current_directory_words = str(current_directory)+"\\python39"
#         pyperclip.copy(current_directory_words)
#         pyautogui.hotkey("ctrl", "v")
#     button_location5 = pyautogui.locateOnScreen('.\\picture\\5.png', confidence=0.8)
#     if button_location5 is not None:
#         button_point5 = pyautogui.center(button_location5)
#         x, y = button_point5
#         pyautogui.click(x, y)
#         time.sleep(1.2)
#         monitor5 = pyautogui.locateOnScreen('.\\picture\\5.1.png', confidence=0.8)
#         if monitor5 is not None:
#             break
#     else:
#         print("未找到 install 按钮 ！！！")
#
# time.sleep(6)
#
# # 第六步
# while True:
#     button_location6 = pyautogui.locateOnScreen('.\\picture\\6.png', confidence=0.8)
#     if button_location6 is not None:
#         button_point6 = pyautogui.center(button_location6)
#         x, y = button_point6
#         pyautogui.click(x, y)
#         time.sleep(1.2)
#         monitor6 = pyautogui.locateOnScreen('.\\picture\\6.1.png', confidence=0.8)
#         if monitor6 is not None:
#             break
#     else:
#         print("未找到 close 按钮 ！！！")
#
# print("已经成功安装 --*** Python ***--")
# time.sleep(2)


###### 安装相关库

# 优化python
rename_fir = "cd" + " " + str(current_directory) + "\\python39"
pyautogui.hotkey("winleft", "r")
pyautogui.typewrite("cmd")
pyautogui.press('enter')
pyautogui.press('enter')
pyperclip.copy(rename_fir)
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')
time.sleep(2)
rename_command = "rename python.exe python39.exe"
pyperclip.copy(rename_command)
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')
time.sleep(2)
rename_command2 = "rename pythonw.exe pythonw39.exe"
pyperclip.copy(rename_command2)
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')
time.sleep(2)
re_pip = "pip39 install --upgrade --force-reinstall " + str(current_directory) + "\\wheel\\pip-23.3-py3-none-any.whl"
pyperclip.copy(re_pip)
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')
time.sleep(2)
rename_pip_dir = "cd" + " " + "Scripts"
rename_pip = "rename pip3.exe pip39.exe"
pyautogui.typewrite(rename_pip_dir)
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite(rename_pip)
pyautogui.press('enter')
time.sleep(8)
pyautogui.typewrite("exit")
pyautogui.press('enter')

# 打开cmd
pyautogui.hotkey("winleft", "r")
pyautogui.typewrite("cmd")
pyautogui.press('enter')
pyautogui.press('enter')

dirs = "cd" + " " + str(current_directory)
pyautogui.typewrite(dirs)
pyautogui.press('enter')

pip_words = "python39 -m pip install --no-index --find-links=wheel -r requirements.txt"
pyautogui.typewrite(pip_words)
pyautogui.press('enter')

# 打开geochemistrypi
next_words = "cd" + " " + "geochemistrypi"
pyautogui.typewrite(next_words)
pyautogui.press('enter')
start_words = "python39 main.py"
pyautogui.typewrite(start_words)
pyautogui.press('enter')


