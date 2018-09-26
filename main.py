import tkinter as t
import sqlite3 as s
import tkinter.messagebox
import table
import webbrowser
import googlemaps as gm

gmaps=gm.Client(key='AIzaSyANvH4-PbX2D_2-q6hjIwm3_psQlz1yivs')

root=t.Tk()
root.title("Location")
root.geometry("300x200")


def CheckPin():
    global lati
    global long
    flag = False

    passpin=(entry1.get())
    if len(passpin)<6:
        tkinter.messagebox.showinfo("Error!", "Pincode Invalid !")
        exit()
    a = s.connect('C:/Users/Admin/sqlite-tools-win32-x86-3240000/textDB.db')
    cur = a.cursor()

    cur.execute("select * from pincode");

    rows = cur.fetchall()

    for row in rows:
        pin=row[0]
        lati=0
        long=0
        if passpin==pin:
            lati=row[1]
            long=row[2]
            place=row[3]
            flag=True
            break
        else:
            pass

    if flag==True:
        labelR.config(text="Latitude And Longitude Of Pincode: '%s'"%passpin)
        labelR1.config(text="Latitude is '%s'" %lati)
        labelR2.config(text="Longitude is '%s'" %long)

        '''code = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
        place = gmaps.reverse_geocode((40.714224, -73.961452))
        print(place)'''
        url = "http://www.google.com/maps/place/{}-{}/@{},{}/".format(place,passpin,lati,long)
        webbrowser.open_new(url)
        print(url)
    else:
        tkinter.messagebox.showinfo("Error!","Pincode Do Not Match In DataBase !")
        exit()
    a.close()


table.Table()
frame=t.Frame(root,
              bd=1,
              width=15,
              height=4).pack()
label1=t.Label(frame,text="Enter Pincode:")
label1.pack()

label2=t.Label(frame,text="").pack()
v1=t.IntVar()
entry1=t.Entry(frame,textvariable=v1,text="")
entry1.pack()

label3=t.Label(frame,text="").pack()
button=t.Button(frame,text="Submit",command=CheckPin,padx=10,pady=2)
button.pack()

labelR=t.Label(frame,text="")
labelR.pack()
labelR1=t.Label(frame,text="")
labelR1.pack()
labelR2=t.Label(frame,text="")
labelR2.pack()

root.mainloop()