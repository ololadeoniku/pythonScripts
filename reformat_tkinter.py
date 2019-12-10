'''
Created by David Ololade Oniku on June17, 2019
'''
import os
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess
import matplotlib.pyplot as plt
import seaborn as sns
import bokeh
import scipy
import time
from datetime import datetime, date
from scipy.stats.stats import pearsonr
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import reformat
from reformat import *
from reformat import Tracelogs

class Window:
    def __init__(self, master):
        # self.filelist = filelist
        # self.newfile = newfile

#PARENT WINDOW
        master.title("TSV_TSP_Oniku")
        master.iconbitmap(r'C:\Users\odoniku\Desktop\Logos\intel_logo.ico')
        master.resizable(True, True)
        master.geometry('1200x700+10+10')
        master.minsize(500,400)
        master.configure(background = 'light blue')

#STYLES
        self.style = ttk.Style()  #TLabel,
        self.style.configure('TFrame', background = '#F0FFF0') ##FFFACD
        self.style.configure('TNotebook.Tab', padding = [2,2], font=('Tahoma','11') )
        self.style.configure('TButton', padding = [2,2], font = ('Tahoma', '10'), foreground = 'blue')
        self.style.configure('Remove.TButton', font=('Tahoma', '10'), foreground='red')
        self.style.configure('TLabel', background = '#F0FFF0')

#FRAMES
        self.frame1 = ttk.Frame(master, width =1196, height = 55, relief = GROOVE) #width =1196, height = 55,
        self.frame1.grid(row=0, column = 0, columnspan = 2, padx = 2, sticky=N+S+E+W)
        self.frame2 = ttk.Frame(master, width =1196, height = 45, relief = FLAT) #width =1196, height = 45,
        self.frame2.grid(row = 1, column = 0, columnspan = 2, padx = 2, sticky=N+S+E+W)
        self.frame3 = ttk.Frame(master, width = 1196, height = 550, relief = SUNKEN) #width = 1196, height = 550,
        self.frame3.grid(row = 2, column = 0, columnspan = 2, padx = 2, sticky=N+S+E+W)
        self.frame4 = ttk.Frame(self.frame3, width =296, height = 550, relief = SUNKEN) #width =396, height = 550,
        self.frame4.grid(row = 0, column = 0, sticky=N+S+E+W)
        self.frame5 = ttk.Frame(self.frame3, width =900, height = 550, relief = GROOVE) #width =800, height = 550,
        self.frame5.grid(row = 0, column = 1, sticky=N+E+S+W)
        self.frame6 = ttk.Frame(master, width =1196, height =50, relief = SOLID) #width =1196, height =50,
        self.frame6.grid(row = 3, column = 0, columnspan = 2, padx = 2, sticky=N+S+E+W)

#FRAME CONFIG
        master.rowconfigure(0, weight = 0)
        master.rowconfigure(1, weight = 1, minsize = 30)
        master.rowconfigure(2, weight = 4)
        master.rowconfigure(3, weight = 1, minsize = 20)
        master.columnconfigure(0, weight = 1)
        master.columnconfigure(1, weight = 3)
        self.frame3.rowconfigure(0, weight = 1)
        self.frame3.columnconfigure(0, weight = 1)
        self.frame3.columnconfigure(1, weight = 5)

