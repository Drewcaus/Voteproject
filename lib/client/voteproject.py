
import sys
import Tkinter as tk # Tkinter = python2
from Tkinter import *
import ttk #pretty button/label library --cant get this to work

from hasher import hasher #hasher modual

LARGE_FONT= ("Verdana", 12) #global varible
MID_FONT= ("Verdana", 10)

#define class

LARGE_FONT= ("Verdana", 12) #global varible

#define class

#_________________________________________________________________________________________
class voteproject(tk.Tk): #inherantance
	def __init__(self, *args, **kwargs):#init is initialitation, args are varibles being passed though, kwargs are keywork varibles
		
		tk.Tk.__init__(self, *args, **kwargs) #initilize tk
		

		#tk.Tk.iconbitmap(self, default= "bulb.xbm") #broken
		tk.Tk.wm_title(self,"VoteProject: Smart Democracy") #Works
		
		container = tk.Frame(self) #made a frame
		container.pack(side="top", fill="both", expand = True) #pack the space, to the top, expand says you can go beyond the page
		container.grid_rowconfigure(0, weight=1) #weight is like priority 
		container.grid_columnconfigure(0, weight=1)	

				#creates frame size and centers with screen
		container.width = container.winfo_screenwidth()/2
		container.height = container.winfo_screenheight()/2
		xmax= container.winfo_screenwidth()
		ymax= container.winfo_screenheight()
		x0 =container.x0 = xmax/2 - container.width/2
		y0 =container.y0 = ymax/2 - container.height/2
		self.geometry("%dx%d+%d+%d" % (container.width, container.height, x0, y0))	
		self.frames = {}

	
		for F in (loginpage,authpage,votepage,resultpage): #loop to have multiple frames!!! 
			frame = F(container, self,) #created the startframe	
			self.frames[F] = frame
			frame.grid(row=0, column =0, sticky="nsew") #must predefine the grid, sticky =northsoutheastswest....kinda like allignment
			frame=tk.Frame(self, background = 'white') #isnt working
		self.show_frame(loginpage) 	


	def show_frame(self, cont):
		
		frame= self.frames[cont] 
		frame.tkraise() #raises to the front
		
	def qf(param): #qf is quickfunction
		print(param)
			
#___________________________________________________________________________________________
class splashscreen(tk.Toplevel):	#displays popup widget
	def __init__(self,parent,image=None,timeout=1000): #master or parent
		#create splash screen with image - timeout in Millisecs 
		
		tk.Toplevel.__init__(self,parent,relief='raised',borderwidth=5,bg='white') #master or parent..???
		self.main=parent
		
		#do not show main window
		self.main.withdraw()
		self.overrideredirect(1)
		
		#PhotoImage for .gif files
		self.image = tk.PhotoImage(file=image)
		self.after_idle(self.centerOnScreen) 
		
		self.update()
		self.after(timeout,self.destroySplash)

	def centerOnScreen(self): 
		self.update_idletasks()
		self.width,self.height=self.image.width(),self.image.height() #screen = image size 
		
		xmax= self.winfo_screenwidth()
		ymax= self.winfo_screenheight()
		
		x0 =self.x0 = xmax/2 - self.width/2
		y0 =self.y0 = ymax/2 - self.height/2
		self.geometry("%dx%d+%d+%d" % (self.width, self.height, x0, y0))
		self.createSplash()
		 
	def createSplash(self):
        # show the splash image
		self.canvas = tk.Canvas(self, height=self.height, width=self.width)
		self.canvas.create_image(0,0, anchor='nw', image=self.image)
		self.canvas.pack()
        
	def destroySplash(self):
        # bring back main window and destroy splash screen
		self.main.update()
		self.main.deiconify()
		self.withdraw()		
        
#___________________________________________________________________________________       		
		
