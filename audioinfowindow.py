import tkinter as tk,os,wave,datetime
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import font
from enum import Enum
from pathlib import Path
from random import randint
from math import floor
class Audio: 
    def __init__(self,path):
        #Путь до торрента
        self.path = path

        self.source,self.name = os.path.split(self.path)

        self.raw = wave.open(self.path) 
        
        self.framerate = self.raw.getframerate()
        
        self.nframes = self.raw.getnframes()

        self.duration = self.nframes / float(self.framerate)
        
        self.nchanels = self.raw.getnchannels()


class AudioInfoWindow(tk.Toplevel):

    #Состояния ответа пользователя
    class _STATES_OF_ANS_(Enum):
        (DFT,FFT,CLS) = range(0,3)

    #Окно обзорщика торрент файла
    def __init__(self,main):
        super().__init__(main)
    
        self.title("Audio File information")
       

        #Ширина всплывающего окна
        self.w = main.w // 2 + main.w//6
        #Высота всплывающего окна
        self.h = (main.h - main.h//3 - main.h//12) //2 + 25
        
        #Центрирование по центру главного окна(main)
        self.geometry(f"{self.w}x{self.h}+{(main.sc_w-self.w)//2}+{(main.sc_h-self.h-50)//2}")

        self.au_data = Audio(main.audio_file.name)
        
        #Установка стиля
        self.set_style()

        #Установка кнопки и лейбла "Source"
        self.set_source_label_and_button()
        
        self.set_information_label()
        #Установка кнопки и лейбла "destination"
        self.set_answer_DFT_FFT_CLOSE()
       
        self.grab_set()
     


    def set_style(self):
        '''Установка стиля'''
        self.font = font.Font(family= "Arial", size=13) 
        self.font2 = font.Font(family= "Arial", size=15) 
        self.font3 = font.Font(family= "Segoe", size=11) 
        self.style_button = ttk.Style()
        self.style_button.configure('Heading.TButton',anchor=tk.W,font = self.font3)        
        self.style_button.configure('Heading.Label', anchor=tk.W,font = self.font3)   
        self.style_button.configure("mystyle2.Treeview",font=('Segoe',11)) 
        self.style_button.configure("mystyle2.Treeview.Heading",font=('Segoe', 9))
    
    
    def set_source_label_and_button(self):
        '''Установка  лейбла Source и кнопки для изменения аудио-файла'''
        self.label_frame = tk.Frame(self)
        self.label_frame.pack(pady=20)
        ttk.Label(self.label_frame,text="Source:",font=self.font,style='Heading.Label').pack(side=tk.LEFT)

       
        self.source_button = ttk.Button(self.label_frame,text = " "+self.au_data.path,width=self.w//10,style="Heading.TButton",command=self.change_audio)
        self.source_button.pack()
    
    def set_information_label(self):
    
        self.info_frame = tk.LabelFrame(self)
        self.info_frame.pack(pady=10)
        self.nameinf = ttk.Label(self.info_frame,text="Название:                           "+self.au_data.name,width = self.w//10,font=self.font3)
        self.nameinf.pack()
        self.durationinf = ttk.Label(self.info_frame,text="Длительность:                     "+datetime.timedelta(seconds=floor(self.au_data.duration)).__str__(),width = self.w//10,font=self.font3)
        self.durationinf.pack()
        self.framerateinf =    ttk.Label(self.info_frame,text="Частота дискретизации:    "+str(self.au_data.framerate)+"Гц",width = self.w//10,font=self.font3)
        self.frameninf =  ttk.Label(self.info_frame,text="Количество фреймов:        "+str(self.au_data.nframes),width = self.w//10,font=self.font3)
        self.framerateinf.pack()
        self.frameninf.pack()
        self.type =  ttk.Label(self.info_frame,text=  "Тип:                                      " + ("Моно" if self.au_data.nchanels == 1 else "Стерео") ,width = self.w//10,font=self.font3)
        self.type.pack()
    def change_audio(self):
        '''Изменение торрент-файла'''
        #Пользователь выбирает новый торрент
        audio_file = fd.askopenfile(parent = self,initialdir=self.au_data.source,filetypes =[('Audio Files', '*.wav')]) 

        if audio_file:
            #Инициализация нового торрента
            self.au_data = Audio(audio_file.name)
            
            #Изменение значения на кнопке
            self.source_button.config(text = ""+self.au_data.path)

      

    def set_answer_DFT_FFT_CLOSE(self):
        '''Установка двух кнопок Open | Close''' 
        
        #Состояние ответа
        self.state_of_answer = 'thinking'
        
        answer_frame = tk.Frame(self)
        answer_frame.pack(fill=tk.X)
        
        #Кнопка Close
        self.button_Close = ttk.Button(answer_frame,text = "Отмена",width = self.w//40,command = self.close_pressed)
        self.button_Close.pack(side = tk.RIGHT,padx=10)
        
        #Кнопка Open
        self.button_Open =  ttk.Button(answer_frame,text = "DFT",width = self.w//40,command = self.DFT_pressed)
        self.button_Open.pack(side=tk.RIGHT,padx=10)

        self.button_Open =  ttk.Button(answer_frame,text = "FFT",width = self.w//40,command = self.FFT_pressed)
        self.button_Open.pack(side=tk.RIGHT,padx=10)
     
    
    def close_pressed(self):
        '''Ответ на событие нажатия кнопки Close'''
        
        #Пользователь отказался от установки
        self.state_of_answer = AudioInfoWindow._STATES_OF_ANS_.CLS
        
        #Разрещаем пользователю пользоваться главным окном
        self.grab_release()

        #Закрытие информационного окна
        self.destroy()

    def DFT_pressed(self):
        '''Ответ на событие нажатия кнопки Open'''

        #Пользователь согласился на установку
        self.state_of_answer = AudioInfoWindow._STATES_OF_ANS_.DFT
        
        #Разрещаем пользователю пользоваться главным окном
        self.grab_release()

        #Закрытие информационного окна
        self.destroy()
    def FFT_pressed(self):
        '''Ответ на событие нажатия кнопки Open'''

        #Пользователь согласился на установку
        self.state_of_answer = AudioInfoWindow._STATES_OF_ANS_.FFT
        
        #Разрещаем пользователю пользоваться главным окном
        self.grab_release()

        #Закрытие информационного окна
        self.destroy()

            

