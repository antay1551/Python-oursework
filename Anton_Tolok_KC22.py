import numpy as np
import sqlite3
from time import time
from tkinter import Tk, Label
import timeit
from timeit import default_timer as timer

def connect_to_base(): 
     # name of database
     conn = sqlite3.connect('from.sqlite')
     cursor = conn.cursor()
     a = []
     a.append(conn)
     a.append(cursor)
     return a
def create_table( cursor ):
     # create table test with two fields
     try:
         cursor.execute('''CREATE TABLE vocabulary (key INTEGER PRIMARY KEY AUTOINCREMENT,word STRING)''')
     except:
         pass


def insert_into_table( cursor, conn, res ):
     #insert into table vocabulary values from array
     k = 0
     while ( k < len( res  ) ):
           cursor.execute("INSERT INTO vocabulary(word) values (?)",[res[k]])
           k+=1
     conn.commit()


def select_from_table( cursor ):
     #select 
     cursor.execute('SELECT * FROM vocabulary')
     row = cursor.fetchone()
     print(row)
     while row is not None:
         print(row[0])
         print(row[1])
         row = cursor.fetchone()

def uniq_elements( result ):
     #we leave only unique elements
     list_elements = list(set(result))
     list_elements = sorted(list_elements)
     return list_elements

def select_from_table_key( cur, k ):
     #find key into db
     start = timer()
     cur.execute('SELECT * FROM vocabulary where key = '+k)
     row = cur.fetchone()
     toc = time()
     end = timer()     
     entry2.insert(END,end-start)
     return (row)


def drop_sumbols( result ):
     #remove extra characters
     k=0
     while ( k < len(result) ):
          result[k] = re.sub(r"[.,!?:;]", "", result[k])
          k+=1
     return result

def search_key( y, key  ):
     #find key into array
     start = timer()
     s=0
     k = 0
     while ( k < len(y) ):
          if ( int(k) == int(key) ):
               s=1
               break
          k+=1
     end = timer()
     return (end- start)

def search_key_to_unit_test( y, key  ):
     s=0
     k = 0
     while ( k < len(y) ):
          if ( int(k) == int(key) ):
               s=1
               break
          k+=1
     return (s)

def sear( y, key  ):
     s=0
     k = 0
     while ( k < len(y) ):
          if ( int(k) == int(key) ):
               s=1
               break
          k+=1



def split_file( content ):
     result = content.split()
     return result
def get_cursor():
     conn = sqlite3.connect('from.sqlite')
     cursor = conn.cursor()
     return cursor


def find_into_text(event):
     if(entry.get()):
          key = entry.get()
          tex.delete('1.0',END)
          entry1.delete(0, END)
          entry2.delete(0, END)

          #connection to db
          conn = sqlite3.connect('from.sqlite')
          cursor = conn.cursor()
          #create_table( conn )
          #insert_into_table(cursor,  conn, y  )
          #select_from_table( cursor )
          res_of_search_key = search_key( y, key  )
          entry1.insert(END,res_of_search_key)
          result_find = select_from_table_key( cursor , key)
          if(result_find is None ):
               s1=0
          else:
               s1=1
          if ( s1 == 1 ):
               tex.insert(END,"find key"+'\n')
          else:
               tex.insert(END,"do not find key"+'\n')
          tex.tag_add('special','1.0','1.end')
          tex.tag_config('special',background='grey85',font=('Dejavu',18,'bold'))
          # close connect to db
          cursor.close()
          conn.close()


from tkinter import *
window = Tk()
window.geometry("500x300")
but = Button(window,text="Find key", width=20,height=3, bg="white",fg="black")
entry = Entry(window,width=40,bd=10, selectbackground="red")# add entry
entry1 = Entry(window,width=38,bd=10, selectbackground="red")# add entry1
entry2 = Entry(window,width=40,bd=10, selectbackground="red")# add entry2

tex = Text(window,width=40,height=4,font="Verdana 12")


with open("from.txt", "r") as file:
          content = file.read()
result = split_file( content )
result = drop_sumbols( result )
res = uniq_elements( result )
y=np.array([np.array(xi) for xi in res])


label1 = Label(text="Hello Python", fg="#eee", bg="#333")# add label1
label2 = Label(text="Hello Python2", fg="#eee", bg="#333")# add label2
entry.bind("<Return>", find_into_text)
but.bind("<Button-1>", find_into_text)

tex.pack()
entry.pack()
but.pack()

poetry = "time to search in array:"
label3 = Label(text=poetry, justify=LEFT,font="Verdana 12", fg = "red")# add label3
label3.place(relx=.0, rely=.6)
poetry4 = "time to search indatabase:"
label4 = Label(text=poetry4, justify=RIGHT,font="Verdana 12", fg = "red")# add label4
label4.place(relx=.5, rely=.6)

entry1.pack(side = LEFT)
entry2.pack(side = RIGHT)

window.mainloop()# start metod mainloop
