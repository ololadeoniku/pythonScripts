import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename

infileName = askopenfilename()
infile = open(infileName, "r")
outfileName = asksaveasfilename()
outfile = open(outfileName, "w")
