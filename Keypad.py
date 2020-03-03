#############################################################
# File Name : Calculator.py
# PhysicsCalc is a General Physics Calculator
#############################################################
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Color
##############################################################

##############################################################
##############################################################
class OSKeypad():
    #########################################
    # Static Class Variables
    csString = ''
    csTextDisplay = TextInput()
    csPad = 5
    csLayout = RelativeLayout()
    csIsKeypadDisplayed = False
    #############################################
    def __init__(self, **kwargs):
        super(OSKeypad, self).__init__(**kwargs)
        return
    #############################################
    def build(self):
        return
    #############################################
    def Set_OSKDisplay(self, pParent, pLayout, pWindow, pX, pY):
        OSKeypad.csLayout = pLayout
        Height = int(pWindow.height * 0.3) - OSKeypad.csPad - OSKeypad.csPad
        Width = int(pWindow.width * 0.5) - OSKeypad.csPad - OSKeypad.csPad
        pLayout.size_hint = (None, None)
        pLayout.width = Width
        pLayout.height = Height
        X = pX
        Y = pY - Height - OSKeypad.csPad
        pLayout.pos = (X, Y)
        pLayout.canvas.add(Color(0, 0, 1, 1))
        pLayout.canvas.add(Rectangle(pos=(0, 0), size=(Width,Height)))
        pParent.add_widget(pLayout)
        return
    #############################################
    def Set_TextDisplay(self, pDisplay):
        OSKeypad.csTextDisplay = pDisplay
        OSKeypad.csString = OSKeypad.csTextDisplay.text
        return
    #############################################
    def Disappear_OSKeypad(self):
        OSKeypad.csLayout.clear_widgets()
        return
    #############################################
    def Display_OSKeypad(self):
        #########################################
        X = OSKeypad.csPad
        Y = OSKeypad.csPad
        #########################################
        Button_0 = CButton()
        Button_0.text = '0'
        Button_0.pos = (X, Y)
        Button_0.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_0)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_D = CButton()
        Button_D.text = '.'
        Button_D.pos = (X, Y)
        Button_D.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_D)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_N = CButton()
        Button_N.text = '+/-'
        Button_N.pos = (X, Y)
        Button_N.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_N)
        #########################################
        X = OSKeypad.csPad
        Y = Y + Button_0.height + OSKeypad.csPad
        #########################################
        Button_1 = CButton()
        Button_1.text = '1'
        Button_1.pos = (X, Y)
        Button_1.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_1)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_2 = CButton()
        Button_2.text = '2'
        Button_2.pos = (X, Y)
        Button_2.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_2)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_3 = CButton()
        Button_3.text = '3'
        Button_3.pos = (X, Y)
        Button_3.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_3)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_E = CButton()
        Button_E.text = '='
        Button_E.pos = (X, Y)
        Button_E.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_E)
        #########################################
        X = OSKeypad.csPad
        Y = Y + Button_0.height + OSKeypad.csPad
        #########################################
        Button_4 = CButton()
        Button_4.text = '4'
        Button_4.pos = (X, Y)
        Button_4.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_4)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_5 = CButton()
        Button_5.text = '5'
        Button_5.pos = (X, Y)
        Button_5.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_5)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_6 = CButton()
        Button_6.text = '6'
        Button_6.pos = (X, Y)
        Button_6.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_6)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_C = CButton()
        Button_C.text = 'C'
        Button_C.pos = (X, Y)
        Button_C.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_C)
        #########################################
        X = OSKeypad.csPad
        Y = Y + Button_0.height + OSKeypad.csPad
        #########################################
        Button_7 = CButton()
        Button_7.text = '7'
        Button_7.pos = (X, Y)
        Button_7.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_7)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_8 = CButton()
        Button_8.text = '8'
        Button_8.pos = (X, Y)
        Button_8.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_8)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_9 = CButton()
        Button_9.text = '9'
        Button_9.pos = (X, Y)
        Button_9.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_9)
        #########################################
        X = X + Button_0.width + OSKeypad.csPad
        #########################################
        Button_B = CButton()
        Button_B.text = '<--'
        Button_B.pos = (X, Y)
        Button_B.Set_Properties(OSKeypad.csPad, OSKeypad.csLayout.width, OSKeypad.csLayout.height)
        OSKeypad.csLayout.add_widget(Button_B)
        #########################################
        return
    #############################################

##############################################################
##############################################################
class CButton(Button):
    #############################################
    def __init__(self, **kwargs):
        super(CButton, self).__init__(**kwargs)
        self.bind(on_press = self.callback_Pressed)
    #############################################
    def callback_Pressed(self, instance):
        tmpStr = OSKeypad.csString
        tmp = len(tmpStr)
        if(self.text == '='):
            OSKeypad.csTextDisplay.dispatch('on_text_validate')
        elif(self.text == '+/-'):
            if(tmp > 0):
                ftmp = float(tmpStr)
                ftmp = ftmp * -1.0
                tmpStr = str(ftmp)
        elif(self.text == 'C'):
            tmpStr = ''
        elif(self.text == '.'):
            if(tmpStr.find('.') == -1):
                tmpStr = tmpStr + '.'
        elif(self.text == '<--'):
            if(tmp >= 1):
                tmpStr = OSKeypad.csString[0:(tmp-1)]
        elif(self.text == '0'):
            tmpStr = tmpStr + '0'
        elif(self.text == '1'):
            tmpStr = tmpStr + '1'
        elif(self.text == '2'):
            tmpStr = tmpStr + '2'
        elif(self.text == '3'):
            tmpStr = tmpStr + '3'
        elif(self.text == '4'):
            tmpStr = tmpStr + '4'
        elif(self.text == '5'):
            tmpStr = tmpStr + '5'
        elif(self.text == '6'):
            tmpStr = tmpStr + '6'
        elif(self.text == '7'):
            tmpStr = tmpStr + '7'
        elif(self.text == '8'):
            tmpStr = tmpStr + '8'
        elif(self.text == '9'):
            tmpStr = tmpStr + '9'
        OSKeypad.csString = tmpStr
        OSKeypad.csTextDisplay.text = OSKeypad.csString
        return
    #############################################
    def build(self):
        return
    #############################################
    def Set_Properties(self, pPad, pLW, pLH):
        Number_Rows = 4
        Number_Cols = 4
        self.width  = int((pLW - ((Number_Cols+1) * pPad)) / Number_Cols)
        self.height = int((pLH - ((Number_Rows+1) * pPad)) / Number_Rows)
        ftmp = self.height * 0.8
        self.font_size = int(ftmp)
        self.size_hint = (None, None)
        self.background_color = (.6, 0, 0, 1)
        self.foreground_color = (1, 1, 1, 1)
        return
    #############################################

##############################################################
##############################################################
