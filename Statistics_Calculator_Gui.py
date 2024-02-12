import statistics as stats
import math
import PySimpleGUI as sg
import time
import threading
import scipy.stats as st
import PyInstaller
import matplotlib.pyplot as plt
import pandas as pd
import csv


sg.theme('TanBlue')

layout = [
            [sg.Text('Please enter values')],
            [sg.Text('If the three fields below data are unknown, only enter the data or upload a file and they will be found for you')],
            [sg.Text('File path for uploads (use csv format)', size=(15, 2)), sg.InputText('C:', key='-FILE-')],
            [sg.Text('Enter the exact column name', size=(15, 2)), sg.InputText('col1', key='-COLUMN-')],
            [sg.Text('Manual Data (comma seperated)', size=(15, 2)), sg.InputText('1,2,3,4', key='-DATA-')],
            [sg.Text('Mean', size=(15, 2)), sg.InputText('1', key='-MEAN-')],
            [sg.Text('StDev', size=(15, 2)), sg.InputText('2', key='-STDEV-')],
            [sg.Text('Count', size=(15, 2)), sg.InputText('3', key='-COUNT-')],
            [sg.Text('X Value', size=(15, 2)), sg.InputText('4', key='-X-')],
            [sg.Text("Confidence Level", size=(15,2)), sg.InputText("0.95", key="-CONFIDENCE-")],
            [sg.Button("Manual Stat Summary"), sg.Button("Plot"), sg.Button("Hist"), sg.Button("File Stat Summary"), sg.Button("Plot File"), sg.Button("Hist File"), sg.Cancel()]
            ]


window = sg.Window('Single Mean Statistics Calculator', layout)
event, values = window.read()
my_list = values["-DATA-"].split(",")
numbered_list = []
count = 0
variable = values["-COLUMN-"]
for i in my_list:
    numbered_list.append(float(i))
    count += 1

if values["-FILE-"] != "C:":
    df = pd.read_csv(values["-FILE-"])
else:
    pass

window.close()
def draw_plot(data):
    plt.plot(data)
    plt.show(block=True)

def draw_hist(data):
    plt.hist(data)
    plt.show(block=True)

if event == "Plot":
    draw_plot(numbered_list)

elif event == "Hist":
    draw_hist(numbered_list)

elif event == "Plot File":
    draw_plot(df[[variable]])
    

elif event == "Hist File":
    draw_hist(df[[variable]])



        

elif event == "Manual Stat Summary":                                                                      
    sg.Popup(event, values, "Mean", stats.mean(numbered_list), "Standard Deviation", stats.stdev(numbered_list), "Max and Min", str(max(numbered_list)) + " | " + str(min(numbered_list)),
         "Quantiles", stats.quantiles(numbered_list),"Variance", stats.variance(numbered_list), "Sample Size", count,
         "Range", max(numbered_list) - min(numbered_list),"Coefficent of Variantion", (float(values['-STDEV-']) / (float(values['-MEAN-'])) * 100),
         "Standard Error", float(values["-STDEV-"]) / (float(values["-COUNT-"]) ** 0.5),
         "Z-Score", (float(values["-X-"]) - float(values["-MEAN-"])) / float(values["-STDEV-"]),
         "MOE (only when using X)", (float(values["-X-"]) - float(values["-MEAN-"])) / float(values["-STDEV-"]) * (float(values["-STDEV-"]) / (float(values["-COUNT-"]) ** 0.5)),
         "Confidence Intervals", "Lower                         Upper", 
         st.t.interval(confidence=float(values["-CONFIDENCE-"]),
                       df = int(values["-COUNT-"]),
                       loc= float(values["-MEAN-"]),
                       scale = float(values["-STDEV-"])/(float(values["-COUNT-"]) ** 0.5)))



elif event == "File Stat Summary":
    sg.Popup(event,values, "Summary", df[[variable]].describe(), "Range", df[[variable]].max() - df[[variable]].min())




















