"""
本项目实现了一个计时器程序

注意显示的格式是 00:00:00 分别表示 分:秒:毫秒
毫秒到秒的进位是 1000, 注意换算


为了实现这个程序我们需要以下的功能
1, 获取当下的时间
2, 定时更新时间显示(比如每秒更新 10 次)
3, 按钮和按钮点击事件

    开始按钮开始计时并更新时间显示
    暂停按钮停止计时并定格时间显示
    重置按钮停止计时并重置时间为 00:00:00

"""
from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock


from kivy.metrics import dp
import time

def font_name():
    """
    苹果系统和微软系统需要不同的字体文件
    """
    from sys import platform
    if platform == "darwin":
        return 'Arial Unicode'
    elif platform == "win32":
        return 'SimHei'
    else:
        print('not support')


# 程序一定是一个继承自 App 的 xxApp 类作为起点
class TestApp(App):
    # build 函数是固定的, 它用于生成界面
    def build(self):
        self.config_window()
        self.title = 'Timepiece'
        root = self.setup_ui()
        return root

    def config_window(self):
        """
        这里设置了 3 个属性, 这是固定的写法
        分别是 禁止缩放, 宽度 400, 高度 600
        """
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', 400)
        Config.set('graphics', 'height', 600)

    def setup_ui(self):
        """
        程序窗口必须有一个 layout(布局), 所有的按钮/文本框之类的东西都必须添加在布局中
        使用 floatlayout 它可以自定义控件的尺寸和座标
        """
        layout = FloatLayout(size=(400, 600))
      
        button_config = dict(
            text='start',
            font_size=20,
            pos=(20, 20),
            size=(100, 100),
            size_hint=(None, None),
            font_name=font_name(),  # 字体名字也可以在初始化的时候配置
        )
        button = Button(**button_config)
        button.bind(on_press=self.button_press)
        layout.add_widget(button)
        # 把 result 这个输入框用类的属性存起来之后要使用
        # 类属性在类的任何函数中都可以创建, 并不一定要在 __init__ 中创建
        self.button = button
        self.started = False
        current_time = time.time()
        self.start_time = current_time
        self.gap = 0
        
        button2_config = dict(
            text='pause',
            font_size=20,
            pos=(150, 20),
            size=(100, 100),
            size_hint=(None, None),
            font_name=font_name(),  
        )
        button2 = Button(**button2_config)
        button2.bind(on_press=self.button2_press)
        layout.add_widget(button2)

        button3_config = dict(
            text='reset',
            font_size=20,
            pos=(280, 20),
            size=(100, 100),
            size_hint=(None, None),
            font_name=font_name(),  
        )
        button3 = Button(**button3_config)
        button3.bind(on_press=self.button3_press)
        layout.add_widget(button3)


        label_config = dict(
            text='00:00:00',
            font_size=50,
            halign='center',    # 横向居中显示
        )
        label = Label(**label_config)
        layout.add_widget(label)
        self.label = label
        # 定时器用法
        # 第一个参数是定时会被调用的函数
        # 第二个参数是调用的间隔时间, 单位是秒, 0.1 表示每秒调用 10 次, 这里是 1 表示每秒调用一次
        # Clock.schedule_interval(self.timer, 1)
        Clock.unschedule(self.timer)
        return layout

    # dt 意思是 delta-time, 间隔时间
    def timer(self, dt):
        current_time = time.time()
        dt = current_time - self.start_time + self.gap
        minutes = dt // 60
        seconds = dt % 60
        nanoseconds = dt % 1
        self.label.text = '{:02d}:{:02d}:{:02d}'.format(int(minutes), int(seconds), int(nanoseconds * 100))

       
    def button_press(self, button):
        if not self.started:
            self.started = True
            self.start_time = time.time()
            print('点击按钮', button)
            Clock.schedule_interval(self.timer, 0.1)

    def button2_press(self, button):
        if self.started:
            Clock.unschedule(self.timer)
            self.gap += time.time() - self.start_time
            self.started = False

    def button3_press(self, button):
        Clock.unschedule(self.timer)
        self.started = False
        self.gap = 0
        self.reset_label()

    def reset_label(self):
        self.label.text = '00:00:00'

    def check(self, input):
        print('check, ', input.text)
        s = input.text + '\n' + 'done'
     


def main():
    # 生成 App 并运行
    TestApp().run()


if __name__ == '__main__':
    main()