#TABS/NOTEBOOK
        self.nb = ttk.Notebook(master, height = 30)
        self.nb.grid(row = 0, column = 0, columnspan = 2, sticky = 'NESW')
        self.File = ttk.Frame(self.nb)
        self.Edit = ttk.Frame(self.nb)
        self.Statistics = ttk.Frame(self.nb)
        self.Canvas = ttk.Frame(self.nb)
        self.Support = ttk.Frame(self.nb)
        self.About = ttk.Frame(self.nb)
        self.Help = ttk.Frame(self.nb)
        self.nb.add(self.File, text='File')
        self.nb.add(self.Edit, text = 'Edit')
        self.nb.add(self.Statistics, text = 'Statistics')
        self.nb.add(self.Canvas, text = 'Canvas')
        self.nb.add(self.Support, text = 'Support')
        self.nb.add(self.About, text = 'About')
        self.nb.add(self.Help, text = 'Help')
        self.selectfile = ttk.Button(self.File, text='Select files')
        self.selectfile.grid(row=0, column=0, padx=2, pady=2)
        self.export1 = ttk.Button(self.File, text='Reformat file', )
        self.export1.grid(row=0, column=1, padx=2, pady=2)
        self.open1 = ttk.Button(self.File, text='Open reformatted file in excel')
        self.open1.grid(row=0, column=2, padx=2, pady=2)
        self.open2 = ttk.Button(self.File, text='Open reformatted file in JMP')
        self.open2.grid(row=0, column=3, padx=2, pady=2)
        self.image = PhotoImage(file = "1280px-Intel-logo.svg.png").subsample(20,20)
        ttk.Label(self.frame2, font = ("Verdana", "11", "bold"), background = '#F0FFF0',
                        text = "Towards Improvement of Root Cause Investigation and Analysis "
                               "for TSV Sputter").grid(row = 0, column = 1, sticky = 'e')
        ttk.Label(self.frame2, image=self.image, background = '#F0FFF0').grid(row=0, column=0, sticky = 'w')
        self.close = ttk.Button(self.frame6, text = 'Close')
        self.close.grid(row=0, column=1, padx=2, pady=2)

        messagebox.showinfo(parent=master, title="Welcome",
                            message=("Welcome! This program was designed by David Oniku to help "
                                     "facilitate an efficient and effective root cause analysis for TSV sputter process module"))
        self.list1 = Listbox(self.frame4, height = 31, width = 50, background = '#F0FFF0', selectmode = MULTIPLE )

        self.scroll1 = ttk.Scrollbar(self.frame4, orient = VERTICAL)
        self.listheader = ttk.Label(self.frame4, text = "Parameters to analyze", font = ("Arial", "10", "bold"), foreground = 'blue')
        self.x_param = ttk.Button(self.frame5, text = 'Add X-axis parameter:')
        self.y_param = ttk.Button(self.frame5, text='Add Y-axis parameter:')
        self.x_param_value = Listbox(self.frame5, width = 25, height = 2, font=("Arial", "10"), selectmode = MULTIPLE)
        self.y_param_value = Listbox(self.frame5, width = 25, height = 4, font=("Arial", "10"), selectmode = MULTIPLE)
        self.x_param_remove = ttk.Button(self.frame5, text='Remove')
        self.y_param_remove = ttk.Button(self.frame5, text='Remove')
        self.plot_param = ttk.Button(self.frame5, text = 'Plot Parameters')


