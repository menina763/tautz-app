"""
main.py

This will be the basic structure for the Tautz app.

Version: 10/7/2023

Terms to know: 

- module: a file with a .py extension
- Root widget: the main container that holds & organizes other widgets in your user interface (like buttons, labels, 
  text input fields, sliders, etc). 

"""
##IMPORTTING THE CLASSES
import kivy
from kivy.lang import Builder
from kivy.app import App                    #From the Kivy App module import the base class App to create the application
from kivy.uix.boxlayout import BoxLayout    #From the Kivy UIX Boxlayout module import the BoxLayout class to make flexible layouts for widgets
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView

##SETTING UP METHODS

#This method will import the main container for user interface
class TautzApp(App):                        #Create a TautzApp class that inherits from the App class
    def build(self):                         #Define the build method (which will use its own paramaters)
        Builder.load_file('main.kv')
        return RootWidget()                 #Return an instance of the RootWidget class to make it the main widget of the app

#
class RootWidget(BoxLayout):                #Set up the RootWidget class (inherited from BoxLayout), but just make it blank.
    pass

if __name__ == '__main__':                    #If we're running the  main program, we'll start the app!              
    TautzApp().run()