
from email.mime import base
import tkinter as tk
from tkinter import ttk
import psycopg2
import io
from PIL import Image, ImageTk
#from pyparsing import col
LARGEFONT = ("Verdana", 35)
conn=psycopg2.connect(database="miniproject", user='postgres', password='ayeman12345', host='localhost')
cursor=conn.cursor()

cursor.execute("select tablename from pg_tables where schemaname='public';")
tableNames = cursor.fetchall()
tableNames = [x for xs in tableNames for x in xs]


class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (login, StartPage, View, Delete):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, Insert, Update respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(login)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class login(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		
		my_frame1 =tk.LabelFrame(self, text="Log into your account")
		my_frame1.grid(row=0, column=0)

		f_label = tk.Label(my_frame1, text="Username:")
		f_label.grid(row=0, column=0, pady=10, padx=10)

		name = tk.Entry(my_frame1, font=("Helvetica, 13"))
		name.grid(row=0, column=1, pady=10, padx=10)

		f_label1 = tk.Label(my_frame1, text="Password:")
		f_label1.grid(row=1, column=0, pady=10, padx=10)

		name1 = tk.Entry(my_frame1, show='*', font=("Helvetica, 13"))
		name1.grid(row=1, column=1, pady=10, padx=10)

		button1 = tk.Button(my_frame1, text="Log in", command=lambda : controller.show_frame(StartPage))
		button1.grid(row=3, column=0, pady=10, padx=10)

		username=name.get()
		#c.execute("select userid from customer where username='%s'",username)
		#result=c.fetchall()

		results=tk.Label(my_frame1,text="Welcome"+username)
		results.grid(row=4,column=0,pady=10,padx=10)



		Quit = ttk.Button(self, text='Quit', command = controller.destroy)
		Quit.grid(row = 3, column = 1, padx = 10, pady = 10)
		

	def query():
		# Configure and connect to Postgres
		conn = psycopg2.connect(
			host = "127.0.0.1", 
			database = "miniproject",
			user = "postgres",
			password = "ayeman12345", 
			port = "5432",
			)

		# Create a cursor
		c = conn.cursor()


	LARGEFONT = ("Verdana", 35)
	user1='postgres'
	conn=psycopg2.connect(database="miniproject", user=user1, password='ayeman12345', host='localhost')
	cursor=conn.cursor()

	cursor.execute("select tablename from pg_tables where schemaname='public';")
	tableNames = cursor.fetchall()

	tableNames = [x for xs in tableNames for x in xs]
	if( user1!= 'postgres'):
		tableNames = ['orders', 'products', 'customer']

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = ttk.Label(self, text = "Startpage", font = LARGEFONT)
		label.grid(row = 0, column = 1, padx = 10, pady = 10)

		'''button1 = ttk.Button(self, text = "Insert",command = lambda : controller.show_frame(Insert))
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		button2 = ttk.Button(self, text = "Update",command = lambda : controller.show_frame(Update))
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)'''

		button3 = ttk.Button(self, text = "View", command = lambda : controller.show_frame(View))
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)

		button4 = ttk.Button(self, text ="Delete",command = lambda : controller.show_frame(Delete))
		button4.grid(row = 4, column = 1, padx = 10, pady = 10)

		Quit = ttk.Button(self, text='Quit', command = controller.destroy)
		Quit.grid(row = 5, column = 1, padx = 10, pady = 10)
		
