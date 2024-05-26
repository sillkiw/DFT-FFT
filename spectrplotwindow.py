import tkinter as tk,sys
from tkinter import filedialog as fd
from audioinfowindow import AudioInfoWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np




class SpectrPlotWindow(tk.Toplevel):
    def __init__(self,main):
        super().__init__(main)
        self.w = main.w
        self.h = main.h
        self.x = main.x
        self.n = 900
        self.components = []
        self.set_spectr_plot()
    
  

    def DFT(self):
        for k in range(self.n):  
            s = complex(0)
            for j in range(self.n): 
                angle = 2j * np.pi * j * k / self.n
                s += self.x[j] * np.exp(-angle)
            self.components.append(s)
    def draw(self):
        print(self.components)
    
    def set_spectr_plot(self):
       self.fig2,self.ax2 = plt.subplots()
       self.spectr_plot_frame = tk.Frame(self)
       self.ax2.set_title("График спектра")
       self.spectr_plot_frame.pack()
       self.spectr_plot = FigureCanvasTkAgg(self.fig2,master = self.spectr_plot_frame)
       self.spectr_plot.get_tk_widget().pack()