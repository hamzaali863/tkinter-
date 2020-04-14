from  tkinter import *
from PIL import ImageTk,Image
import sqlite3
root=Tk()
root.title('ha')
root.iconbitmap('E:\COURSERA\man.ico')
root.geometry("400x600")

#Database
#create database
conn= sqlite3.connect('addres-_book.db')
c=conn.cursor()
#creat table
'''
c.execute(""" CREATE TABLE ADDR(
    first_name text,
    last_name text,
    address text,
    state text,
    city text,
    zipcode integer
         ) """)
'''

def submit():
    #create database
    conn= sqlite3.connect('addres-_book.db')
    c=conn.cursor()

    #insert Into table
    c.execute("INSERT INTO ADDR VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address':address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
        })
    #commit changes
    conn.commit()
    #close connection
    conn.close()


 #clear the text boxes
    f_name_edittor.delete(0,END)
    l_name_edittor.delete(0,END)
    address_edittor.delete(0,END)
    city_edittor.delete(0,END)
    state_edittor.delete(0,END)
    zipcode_edittor.delete(0,END)
 #creat Query function 
def query():
    conn=sqlite3.connect('addres-_book.db')
    c=conn.cursor()
    #
    c.execute("SELECT * ,oid FROM ADDR")
    records= c.fetchall()
    print_records= ''
    for record in records:
        print_records += str(record[0])+" "+str(record[1])+'  '+str(record[6])+"\n"
    query_lab=Label(root,text=print_records)
    query_lab.grid(row=8,column=0,columnspan=2)    

    conn.commit()
    conn.close()

#creat delete function
def Drop():
    conn=sqlite3.connect('addres-_book.db')
    c=conn.cursor()
    #
    c.execute("DELETE FROM ADDR WHERE oid = " + delete_box.get())
    conn.commit()
    conn.close()
#create edite function
def update():
    conn=sqlite3.connect('addres-_book.db')
    c=conn.cursor()
    #
    record_id= delete_box.get()
    c.execute("""UPDATE ADDR SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city   = :city,
        state  = :state,
        zipcode = :zipcode 

        WHERE oid = :oid""",
        {
        'first': f_name_edittor.get(),
        'last': l_name_edittor.get(),
        'address' : address_edittor.get(),
        'city' : city_edittor.get(),
        'state' : city_edittor.get(),
        'zipcode': zipcode_edittor.get(),
        'oid':record_id
        }) 
        
    conn.commit()
    conn.close()
    edittor.destroy()
 #clear the text boxes
   



def edit():
    global edittor
    edittor=Tk()
    edittor.title('update records')
    edittor.iconbitmap('E:\COURSERA\man.ico')
    edittor.geometry("400x600")

    conn=sqlite3.connect('addres-_book.db')
    c=conn.cursor()
    #
    record_id = delete_box.get()
    c.execute("SELECT *  FROM ADDR WHERE oid = " + record_id)

    records = c.fetchall()


    #cereat global function dor text
    global f_name_edittor
    global l_name_edittor
    global address_edittor
    global city_edittor 
    global state_edittor
    global zipcode_edittor
    #creat text boxes
    f_name_edittor=Entry(edittor,width=30)
    f_name_edittor.grid(row=0,column=1,padx=20)
    l_name_edittor=Entry(edittor,width=30)
    l_name_edittor.grid(row=1,column=1,padx=20,pady=(10,0))
    address_edittor=Entry(edittor,width=30)
    address_edittor.grid(row=2,column=1,padx=20)
    city_edittor=Entry(edittor,width=30)
    city_edittor.grid(row=3,column=1,padx=20)
    state_edittor=Entry(edittor,width=30)
    state_edittor.grid(row=4,column=1,padx=20)
    zipcode_edittor=Entry(edittor,width=30)
    zipcode_edittor.grid(row=5,column=1,padx=20)

    #creat text box label
    f_name_label=Label(edittor,text="First Name")
    f_name_label.grid(row=0,column=0,padx=20)
    l_name_label=Label(edittor,text="last Name")
    l_name_label.grid(row=1,column=0,pady=(10,0))
    adress_label=Label(edittor,text="Adress")
    adress_label.grid(row=2,column=0)
    city_label=Label(edittor,text="City")
    city_label.grid(row=3,column=0)
    state_label=Label(edittor,text="State")
    state_label.grid(row=4,column=0)
    zipcode_label=Label(edittor,text="zipecode")
    zipcode_label.grid(row=5,column=0)
    
    for record in records:
        f_name_edittor.insert(0,record[0])
        l_name_edittor.insert(0,record[1])
        address_edittor.insert(0,record[2])
        city_edittor.insert(0,record[3])   
        state_edittor.insert(0,record[4])
        zipcode_edittor.insert(0,record[5])
    
    save_btn=Button(edittor,text="save",command=update)
    save_btn.grid(row =6,column=1,padx=10,pady=10,ipadx=70)

'''/////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////'''    
#creat text boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20,pady=(10,0))
address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)
city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)
state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)
delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,padx=20)

#creat text box label
f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0,padx=20)
l_name_label=Label(root,text="last Name")
l_name_label.grid(row=1,column=0,pady=(10,0))
adress_label=Label(root,text="Adress")
adress_label.grid(row=2,column=0)
city_label=Label(root,text="City")
city_label.grid(row=3,column=0)
state_label=Label(root,text="State")
state_label.grid(row=4,column=0)
zipcode_label=Label(root,text="zipecode")
zipcode_label.grid(row=5,column=0)
delete_label=Label(root,text="ID Number")
delete_label.grid(row=9,column=0)
#///////////////////////////////


#creat submite buttom
submit_btn=Button(root,text="Add record to database",command=submit)
submit_btn.grid(row=6 ,column=0,columnspan=2,padx=10,pady=10,ipadx=130)

#creat query butn
query_btn=Button(root,text="show record",command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

#creat Delet bttuon
del_btn=Button(root,text="Delete",command=Drop)
del_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

edit_btn=Button(root,text="Edite Records",command=edit)
edit_btn.grid(row=13,column=0,columnspan=2,padx=10,pady=10,ipadx=139)


#commit changes
conn.commit()
#close connection
conn.close()


root.mainloop()
