# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:22:48 2022

@author: Nicolas Pelletier-Côté
"""
from Screen import Screen as Screen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image

from MainWindowMotor import MainWindowMotor
from ActivityMenu import ActivityMenu
from StopMenu import StopMenu
from SummaryMenu import SummaryMenu

from MotorParameters import MotorParameters

import sys
# from CommandButton import CommandButton as CommandButton

class MotorScreen(Screen):
    def __init__(self, event_function):
        super(MotorScreen, self).__init__(event_function)
        #self.event_function = event_function
        self.app = QApplication(sys.argv)
        
        # self.motor_parameters = MotorParameters()
        # self.main_window_motor
        
        self.button_dictionary = {}
        
        # self.connect_buttons(self.main_window_motor)
        self.current_menu = 0
        self.confirm_menu = 0
        
    
    def manage_active_window(self, motor_parameters):
        # print(f"window_counter = {self.window_counter}")
        if self.window_counter == 0:
            self.current_menu = MainWindowMotor(motor_parameters)
            self.connect_buttons(self.current_menu)
        elif self.window_counter == 1:
            self.current_menu.close()
            self.current_menu = ActivityMenu(motor_parameters)
            self.current_menu.show()
            self.connect_buttons(self.current_menu)
        elif self.window_counter == 2:
            # self.current_menu.close()
            self.confirm_menu = StopMenu()
            self.confirm_menu.show()
            self.confirm_menu.confirmation_button.clicked.connect(lambda:self.confirmation_button_clicked(motor_parameters))
            # self.button_dictionary[self.confirm_menu.confirmation_button] = "confirmed_stop_training"
            self.connect_buttons(self.confirm_menu)
            self.confirm_menu.continue_button.clicked.connect(lambda:self.continue_button_clicked(motor_parameters))
        elif self.window_counter == 3:
            self.current_menu.close()
            self.current_menu = SummaryMenu()
            self.current_menu.show()
        
        
    def connect_buttons(self, window):
    # Connect before the show or the exec
        # print(f"{len(window.button_dictionary)} Buttons:")
        for button in window.button_dictionary:
            #print(widget)
            #print(type(widget))
            button.clicked.connect(lambda : self.event_function(window.button_dictionary[button]))
            # self.event_function(window.button_dictionary[button])
                
            # print(f"CONNECTED BUTTON {button.text()} TO COMMAND {window.button_dictionary[button]} IN ERGOCYCLE")
    
    def confirmation_button_clicked(self, motor_parameters):
        self.next_window()
        self.manage_active_window(motor_parameters)
        self.confirm_menu.close()
    
    def continue_button_clicked(self, motor_parameters):
        self.window_counter -= 1
        self.manage_active_window(motor_parameters)
        self.confirm_menu.close()
        
        # print(f"{window.layout.count()} Widgets:")
        # for i in range(0, window.layout.count()):
        #     widget = window.layout.itemAt(i).widget()
        #     #print(widget)
        #     #print(type(widget))
        #     if type(widget) is CommandButton:

        #         widget.clicked.connect(lambda : self.event_function(widget.get_command()))
                
        #         print(f"CONNECTED BUTTON {widget.get_command()} TO ERGOCYCLE")
    
    # def start_motor_application(self):
    #     self.win.show()
    #     sys.exit(self.app.exec_())