
import sqlite3

conn = sqlite3.connect('dbassignment.db')

#create table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit()
conn.close()


#here is our list of files we are going to search
fileList = ('information.docx','Hello.txt','myImage.png' \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


conn = sqlite3.connect('dbassignment.db')

#determining which files end in .txt before adding to the database
with conn:
    cur = conn.cursor()
    for fileName in fileList:
        if fileName.endswith(".txt"):
            cur.execute("INSERT INTO tbl_file(col_fname) VALUES (?)", \
                        (fileName,))
            print(fileName)
        conn.commit()
conn.close()
        
