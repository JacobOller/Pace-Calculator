import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.properties import StringProperty


kivy.require("2.3.0")
Window.clearcolor = 0, .5, 1, 1


class picturebackground(Widget):
    pass


class InitialScreen(Screen):
    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)
        self.picture = picturebackground()
        self.add_widget(self.picture)

    def presslower(self, *args, **kwargs):
        eventpresslower = None
        if kwargs['event'] == '600':
            eventpresslower = 'event600'
        if kwargs['event'] == '800':
            eventpresslower = 'event800'
        if kwargs['event'] == '1000':
            eventpresslower = 'event1000'
        if kwargs['event'] == '1mile':
            eventpresslower = 'event1mile'
        App.get_running_app().root.current = 'calculatorbelow_screen'
        self.manager.get_screen('calculatorbelow_screen').eventpresslower = eventpresslower

    def pressabove(self,**kwargs):
        if kwargs['event'] == '5000':
            eventpressupper = 'event5000'
        if kwargs['event'] == '10000':
            eventpressupper = 'event10000'
        App.get_running_app().root.current = 'calculatorabove_screen'
        self.manager.get_screen('calculatorabove_screen').eventpressupper = eventpressupper


class CalculatorScreenBelowMile(Screen):
    eventpresslower = StringProperty('')
    user_time = StringProperty('')
    #yellow = [255,255,102,1]
    def __init__(self, **kwargs):
        super(CalculatorScreenBelowMile, self).__init__(**kwargs)
        self.picture = picturebackground()
        self.add_widget(self.picture)
    def m_to_s(self,time):
        m, s = time.split(':')
        return int(m) * 60 + int(s)

    def press_calculate_below(self, **kwargs):
        #user_time = StringProperty('')
        splitslist = []
        userevent = self.eventpresslower
        user_time = self.ids.inputbelow.text
        resultsbelow = self.m_to_s(user_time)
        if userevent == 'event600':
            splitsdividing = [6, 3, 2, 1.5]
        if userevent == 'event800':
            splitsdividing = [8,4,2.67,2]
        if userevent == 'event1000':
            splitsdividing = [10, 5, 3.33, 2.5]
        if userevent == 'event1mile':
            splitsdividing = [16, 8, 5.33, 4]

        for i in splitsdividing:
            results = float(resultsbelow)
            results = results / i
            results = int(results)
            results = str(results)
            splitslist.append(results)
            print(splitslist)
        self.ids.event100split.text = (splitslist[0])
        self.ids.event200split.text = (splitslist[1])
        self.ids.event300split.text = (splitslist[2])
        self.ids.event400split.text = splitslist[3]

    def press_return(self, **kwargs):
        App.get_running_app().root.current = "initial"


class CalculatorScreenAboveMile(Screen):    #Have not started on this yet
    eventpressupper = StringProperty('')
    user_time = StringProperty('')
    def __init__(self, **kwargs):
        super(CalculatorScreenAboveMile, self).__init__(**kwargs)
        self.picture = picturebackground()
        self.add_widget(self.picture)
    def m_to_s(self, time):
        m, s = time.split(':')
        return int(m) * 60 + int(s)

    def s_to_m(self,timefinal):
        timefinal = float(timefinal)
        t = timefinal / 60
        seconds = t % 1
        s = seconds * 60
        m = t // 1
        m = int(m)
        s = int(s)
        return "{}:{}".format(m,s)

    def press_calculate_above(self, **kwargs):
        # user_time = StringProperty('')
        splitslist = []
        userevent = self.eventpressupper
        user_time = self.ids.inputabove.text
        resultsabove = self.m_to_s(user_time)
        if userevent == 'event5000':
            splitsdividing = [12.5, 6.25, 4.167, 3.125]
        if userevent == 'event10000':
            splitsdividing = [25, 12.5, 8.334, 6.25]

        for i in splitsdividing:
            results = float(resultsabove)
            results = results / i
            results = int(results)
            results = str(results)
            splitslist.append(results)
            print(splitslist)
        self.ids.event400split.text = (splitslist[0])
        splitslist[1] = self.s_to_m(splitslist[1])
        self.ids.event800split.text = (splitslist[1])
        splitslist[2] = self.s_to_m(splitslist[2])
        self.ids.event1200split.text = (splitslist[2])
        splitslist[3] = self.s_to_m(splitslist[3])
        self.ids.event1600split.text = splitslist[3]

    def press_return(self, **kwargs):
        App.get_running_app().root.current = "initial"


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('pacemain.kv')


class MainApp(App):
    def build(self):
        return kv


if __name__=="__main__":
    MainApp().run()