import sqlite3 as s
def Table():
    a=s.connect('C:/Users/Admin/sqlite-tools-win32-x86-3240000/textDB.db')
    cur=a.cursor()

    cur.executescript("""
                    drop table if exists pincode;
                    create table pincode(pincode text,Latitude text,longitude text,post string);
                    insert into pincode values(560000,12.9406234,77.5705272,"");
                    insert into pincode values(560001,12.9706,77.60024,"Bangalore Bazaar");
                    insert into pincode values(560002,12.9715987,77.5945627,"Bangalore City");
                    insert into pincode values(560003,13.0084296,77.5705282,"Malleswaram");
                    insert into pincode values(560004,12.929268,77.6877504,"Basavanagudi");
                    insert into pincode values(560010,12.9931892,77.5521591,"Industrial Estate Bangalore");
                    insert into pincode values(560030,12.9441554,77.6054397,"Adugodi");
                    insert into pincode values(560050,12.9353119,77.5563475,"Ashoknagar");
                    insert into pincode values(560090,13.0796332,77.4948494,"Chikkabanavara");
                    """)

    a.commit()
