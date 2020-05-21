######################################################################
# Ici nous avons l'interface utilisateur
# qui utilise les données de loadData pour predire la classe d'une image 
######################################################################
import tkinter as tk   # python3
from tkinter import *
from PIL import ImageTk,Image,ImageDraw,ImageFont
from tkinter import filedialog
from utils import*
import matplotlib.image as mpimg
from recettes import *
from random import randint
from loadData import*
#import Tkinter as tk   # python

TITLE_FONT = ("Helvetica", 18, "bold")
listImageT=[]
ilYaTilUneImage=0
class_names=['Apple' ,'Banana' ,'Grape' ,'Orange']
class_names=['Apple' ,'Banana' ,'Grape' ,'Orange']

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        global ilYaTilUneImage
       
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F,geometry in zip((StartPage, PageOne), ('600x700', '1080x700')):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.config(background='#41B77F')
            self.frames[page_name] = (frame, geometry)
            

            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        
        frame, geometry = self.frames[page_name]
        # change geometry of the window
        self.update_idletasks()
        self.geometry(geometry)
        #self.config(background='#41B77F')
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global ilYaTilUneImage
        
        #img = ImageTk.PhotoImage(file="fruits.png")
    
        canvas = tk.Canvas(self, width=300, height=300, bd=0, highlightthickness=0,bg='#41B77F')
        #canvas.create_image(0,0, image=img)
        canvas.pack ()
        img=Image.open("fruits.png")
        #resize Image
        img2 = img.resize((300, 300), Image.ANTIALIAS) 
        canvas.image=ImageTk.PhotoImage(img2)
        canvas.create_image(0,0,image=canvas.image,anchor='nw')
        canvas.pack(expand=YES)

        
       

        label = tk.Label(self, text="Bienvenue sur TShEf", font=("Leelawadee",40), bg='#41B77F', fg='white')
        label.pack(expand=YES)
        label = tk.Label(self, text="TShEf c'est fruité mais jamais stresser!", font=("Calibri",25),bg='#41B77F', fg='white')
        label.pack(side="bottom")
        

        button1 = tk.Button(self, text="Commencer",font=("Leelawadee",25),bg='white', fg='#41B77F',
                            command=lambda: controller.show_frame("PageOne"))
      
        button1.pack(pady=25)
       


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global ilYaTilUneImage

        frame1 = tk.Frame(self, bg='#41B77F')
        frame2 = tk.Frame(self, bg='#41B77F')
        
        label = tk.Label(self, text="TShEf c'est fruité mais jamais stresser!", font=("Leelawadee",30),bg='#41B77F', fg='white')
        label.pack(side="top")#pady=10
        #Création d'un espace canvas "image chargé"
        self.canvas = tk.Canvas(frame1, width=520, height=400, background='#41B77F')
        self.canvas.create_text("0","0",text="", font="Arial 25",fill="white")
        self.canvas.pack()

        #Création d'un espace canvas "images déjà chargé"
        self.canvas1 = tk.Canvas(frame2, width=520, height=400, background='#41B77F')
        self.canvas1.create_text("0","0",text=" ", font="Arial 25",fill="white")
        self.canvas1.pack()

        button1 = tk.Button(self, text="Done",font=("Leelawadee",25),bg='white', fg='#41B77F',
                            command=self.giveRecette)
        button1.pack(side="bottom")
        button2 = tk.Button(self, text="Charger image",font=("Leelawadee",25),bg='white', fg='#41B77F',
                            command=self.browseFiles)
        button2.pack(side="bottom")
        #ajouter
        frame1.pack(side="left")
        frame2.pack(side="right")
        self.fileName=[]
        self.Fruit=[]
        #print(predict(self.X_train,self.Y_train,[[100,200,100,3,6,6]]))
        

    def changeImagePrincipal(self):
         #resize Image
        array_length = len(self.fileName)
        last_element = self.fileName[array_length - 1]
 
        
        
        xyz=self.predictFruit(last_element)
        if(xyz not in self.Fruit):
            self.Fruit.append(xyz[0])
            img=Image.open(last_element)
            img2 = img.resize((520, 400), Image.ANTIALIAS) 
            self.canvas.image=ImageTk.PhotoImage(img2)
            self.canvas.create_image(0,0,image=self.canvas.image,anchor='nw')
        else:
            result = speak(self,class_names[xyz[0]-1]).show()
            self.fileName.pop(array_length - 1)
    
            print("yesss")
        
       # self.Fruit.append(xyz[0])
        
        
    def get_concat_h(self,im1, im2):
        dst = Image.new('RGB', (im1.width + im2.width, im1.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, 0))
        return dst

    def get_concat_v(self,im1, im2):
        dst = Image.new('RGB', (im1.width, im1.height + im2.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (0, im1.height))
        return dst
            
    def changeListBox(self):
        if(len(self.fileName)==2):
            element = self.fileName[0]
        
            img=Image.open(element)
            
            #img=self.draw_text(img, class_names[self.Fruit[0]], x=0, y=0)
            
            img2 = img.resize((520, 400), Image.ANTIALIAS) 
            self.canvas1.image=ImageTk.PhotoImage(img2)
            self.canvas1.create_image(0,0,image=self.canvas1.image,anchor='nw')
        elif(len(self.fileName)==3):
            
            element1 = self.fileName[0]
            element2 = self.fileName[1]
            img1=Image.open(element1)
            img2=Image.open(element2)
            img3=self.get_concat_h(img1,img2)
            img4 = img3.resize((520, 400), Image.ANTIALIAS)
            self.canvas1.image=ImageTk.PhotoImage(img4)
            self.canvas1.create_image(0,0,image=self.canvas1.image,anchor='nw')
            
        elif(len(self.fileName)==4):
            element1 = self.fileName[0]
            element2 = self.fileName[1]          
            element3 = self.fileName[2]
            
            img1=Image.open(element1)
            img3=Image.open(element3)
            img2=Image.open(element2)
            img4=self.get_concat_h(img1,img2)
            img5=self.get_concat_v(img4,img3)
            
            img6 = img5.resize((520, 400), Image.ANTIALIAS)
            self.canvas1.image=ImageTk.PhotoImage(img6)
            self.canvas1.create_image(0,0,image=self.canvas1.image,anchor='nw')
            
    def giveRecette(self):
        if(len(self.fileName)!=0):
            self.Fruit.sort()
            full=""
            for val in self.Fruit:
                full=full+"-"+str(val)
            full=full[1:]
            #print(full)
            result = MyDialog(self, full).show()
            self.canvas.delete("all")
            self.canvas1.delete("all")
            self.fileName=[]
            self.Fruit=[]
            


    def predictFruit(self,name):
        #predict(self.X_train,self.Y_train,[[100,200,100,3,6,6]]))
        #imgT=mpimg.imread('name')
        #print("lalalala")
        tttt=np.array([extractFeatures(mpimg.imread(name))])
        #print(tttt)
        #print("lalalal")
        print(predict(X_train,Y_train,tttt))
        return predict(X_train,Y_train,tttt)
    










    def browseFiles(self):
            try:
            
                if(len(self.fileName)<4):
                    fileName=(filedialog.askopenfilename(initialdir = "/", 
                                                          title = "Select a File", 
                                                           filetypes=[('all files', '.*'),
                           ('image files', '.png'),
                           ('image files', '.jpg'),
                       ]))
                    self.fileName.append(fileName)
                    #file = open("tshef.txt", "w")
                    #self.file.write(fileName+ "\r\n")
                   
                    self.changeImagePrincipal()
                    self.changeListBox()
                    
            except:
                print("something wrong")

       




class MyDialog(object):
    def __init__(self, parent, prompt):
        self.toplevel = tk.Toplevel(parent)
        self.var = tk.StringVar()
        #label = tk.Label(self.toplevel, text=prompt)

        frame1 = tk.Frame(self.toplevel, bg='#41B77F')
        frame2 = tk.Frame(self.toplevel, bg='#41B77F')
        #print("lalalal")
        #print(prompt)
        yyyy=recettes[str(prompt)]
        rd=randint(0,len(yyyy)-1)
        
        self.path="recettes/"+str(prompt)+"/"
        ingre=self.path+str(prompt)+"-Ingredients"+str(rd+1)+".png"
        recet=self.path+str(prompt)+"-preparation"+str(rd+1)+".png"
        img1=Image.open(ingre)
        img2=Image.open(recet)
        

        
            
        label = tk.Label(self.toplevel, text=yyyy[rd], font=("Leelawadee",25), fg='black')
        label.pack(side="top")#pady=10
            #Création d'un espace canvas "image chargé"

        self.canvas = tk.Canvas(frame1, width=520, height=400, background='#41B77F')
        self.canvas.create_text("0","0",text="", font="Arial 25",fill="white")
        self.canvas.pack()
        
        img1 = img1.resize((520, 400), Image.ANTIALIAS) 
        self.canvas.image=ImageTk.PhotoImage(img1)
        self.canvas.create_image(0,0,image=self.canvas.image,anchor='nw')

            #Création d'un espace canvas "images déjà chargé"
        self.canvas1 = tk.Canvas(frame2, width=520, height=400, background='#41B77F')
        self.canvas1.create_text("0","0",text="", font="Arial 25",fill="white")
        self.canvas1.pack()
           
        img2 = img2.resize((520, 400), Image.ANTIALIAS) 
        self.canvas1.image=ImageTk.PhotoImage(img2)
        self.canvas1.create_image(0,0,image=self.canvas1.image,anchor='nw')

        button1 = tk.Button(self.toplevel, text="Done",font=("Leelawadee",25),bg='white', fg='#41B77F',
                                command=self.toplevel.destroy)
        button1.pack(side="bottom")
        
            #ajouter
        frame1.pack(side="left")
        frame2.pack(side="right")

      

    def show(self):
        self.toplevel.grab_set()
        self.toplevel.wait_window()
        value = self.var.get()
        return value


    def changeImagePrincipal1(self,img1):
         #resize Image

        img2 = img1.resize((520, 400), Image.ANTIALIAS) 
        self.canvas1.image=ImageTk.PhotoImage(img2)
        self.canvas1.create_image(0,0,image=self.canvas1.image,anchor='nw')
        #print("szerdtfygbhknj,")
        
    def changeImagePrincipal2(self,img2):
         #resize Image
      
        img3 = img2.resize((520, 400), Image.ANTIALIAS) 
        self.canvas1.image=ImageTk.PhotoImage(img3)
        self.canvas1.create_image(0,0,image=self.canvas1.image,anchor='nw')
        
        

class speak(object):
    def __init__(self, parent,stri):
        self.toplevel = tk.Toplevel(parent)
        self.var = tk.StringVar()
        
        label = tk.Label(self.toplevel, text="Vous avez déjà chargé le fruit: " + stri, font=("Leelawadee",25), fg='#41B77F')
        label.pack(expand=YES)
      
        
        button1 = tk.Button(self.toplevel, text="OK",font=("Leelawadee",15),bg='white', fg='#41B77F',
                                command=self.toplevel.destroy)
        button1.pack(side="bottom")
        
    
  
    def show(self):
        self.toplevel.grab_set()
        self.toplevel.wait_window()
        value = self.var.get()
        return value



