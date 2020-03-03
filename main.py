#############################################################
# File Name : main.py
# PhysicsCalc is a General Physics Calculator
#############################################################
from Keypad import OSKeypad
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput

#  Window.size = (500, 650)  # Tablet Ratio  (Width 768 x Height 1000)
#  Window.size = (350, 650)  # Phone Ratio  (Width 1080 x Height 2004)

##############################################################
##############################################################
class T_Class(TextInput):
    ############################################
    # Static Class Variables
    csOSKeypad = OSKeypad()
    ################################################
    def __init__(self, **kwargs):
        # Button Events:  on_press  on_release
        # Widget Events:  on_touch_down  on_touch_up  on_touch_move
        super(T_Class, self).__init__(**kwargs)
        self.bind(on_touch_down = self.callback_Touched)
        self.bind(on_text_validate = self.callback_Validate)
        self.coUID = 'String'
        self.coUID_Holder = self.coUID
        return
    ################################################
    def callback_Touched(self, instance, touch):
        # Scan Through All Child Widgets to see which one was Touched
        mStr = ''
        for child in LayoutsApp.csParent.children:
            if(child.collide_point(touch.x, touch.y)):
                mStr = child.coUID
                child.coUID_Holder = mStr
                # Display the Keypad if it's not already displayed
                if(OSKeypad.csIsKeypadDisplayed == False):
                    OSKeypad.csIsKeypadDisplayed = True
                    #########################################
                    # create an object of class OSCalculator
                    # and set the FloatLayout property so
                    # we can add Buttons and add other
                    # Widgets inside the Window
                    child.csOSKeypad = T_Class.csOSKeypad
                    child.csOSKeypad.Set_OSKDisplay(self.get_parent_window(),\
                                                   LayoutsApp.csChildLayout,\
                                                   Window, child.x, child.y)
                    child.csOSKeypad.Display_OSKeypad()
                    child.csOSKeypad.Set_TextDisplay(child)
                    #########################################
                break
        return
    ################################################
    def callback_Validate(self, value):
        for child in LayoutsApp.csParent.children:
            if(child.coUID == child.coUID_Holder):
                OSKeypad.csIsKeypadDisplayed = False
                child.csOSKeypad.Disappear_OSKeypad()
                child.get_parent_window().remove_widget(LayoutsApp.csChildLayout)
        return
    ################################################
    
##############################################################
##############################################################
class LayoutsApp(App):
    #############################################
    # Static Class Variables
    csParent = Widget()
    csChildLayout  = RelativeLayout()
    #############################################
    def __init__(self, **kwargs):
        # Button Events:  on_press  on_release
        # Widget Events:  on_touch_down  on_touch_up  on_touch_move
        super(LayoutsApp, self).__init__(**kwargs)
        return
    #############################################
    def build(self):
        #########################################
        w1 = Window.width
        ftmp = w1 / 4.0
        w1 = int(ftmp)
        h1 = Window.height
        ftmp = h1 / 20.0
        h1 = int(ftmp)
        ftmp = Window.width / 100.0
        Xo = int(ftmp)
        ftmp = Window.height / 100.0
        Yo = int(ftmp)
        #########################################
        T1 = T_Class()
        T1.coUID = 'TInput1'
        T1.text = '3.14'
        T1.size_hint = (None, None)
        T1.width  = w1
        T1.height = h1
        X = Xo * 5
        Y = Yo * 80
        T1.x = X
        T1.y = Y
        ftmp = (h1 * 0.5)
        T1.font_size = int(ftmp)
        T1.multiline = False
        T1.readonly = True
        LayoutsApp.csParent.add_widget(T1)
        #########################################
        T2 = T_Class()
        T2.coUID = 'TInput2'
        T2.text = '0.005'
        T2.size_hint = (None, None)
        T2.width  = w1
        T2.height = h1
        X = Xo * 50
        Y = Yo * 60
        T2.pos  = (X, Y)
        ftmp = (h1 * 0.5)
        T2.font_size = int(ftmp)
        T2.multiline = False
        T2.readonly = True
        LayoutsApp.csParent.add_widget(T2)
        #########################################
        T3 = T_Class()
        T3.coUID = 'TInput3'
        T3.text = '-9.776'
        T3.size_hint = (None, None)
        T3.width  = w1
        T3.height = h1
        X = Xo * 10
        Y = Yo * 40
        T3.pos  = (X, Y)
        ftmp = (h1 * 0.5)
        T3.font_size = int(ftmp)
        T3.multiline = False
        T3.readonly = True
        LayoutsApp.csParent.add_widget(T3)
        #########################################
        return LayoutsApp.csParent
    #############################################
    
##############################################################
##############################################################
    
if __name__ == "__main__":
    LayoutsApp().run()
    