'''class Insert(tk.Frame):	
	def __init__(self, parent, controller):		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Insert", font = LARGEFONT)
		label.grid(row = 0, column = 2, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 1, column = 2, padx = 10, pady = 10)

		clicked=tk.StringVar()
		drop = tk.OptionMenu( self , clicked , *tableNames )
		drop.grid(row = 2, column = 2, padx = 10, pady = 10)
		drop.config(width=25)

		def selected_table():
			return clicked.get()
		
		def columns():
			cursor.execute("select * from {0};".format(selected_table()))
			return [desc[0] for desc in cursor.description]

		
		label = ttk.Label(self, text = '')
		#insertText = tk.Text(self, height = 1, width = 50)
		insertValText = tk.Text(self, height = 1, width = 50)
		def selectColumns(*args):
			column_names = columns()
			labelText="Available columns are : {0}".format(column_names)
			label.config(text = labelText)
			label.grid(row = 3, column = 2, padx = 10, pady = 10,  sticky='W', columnspan=5)

			#labelInsert = ttk.Label(self, text="Enter the columns to insert values in : ")
			#labelInsert.grid(row = 4, column = 1, padx = 10, pady = 10,  sticky='W', columnspan=5)
			#insertText.grid(row = 4, column = 2, padx = 10, pady = 10)

			labelInsertVal = ttk.Label(self, text="Enter the values : ")
			labelInsertVal.grid(row = 4, column = 2, padx = 10, pady = 10,  sticky='W', columnspan=5)
			insertValText.grid(row = 4, column = 3, padx = 10, pady = 10)
			
		clicked.trace('w', selectColumns)


		def insVal():
			table=selected_table()
			#selectedColumns = insertText.get(1.0, "end-1c")
			insertVal = insertValText.get(1.0, "end-1c")
			cursor.execute("insert into {0} values ({1});".format(table,insertVal))    	
			#data=cursor.fetchall()
			#out = ttk.Label(self, text=data)
			#out.grid(row = 6, column = 2, padx = 10, pady = 10)
			conn.commit()

		insButton = ttk.Button(self, text = "Insert", command = insVal)
		insButton.grid(row = 20, column = 2, padx = 10, pady = 10)


class Update(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Update", font = LARGEFONT)
		label.grid(row = 0, column = 2, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 1, column = 2, padx = 10, pady = 10)

		clicked=tk.StringVar()
		drop = tk.OptionMenu( self , clicked , *tableNames )
		drop.grid(row = 2, column = 2, padx = 10, pady = 10)
		drop.config(width=25)

		def selected_table():
			return clicked.get()
		
		def columns():
			cursor.execute("select * from {0};".format(selected_table()))
			return [desc[0] for desc in cursor.description]

		
		label = ttk.Label(self, text = '')
		insertText = tk.Text(self, height = 1, width = 50)
		insertValText = tk.Text(self, height = 1, width = 50)
		conditionText = tk.Text(self, height = 1, width = 50)
		def selectColumns(*args):
			column_names = columns()
			labelText="Available columns are : {0}".format(column_names)
			label.config(text = labelText)
			label.grid(row = 3, column = 2, padx = 10, pady = 10,  sticky='W', columnspan=5)

			labelInsert = ttk.Label(self, text="Enter the column to alter values in : ")
			labelInsert.grid(row = 4, column = 2, padx = 10, pady = 10,  sticky='W', columnspan=5)
			insertText.grid(row = 4, column = 3, padx = 10, pady = 10)

			labelInsertVal = ttk.Label(self, text="Enter the value : ")
			labelInsertVal.grid(row = 5, column = 2, padx = 10, pady = 10,  sticky='W', columnspan=5)
			insertValText.grid(row = 5, column = 3, padx = 10, pady = 10)

			conditionLabel = ttk.Label(self, text="Enter the Condition : ")
			conditionLabel.grid(row = 6, column = 2, padx = 10, pady = 10,  sticky='W', columnspan=5)
			conditionText.grid(row = 6, column = 3, padx = 10, pady = 10)
			
		clicked.trace('w', selectColumns)


		def upTab():
			table=selected_table()
			selectedColumns = insertText.get(1.0, "end-1c")
			insertVal = insertValText.get(1.0, "end-1c")
			condition = conditionText.get(1.0, "end-1c")
			cursor.execute("update {0} set {1}={2} where {3}".format(table,selectedColumns,insertVal,condition))
			#data=cursor.fetchall()
			#out = ttk.Label(self, text=data)
			#out.grid(row = 6, column = 2, padx = 10, pady = 10)
			conn.commit()

		upButton = ttk.Button(self, text = "Update", command = upTab)
		upButton.grid(row = 20, column = 2, padx = 10, pady = 10)

'''
class View(tk.Frame):	
	def __init__(self, parent, controller):	
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="View", font = LARGEFONT)
		label.grid(row = 0, column = 2, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 1, column = 2, padx = 10, pady = 10)

		clicked=tk.StringVar()
		drop = tk.OptionMenu( self , clicked , *tableNames )
		drop.grid(row = 2, column = 2, padx = 10, pady = 10)
		drop.config(width=25)

		def selected_table():
			return clicked.get()
		
		def columns():
			cursor.execute("select * from {0};".format(selected_table()))
			return [desc[0] for desc in cursor.description]

		
		label = ttk.Label(self, text = '')
		selectText = tk.Text(self, height = 1, width = 50)
		def selectColumns(*args):
			column_names = columns()
			labelText="Available columns are : {0}".format(column_names)
			label.config(text = labelText)
			label.grid(row = 3, column = 2, padx = 10, pady = 10,  sticky='W', columnspan=5)

			labelSelect = ttk.Label(self, text="Enter the columns to be selected : ")
			labelSelect.grid(row = 4, column = 2, padx = 10, pady = 10,  sticky='W', columnspan=5)
			selectText.grid(row = 4, column = 3, padx = 10, pady = 10)
			
		clicked.trace('w', selectColumns)


		def viewVal():
			
			table=selected_table()
			selectedColumns = selectText.get(1.0, "end-1c")
			cursor.execute("select {0} from {1};".format(selectedColumns,table))    	
			data=cursor.fetchall()
			#print(data[1])
			#print(selectColumns)
			column_names=columns()
			if("photo" in column_names):
				root=tk.Toplevel()
				vertical_scrollbar = ttk.Scrollbar(root)
				vertical_scrollbar.pack(side="right", fill="both")

				my_tree = ttk.Treeview(root,height=1080, yscrollcommand= vertical_scrollbar.set)
				my_tree.pack()

				vertical_scrollbar.config(command= my_tree.yview)

				style = ttk.Style(root)
				style.theme_use("winnative")
				style.configure(".", font=("Helvetica", 11))
				style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))
				style.configure("Treeview", rowheight=50) # set row height

				my_tree['columns'] = ["productid","price","description"]
				my_tree.column("#0", width=100, stretch='NO') # set width
				my_tree.column("productid", width=100, anchor='w')
				my_tree.column("price", width=100, anchor='w')
				my_tree.column("description", width=200, anchor='w')
				my_tree.heading("#0", anchor='w', text='Photo')
				my_tree.heading("productid", anchor='w', text="productId")
				my_tree.heading("price", anchor='w', text="price")
				my_tree.heading("description", anchor='w', text="description")
				'''my_tree.column("#0",width=150, stretch='NO')
				for i in column_names:
					if(i!="photo"):
						my_tree.column(i,width=150, anchor='w')
				my_tree.heading("#0",anchor='w', text='photo')
				for i in column_names:
					if(i!='photo')
					my_tree.heading(i,anchor='w', text=i)'''
				count = 0

				my_tree.imglist = []
				for record in data:
					img = Image.open(io.BytesIO(record[2]))
					#print(img)
					img.thumbnail((50,50)) # resize the image to desired size
					img = ImageTk.PhotoImage(img)
					my_tree.insert(parent="", index="end", iid=count,image=img, values=(record[0],record[1],record[3])) # use "image" option for the image
					my_tree.imglist.append(img) # save the image reference
					count += 1
			else:

				for i in range(len(data)):
					#print('\n')
					for j in range(len(data[i])):
						#print(data[i][j],end=' ')
						self.e = ttk.Entry(self, width=20)
						self.e.grid(row=i+6, column=j+1)
						self.e.insert(tk.END, data[i][j])
				#tk.Frame.__init__(self, parent)
			def dest():
				for i in range(len(data)):
					for j in range(len(data[i])):
						self.e = ttk.Entry(self, width=20)
						self.e.grid(row=i+6, column=j+1)
						self.e.destroy
			destroybutton = ttk.Button(self, text = "Destroy", command = dest)
			destroybutton.grid(row = 20, column = 3, padx = 10, pady = 10)
		
		viewButton = ttk.Button(self, text = "View", command = viewVal)
		viewButton.grid(row = 20, column = 2, padx = 10, pady = 10)

