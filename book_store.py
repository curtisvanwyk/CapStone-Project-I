import sqlite3
db = sqlite3.connect('data_bookstore/ebookstore_db')
cursor = db.cursor()  
   
db.commit()

Create a table called "books" with that accepts "id", "Title", "Author" and "Qty" as keys
cursor.execute('''
    CREATE TABLE books(id INTEGER, Title TEXT,    
                   	Author Text, Qty INTEGER)
''')

db.commit()

id_1 = 3001
title_1 = 'A Tale of Two Cities'
author_1 = 'Charles Dickens'
qty_1 = 30

id_2 = 3002
title_2 = 'Harry Potter and the Philosopher\'s Stone'
author_2 = 'J.K. Rowling'
qty_2 = 40

id_3 = 3003
title_3 = 'The Lion, the Witch and the Wardrobe'
author_3 = 'C.S. Lewis'
qty_3 = 25

id_4 = 3004
title_4 = 'The  Lord of the Rings'
author_4 = 'J.R.R. Tolkien'
qty_4 = 37

id_5 = 3005
title_5 = 'Alice in Wonderland'
author_5 = 'Lewis Carroll'
qty_5 = 12

id_6 = 3006
title_6 = 'Homo Deus'
author_6 = 'Yuvul Noah Harari'
qty_6 = 66

id_7 = 3007
title_7 = 'Messiah'
author_7 = 'Boris Starling'
qty_7 = 56

id_8 = 3008
title_8 = 'On the Bone'
author_8 = 'Barbara Nadel'
qty_8 = 18

id_9 = 3009
title_9 = 'The Hitchhikers Guide to the Galaxy'
author_9 = 'Douglas Adams'
qty_9 = 11

id_10 = 3010
title_10 = 'The Unlikely Pilgrimlage of Harold Key'
author_10 = 'Rachel Joyce'
qty_10 = 29

id_11 = 3011
title_11 = 'Emotional Intelligence'
author_11 = 'Daniel Goleman'
qty_11 = 2

books = [(id_1,title_1,author_1, qty_1),(id_2,title_2,author_2, qty_2),(id_3,title_3,author_3, qty_3),
         (id_4,title_4,author_4, qty_4),(id_5,title_5,author_5, qty_5),(id_6,title_6,author_6, qty_6),
         (id_7,title_7,author_7, qty_7),(id_8,title_8,author_8, qty_8),(id_9,title_9,author_9, qty_9),
         (id_10,title_10,author_10, qty_10),(id_11,title_11,author_11, qty_11)]

cursor.executemany('''INSERT INTO books(id, Title, Author, Qty)VALUES(?,?,?,?)''', books)    #To insert several entries at once, use executemany()

db.commit()

user_input = ""

while user_input != 0:    #Use conditional statements to execute specific pieces of code depending on user input

    user_input = int(input("\nWould you like to: \n1) Enter Book \n2) Update Book \n3) Delete Book \n4) Search Book \n0) Exit"))

    if user_input == 1:

        #To insert a single row into a table, use INSERT statement
        cursor = db.cursor()
        
        id_db = int(input('ID number: '))
        title_db = input('Title: ')
        author_db = input('Author: ')
        qty_db = int(input('Quantity available: '))

        cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
                           VALUES(?,?,?,?)''',(id_db, title_db, author_db, qty_db))

        print("\n" + title_db + " inserted.")
        db.commit()
    
    elif user_input == 2:

        #Allow user to update data 
        author = input('Enter the author of the book you would like to update: ')
        id = int(input('Please enter updated id number: '))
        title = input('Please enter updated title: ')
        qty = int(input('Please enter quantity available: '))
        Author = author

        cursor.execute('''UPDATE books SET id = ? WHERE Author = ?''', (id, Author))
        cursor.execute('''UPDATE books SET Title = ? WHERE Author = ?''', (title, Author))
        cursor.execute('''UPDATE books SET Qty = ? WHERE Author = ?''', (qty, Author))
        
        print('Updated!')

        db.commit()

    elif user_input == 3:

        #To delete a row, use the DELETE statement
        id = int(input('Enter the id number of the book you would like to delete: '))
        cursor.execute('''DELETE FROM books WHERE id = ? ''', (id,))
        print('Book number %d deleted' %id)

    elif user_input == 4:
        #To retrieve data, execute a SELECT SQL statement against the cursor object and use fetchone() to retrieve the row
        id = int(input('Enter the id number of the book you would like to retrieve: '))
        cursor.execute('''SELECT Title, Author FROM books WHERE id = ?''', (id,))
        book = cursor.fetchone()
        print(book)

        db.commit()

    else:
        print("Thank You!")
        

db.commit()
db.close()    #Close the connection to the database

