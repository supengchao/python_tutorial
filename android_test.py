import os
import time


def main():
    # get_screnncap('caca')
    # android_input_text('hahahhaha')
    # android_input_keyevent(3)
    # android_input_swipe(0, 20, 0, 300)
    # android_pull_file()
    android_density()
    android_devices_info()
    android_devices_size()

def research_adb_command():
    # 尝试用python通过adb命令操作手机
    adb_command_captial = 'adb shell screencap -p /sdcard/test.png'  # 截屏
    adb_command_pull = 'adb pull /sdcard/test.png .'  # 拉取文件
    adb_command_pull_desktop = 'adb pull /sdcard/test.png ~/Desktop/'  # 拉取文件
    adb_command_pull_desktop = 'adb pull /sdcard/.WL ~/Desktop/Log/'  # 拉取文件
    adb_command_pull_log = 'adb pull /sdcard'
    os.system(adb_command_captial)
    print('开始截屏')
    time.sleep(3)
    print('开始拉取截屏')
    os.system(adb_command_pull_desktop)
    print('更新完成')


def android_input_tap(x, y):
    # 模拟点击（x,y）
    adb_command_tap = 'adb shell input tap {} {}'.format(x, y)
    os.system(adb_command_tap)


def android_input_swipe(x1, y1, x2, y2):
    # 模拟滑动，从（x1,y1）点滑到（x2,y2）点
    adb_command_input_swipe = 'adb shell input swipe {} {} {} {}'.format(x1, y1, x2, y2)
    os.system(adb_command_input_swipe)


def android_input_keyevent(key):
    '''
  1	按menu键	KEYCODE_MENU
3	按home键	KEYCODE_HOME
4	按back键	KEYCODE_BACK
21	光标左移	KEYCODE_DPAD_LEFT
22	光标右移	KEYCODE_DPAD_RIGHT
67	按删除按钮	KEYCODE_DEL
    '''
    adb_command_input_keyevent = 'adb shell input keyevent {}'.format(key)
    os.system(adb_command_input_keyevent)


def android_input_text(text):
    # 模拟输入文本
    adb_command_input_text = 'adb shell input text {}'.format(text)
    os.system(adb_command_input_text)


def android_get_screnncap(filename):
    # 拉取手机截图到sdcard
    adb_command_screencap = 'adb shell screencap -p /sdcard/{}.png'.format(filename)
    os.system(adb_command_screencap)

def android_pull_screnncap_to_current_path(filename):
    # 抓取日志到当前目录
    adb_command_pull_log = 'adb pull /sdcard/{}.png .'.format(filename)
    os.system(adb_command_pull_log)


def android_pull_file_to_current_path():
    # 抓取日志到当前目录
    adb_command_pull_log = 'adb pull /sdcard/.WL .'
    os.system(adb_command_pull_log)

def android_pull_file():
    # 抓取日志到/User/{username}目录
    adb_command_pull_log = 'adb pull /sdcard/.WL ~/'
    os.system(adb_command_pull_log)

def android_pull_log_to_desktop():
    # 抓取日志包到桌面的Log文件夹中
    adb_command_pull_log = 'adb pull /sdcard/.WL ~/Desktop/Log/'
    os.system(adb_command_pull_log)

def android_devices_size():
    #手机尺寸
    size_str = os.popen('adb shell wm size').read()
    print(size_str.strip())

def android_devices_info():
    #设备信息
    devices_str = os.popen('adb shell getprop ro.product.model').read()
    print(devices_str.strip())

def android_density():
    #屏幕密度
    density = os.popen('adb shell wm density').read()
    print(density.strip())

if __name__ == '__main__':
    main()