class Delete(tk.Frame):	
	def __init__(self, parent, controller):		
		tableNames=['orders','customer']
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Delete", font = LARGEFONT)
		label.grid(row = 0, column = 2, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 1, column = 2, padx = 10, pady = 10)

		clicked=tk.StringVar()
		drop = tk.OptionMenu( self , clicked , *tableNames )
		drop.grid(row = 2, column = 2, padx = 10, pady = 10)
		drop.config(width=25)

		def selected_table():
			return clicked.get()
		
		def columns():
			cursor.execute("select * from {0};".format(selected_table()))
			return [desc[0] for desc in cursor.description]

		
		label = ttk.Label(self, text = '')
		conditionText = tk.Text(self, height = 1, width = 50)
		def selectColumns(*args):
			column_names = columns()
			labelText="Available columns are : {0}".format(column_names)
			label.config(text = labelText)
			label.grid(row = 3, column = 2, padx = 10, pady = 10,  sticky='W', columnspan=5)

			conditionLabel = ttk.Label(self, text="Enter the Condition : ")
			conditionLabel.grid(row = 4, column = 2, padx = 10, pady = 10,  sticky='W', columnspan=5)
			conditionText.grid(row = 4, column = 3, padx = 10, pady = 10)
			
		clicked.trace('w', selectColumns)


		def delTab():
			table=selected_table()
			condition = conditionText.get(1.0, "end-1c")
			cursor.execute("delete from {0} where {1}".format(table,condition))
			#data=cursor.fetchall()
			#out = ttk.Label(self, text=data)
			#out.grid(row = 6, column = 2, padx = 10, pady = 10)
			conn.commit()

		delButton = ttk.Button(self, text = "Delete", command = delTab)
		delButton.grid(row = 20, column = 2, padx = 10, pady = 10)


app = tkinterApp()
#base.mainloop()
app.mainloop()
conn.close()