def main():
    root = Tk()
    window = Window(root)
    filetypes_open = [("All Files", ".*"), ("csv files", ".csv")]
    filetypes_save = [("All Files", ".*"), ("excel files", ".xlsx")]
    filename = list(filedialog.askopenfilenames(parent=root,initialdir=os.getcwd(), title='Select Files',filetypes=filetypes_open))
    messagebox.showinfo(title='Save-as Filename', message='Please enter the name to save the reformatted file.')
    window.selectfile.configure(command = filename)
    filelist = []
    for f_path in filename:
        filelist.append(os.path.realpath(f_path))

    newfile = filedialog.asksaveasfilename(parent = root,initialdir=os.getcwd(), title='Save File',
                                                        defaultextension='.xlsx',filetypes=filetypes_save)
    trace_logs = Tracelogs(filelist, newfile)
    trace_file = trace_logs.reFormat()
    trace_file.columns = ['ACBias_V', 'MatchLoad_mV', 'MatchTune_mV', 'ACBiasForward_W',
            'ACBiasReflected_W', 'ArBackside_sccm', 'ArFlow_sccm', 'BacksidePress_torr','CenterTapBias_V',
            'CryoTemp_degK', 'DCCurrent_A', 'DCPower_W', 'TargetVoltage_V', 'DCArc_Acc_Count','DCArc_Acc_Micro_Count',
            'DCArc', 'DCArc_Micro', 'ESCCurrent_mA', 'ESCVoltage_V', 'PedestalTemp_degC','HtrLiftStep_step',
            'HXTemp_degC', 'IGPressure_torr', 'LiftPosition', 'MagnetPos', 'N2Flow_sccm','CHPressure_torr',
            'StepNumber', 'TargetLife_kWh', 'Start_Date', 'DateTime', 'Elapsed_Time_sec','sample_index']
    writer = pd.ExcelWriter(newfile, engine="xlsxwriter")
    trace_file.to_excel(writer, sheet_name='Sheet1')
    fig = Figure(figsize=(12, 5), facecolor='white')


    def export_excel():
        writer.save()
        window.list1.grid(row=1, column=0, rowspan=10, pady = 2, padx = 2, sticky = 'NESW')
        window.scroll1.grid(row=1, column=1, rowspan=10, sticky='NS')
        window.scroll1.configure(command = window.list1.yview)
        window.list1.configure(font = ('Arial', '10'), yscrollcommand=window.scroll1.set)
        window.listheader.grid(row=0, column=0, pady = 2, sticky = 'e')
        window.list1.delete(0, END)
        for row in trace_file.columns:
            window.list1.insert(END, row)
        window.x_param.grid(row=0, column=0, sticky = 'nw', padx = 2, pady = 2)
        window.x_param.configure(command = add_x_parameters)
        window.y_param.grid(row=1, column=0, sticky = 'nw', padx = 2, pady = 2)
        window.y_param.configure(command = add_y_parameters)
        window.x_param_remove.grid(row=0, column=2, sticky='nw', padx=2, pady=2)
        window.x_param_remove.configure(style = 'Remove.TButton', command=remove_x_parameters)
        window.y_param_remove.grid(row=1, column=2, sticky='nw', padx=2, pady=2)
        window.y_param_remove.configure(style = 'Remove.TButton', command=remove_y_parameters)
        window.x_param_value.grid(row=0, column=1, sticky='w', padx=2, pady=2)
        window.y_param_value.grid(row=1, column=1, sticky='w', padx=2, pady=2)
        window.plot_param.grid(row=2, column=0, sticky='nw', padx = 2, pady=2)
        window.plot_param.configure(command = plot_parameters)
        # window.y_param_value.tag_config("a", foreground="blue", underline=1)
        # window.y_param_value.tag_bind("Enter>", show_hand_cursor)
        # window.y_param_value.tag_bind("Leave>", show_arrow_cursor)
        # window.y_param_value.tag_bind("Button-1>", click)
        window.x_param_value.config(cursor="hand2")
        window.y_param_value.config(cursor="hand2")

    def open_file(file):
        export_excel()
        with subprocess.Popen(["start", "/WAIT", file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True) as doc:
                doc.poll()

    def get_parameters(event):
        global selectlist
        selectlist = []
        for item in window.list1.curselection():
            selection = window.list1.get(item)
            selectlist.append(selection)

    def get_x_parameters(event):
        global x_delete_list
        x_delete_list = []
        for item in window.x_param_value.curselection():
            x_delete_list.append(item)

    def get_y_parameters(event):
        global y_delete_list
        y_delete_list = []
        for item_y in window.y_param_value.curselection():
            y_delete_list.append(item_y)

    def add_x_parameters():
        global selectlist
        if len(selectlist) == 0:
            messagebox.showwarning(title = "Select Parameter", message = "Please select a "
                                                                             "parameter to analyze from the left pane")
        for item in selectlist:
            window.x_param_value.insert(END, item)
        window.list1.selection_clear(0, END)

    def add_y_parameters():
        global selectlist
        if len(selectlist) == 0:
            messagebox.showwarning(title="Select Parameter", message="Please select at least one "
                                                                     "parameter to analyze from the left pane")
        for item in selectlist:
            window.y_param_value.insert(END, item)
        window.list1.selection_clear(0, END)

    def remove_x_parameters():
        for item in x_delete_list:
            window.x_param_value.delete(item)
        window.x_param_value.update_idletasks()

    def remove_y_parameters():
        for item in y_delete_list:
            window.y_param_value.delete(item)
        window.x_param_value.update_idletasks()

    def plot_parameters():
        x_param_list = list(window.x_param_value.get(0, END))
        y_param_list = list(window.y_param_value.get(0, END))
        x_size = len(x_param_list)
        print(x_size)
        print(x_param_list)
        for item in x_param_list:
            print(item)
            x_parameter = trace_file[item]
            min_x = min(x_parameter)
            max_x = max(x_parameter)
            y_size = len(y_param_list)
            print(y_param_list)
            for item_y in y_param_list:
                print(item_y)
                y_parameter = trace_file[item_y]
                min_y = min(y_parameter)
                max_y = max(y_parameter)
                axis = fig.add_subplot(2,2,(y_param_list.index(item_y)+1))
                axis.set_ylim(min_y, max_y)
                axis.set_xlim(min_x, max_x)
                p0 = axis.plot(x_parameter, y_parameter, label = '{} vs {}'.format(item_y, item))
                axis.set_ylabel(item_y)
                axis.set_xlabel(item)
                axis.grid()
                fig.legend(p0, '{} vs {}'.format(item_y, item), 'upper right')
                plot_figure = Toplevel(root)
                canvas = FigureCanvasTkAgg(fig, master=plot_figure)
                canvas._tkcanvas.grid(row=0, column = 0, columnspan = 4, sticky = 'nesw')

    window.export1.configure(command = export_excel)
    working_file_path = os.path.realpath(newfile)
    window.open1.configure(command=lambda: open_file(working_file_path))
    window.open2.configure(command=None)
    window.list1.bind('<<ListboxSelect>>', get_parameters)
    window.x_param_value.bind('<<ListboxSelect>>', get_x_parameters)
    window.y_param_value.bind('<<ListboxSelect>>', get_y_parameters)

    def close_window():
        root.destroy()

    window.close.configure(command = close_window)
    root.mainloop()

if __name__ == "__main__": main()







    # except FileNotFoundError:
    #     messagebox.showinfo(title="warning", message="You did not select a file to open")
    # except ValueError:
    #     messagebox.showinfo(title="warning", message="You did not select a file to open")
    #
    # except IndexError:
    #     messagebox.showinfo(title="Warning", message="You did not select any file to upload")