class loginpage(tk.Frame): #This is the main page for log in 
	def __init__(self,parent,controller): 
		tk.Frame.__init__(self,parent)			
			#just to see the page
			

		label0= tk.Label(self, text="VoteProject Login", font=LARGE_FONT) #reference GloVar, this is how you add text in tk
		label0.grid(row=0,column=0)
		
		label1 = tk.Label(self, text= "First Name",font=MID_FONT)			
		label2 = tk.Label(self, text= "Last Name", font=MID_FONT)
		label3 = tk.Label(self, text= "Email Name", font=MID_FONT)		
		
		#innitiate the entry varriables. 
		self.fn=tk.StringVar() 
		self.ln=tk.StringVar()
		self.em=tk.StringVar()		
		#entry input -> variable
		entry1 = tk.Entry(self,textvariable = self.fn)
		entry2 = tk.Entry(self,textvariable =self.ln)		
		entry3 = tk.Entry(self,textvariable =self.em)
		
		#login page grid work...terrible formating come back and fix lol 
		label1.grid(row=1,column=0)
		entry1.grid(row=1,column=2)
		
		label2.grid(row=2,column=0)
		entry2.grid(row=2,column=2)
		
		label3.grid(row=3,column=0)
		entry3.grid(row=3,column=2)	
		
		#button calls button function 											
		button1 = tk.Button(self,text="Login",command=lambda: self.buttonfuction())
		button1.grid(row=4,column=0)
		
		#returns from sanitize(), hashes (hasher.py), then goes to AuthPage 
	def buttonfuction(self):
	
		fname = self.sanitize(self.fn.get())
		lname = self.sanitize(self.ln.get())
		email = self.sanitize(self.em.get())
		
		#Calls hasher.py
		h = hasher()
		hashdata = h.hash([fname,lname,email])
		
		#goes to next page for auth. 
		c = controller.show_frame
		controller.show_frame(authpage,hashdata)
		
		#retrieves and sanitizes the data 
	def sanitize(self,inn):
		san = str(inn) #The error is being caused by reading tomany keyboard inputs...i think
		san = san.replace(' ', '') #replaces all white space with no space
		san = san.lower()
		san = san.title()
		return san
			
#___________________________________________________________________________________________________________			

class authpage(tk.Frame): 
	def __init__(self,parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self, text="Start Page", font=LARGE_FONT) #reference GloVar, this is how you add text in tk
		label.pack(pady=10,padx=10)
			

		button4 = ttk.Button(self, text="Go Vote!",command=lambda: controller.show_frame(votepage))
		button4.pack()
		
		'''
		http request
		authenticate with server
		if yes
			go to next page
		'''
		
		
		button4 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(votepage))
		button4.pack()

class votepage(tk.Frame): 
	def __init__(self,parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self, text="Page Two!!", font=LARGE_FONT) #reference GloVar, this is how you add text in tk
		label.pack(pady=10,padx=10)
			
		button2 =ttk.Button(self, text="Page One ",command=lambda: controller.show_frame(loginpage))
		button2.pack()	
		
		button3 = ttk.Button(self, text="Back to Home ",command=lambda: controller.show_frame(authpage))
		button3.pack()

		"""
		embed canadate wallet address
		create address
		reward coin
		"""
		
		
#def sel():
#selection = "You selected the option " + str(var.get())
#label.config(text = selection)

#root = Tk()
#var = IntVar()
#R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
	  #command=sel)
#R1.pack( anchor = W )

#R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
	  #command=sel)
#R2.pack( anchor = W )

#R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
	  #command=sel)
#R3.pack( anchor = W)

#label = Label(root)
#label.pack()

		 

		 ##CREATE RADIO BUTTONS
        #RADIO_BUTTON = [
            #("This will display A", "A"),
            #("This will display B","B")
        #]
 
        ##initialize a variable to store the selected value of the radio buttons
        ##set it to A by default
        #self.radio_var = StringVar()
        #self.radio_var.set("A")
 
        ##create a loop to display the RADIO_BUTTON
        #i=0
        #for text, item in RADIO_BUTTON:
            ##setup each radio button. variable is set to the self.radio_var
            ##and the value is set to the "item" in the for loop
            #self.radio = Radiobutton(self.master, text=text, variable=radio_var, value=item)
            #self.radio.grid(row=2, column=i)
            #i += 1
 
        ##now for a button
        #self.submit = Button(self.master, text="Execute!", command=self.start_processing, fg="red")
        #self.submit.grid(row=3, column=0)
 
		
class resultpage(tk.Frame): 
	def __init__(self,parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = tk.Label(self, text="Start Page", font=LARGE_FONT) #reference GloVar, this is how you add text in tk
		label.pack(pady=10,padx=10)
			
		button4 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(Pagetwo))

		button4.pack()
		
		

#mainwindow	
#the Voteproject logo for splash screen (gif) 

if __name__=="__main__":
	import os
	app = voteproject()
	image_file="voteproject.gif"
	assert os.path.exists(image_file)
	s=splashscreen(app,timeout=2000,image=image_file)					
	app.mainloop() #mainscreen wont stop
