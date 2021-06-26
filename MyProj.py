def return_list_of_files():
    import os
    x = "-------------------------------------------------------\n"
    n = 0
    basepath = os.getcwd()
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            if n<30:
                if ( entry[entry.find('.'):] == ".txt" ):
                    entry = entry[0:entry.find('.')]
                    if len(entry)>40:
                        x+="- "+entry[0:40]+" .."
                    else:
                        x+="- "+entry
                    x+="\n"
                    n += 1
    if n == 0:
        x += "Pas de fichers [.txt] !!\n"
    if n == 30:
        x+="- ect..\n"
    x+="-------------------------------------------------------"
    return x

def set_filename(filename):    
    filenamee = str(filename)
    filenamee+=".txt"
    return filenamee
        
def filepath(filename):
    import os
    filepath = os.getcwd()+"/"+filename
    return filepath
    
def create_HTML():
    txtfile = open(filepath(set_filename(filename.get())),"r")
    contents = txtfile.readlines()
    txtfile.close()
    filenameHTML=filename.get()+" HTML.html"
    f = open(filenameHTML,"w")
    f.writelines("<html>\n<head>\n<title>")
    f.writelines(filename.get())
    f.writelines("</title>\n</head>\n<body>\n<h3>")
    for i in contents:
        f.writelines(i)
        f.writelines("<br>")
    f.writelines("</h3>\n</body>\n</html>")
    f.close()

#============================================ MAIN ============================================ 

import tkinter as tk
from tkinter import ttk

CoList = return_list_of_files().split("\n")
Counter = 0
for i in CoList:
    if i:
        Counter += 1

frame = tk.Tk()
# Width and Height
w = 370
h = 200 + Counter*15
# Screen Width and Height
sw = frame.winfo_screenwidth()
sw = ( (sw-w)/2 )
# using [ %d ] fi blast [ .format ] to convert variables to "int"
# variables inside frame.geometry() should be "int"
frame.geometry("%dx%d+%d+0" % (w,h,sw))
frame.title('Convert to Web Page')
#frame.resizable(False,False)

aff1 = ttk.Label(frame,text="Liste des Fichers texte",foreground="blue")
aff1.config(font=("consolas",15))

aff2 = ttk.Label(frame,text=return_list_of_files())
aff2.config(font=("",10))

aff3 = ttk.Label(frame,text="Entrer le nom du ficher TXT\n(sans écrire l'extension)",foreground="blue")
aff3.config(font=("consolas",15))
filename = ttk.Entry(frame)
filename.config(font=("consolas",11))

btn = ttk.Button(frame,text="CONVERT",command=create_HTML)

aff1.pack()
aff2.pack()
aff3.pack()
filename.pack()
aff4 = ttk.Label(frame,text="").pack()
btn.pack()

frame.mainloop()
