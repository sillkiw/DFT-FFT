import tkinter as tk,sys
from tkinter import filedialog as fd
from audioinfowindow import AudioInfoWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from spectrplotwindow import SpectrPlotWindow
class Interface(tk.Tk): #главное окно
    def __init__(self):
        super().__init__()    

        self.title('FFT/DFT | KOVALENKO')

        self.sc_w = self.winfo_screenwidth()
        self.sc_h = self.winfo_screenheight()

        self.w = self.sc_w//2 + self.sc_w//4 #ширина главного окна
        self.h = self.sc_h//2  +  self.sc_h//4 #высота главного окна
        
        self.config(bg="white")

        self.geometry(f"{self.w}x{self.h}+{(self.sc_w - self.w)//2}+{(self.sc_h - self.h -100)//2}")

        self.set_audio_plot()
   #     self.set_spectr_plot()
        #Установка панели инструментов
        self.set_tool_bar()
        


    def open_audio_information_window(self):
        '''Запуск всплывающего окна, если пользователь выбрал файл''' 
        
        self.audio_info_window = AudioInfoWindow(self)
        
        self.check_state_of_answer()

    def set_audio_plot(self):
        self.fig,self.ax = plt.subplots()
        self.audio_plot_frame = tk.Frame(self)
        self.fig.set_size_inches(10, 8)
        self.ax.set_title("График аудио")
        self.audio_plot_frame.pack()
        self.audio_plot = FigureCanvasTkAgg(self.fig,master = self.audio_plot_frame)
        self.audio_plot.get_tk_widget().pack()



    def ask_audio_file(self,chest = False): 
        '''Выбор аудио-файла'''
       
        #Пользователь выбирает торрент файл
        self.audio_file = fd.askopenfile(initialdir="C:\\",filetypes =[('Audio Files', '*.wav')]) 
        
        if self.audio_file:
            self.open_audio_information_window()
  
            
    
    def set_tool_bar(self):
        '''Установка панели инструментов Open|Edit|View'''

        #Инициализация панели инструментов (Open|Edit|View)
        main_menu = tk.Menu(self) 
       
        #При нажатии на File
        file_menu = tk.Menu(tearoff=0)
        file_menu.add_command(label="Открыть...",command=self.ask_audio_file) 
        file_menu.add_separator()
        file_menu.add_command(label="Выйти",command=sys.exit)
        
        #Инициализация(File|Edit|View) 
        main_menu.add_cascade(label="Файл",menu = file_menu)
      
     
        #Бинд на главное окно
        self.config(menu=main_menu)

    def plot_audio(self): 
        self.ax.clear()
        self.ax.set_title("График аудио")
        self.x = self.au.raw.readframes(-1) 
        self.x = np.frombuffer(self.x, dtype ="int16") 
        self.lenx = 1000
      
        time = np.linspace( 
            0, # start 
            self.lenx / self.au.framerate, 
            num = self.lenx
        ) 
  
 
        self.ax.scatter(time,self.x[:self.lenx],marker = 'o',s=4)
        self.audio_plot.draw()
  
   


    def check_state_of_answer(self):  
        '''Проверка действия пользователя. После нажатия Open в информационном окне начинается установка'''
        
        #Ожидание ответа пользователя
        self.wait_window(self.audio_info_window)
        
        if self.audio_info_window.state_of_answer == AudioInfoWindow._STATES_OF_ANS_.DFT:
            self.au = self.audio_info_window.au_data
            self.plot_audio()
            self.spectr_plot_window = SpectrPlotWindow(self)
            self.spectr_plot_window.DFT()
            self.spectr_plot_window.draw()
            self.wait_window(self.spectr_plot_window)


if __name__ == "__main__":
    window = Interface()
    window.mainloop()