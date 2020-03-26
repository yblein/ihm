import tkinter as tk
import time

class Mesure:
    def __init__(self,app,id,unit,title):
        self.value = tk.IntVar()
        self.value.set(0)
        self.state = 0
        self.id = id
        self.unit = unit
        self.title = title

        self.width = 120
        self.height = 120

        self.canvas = tk.Canvas(app, height=self.height, width=self.width,bg="#edf0f6")
        
        self.canvas.create_text(int(self.width*0.1), int(self.height*0.1), anchor='w', \
        		font=("Helvetica", 14),fill='black', text=self.title +" "+self.unit)
        self.canvas.create_text(int(self.width*0.5), int(self.height*0.5), anchor='c', \
        		font=("Helvetica", 44),fill='black', text=self.value.get(),tags='text'+str(self.id))
        
    def update(self,value):
        self.value.set(value)
        self.canvas.itemconfigure('text'+str(self.id), text=self.value.get())
        self.canvas.update()

      		


# app = tk.Tk()
# app.wm_title("Graphe Matplotlib dans Tkinter")

# btn1 = Mesure(app,0,'MLrfr','VT')
# btn2 = Mesure(app, 0, 'MLrfr','VT')
# btn3 = Mesure(app, 0, 'MLrfr','VT')
# btn1.canvas.pack()
# btn2.canvas.pack()
# btn3.canvas.pack()

# for i in range(0,400):
#     print('debug:',i)
#     btn1.update(i)
#     btn2.update(i)
#     btn3.update(i)
#     time.sleep(0.1)
# app.mainloop()