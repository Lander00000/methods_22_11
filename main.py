import mysql.connector
from datetime import datetime
from prettytable import PrettyTable

con = mysql.connector.connect(host="localhost", user="root", password="", database="methods")
cursor = con.cursor(buffered=True)


def main():
    global cur_user
    menutext = """1. Display Books
2. View Cart
3. Add Item to Cart
4. Remove Item from Cart
5. View Order History
6. Edit Shipping Information
7. Edit Payment Information
8. Delete Account
9. Log Out\n"""
    cur_user = ""
    active = 1
    while active:
        while cur_user == "":
            user = input("Username:")
            password = input("Password:")
            if not trystr(user) or not trystr(password):
                pass
            if login(user, password):
                pass
            else:
                print("username and/or password incorrect")
                pass
        print(menutext)
        x = input("What would you like to do?(numeric input)")
        if not tryint(x):
            continue
        if x == 1:
            filter = input("enter genre here or leave blank:")
            if not trystr(table):
                pass
            display("book", filter)
            pass
        elif x == 2:
            display("cart", cur_user)
            pass
        elif x == 3:
            
            pass
        elif x == 4:
            pass
        elif x == 5:
            pass
        elif x == 6:
            pass
        elif x == 7:
            pass
        elif x == 100:
            active = 0
            print("exiting menu")
        else:
            print("Error: invalid input")

def display(tablename, genrefilter=""):
    if tablename == "user" or tablename == "book" or tablename == "transaction" or tablename == "cart":
        query1 = "select Column_name from Information_schema.columns where Table_name = '" + tablename + "'"
    else:
        return False
    cursor.execute(query1)
    table1 = cursor.fetchall()
    list = []
    for col in table1:
        list.append(col[0])
    if tablename == "user":
        list = ["username", "password", "name", "shippinginfo", "paymentinfo"]
    table3 = PrettyTable(list)

    query2 = "select * from " + tablename
    cursor.execute(query2)
    table2 = cursor.fetchall()
    for row in table2:
        list = []
        for item in row:
            list.append(item)
        if genrefilter == "":
            table3.add_row(list)
        elif tablename == "book" and row[-1] == genrefilter:
            table3.add_row(list)
        elif tablename == "transaction" and row[1] == genrefilter:
            table3.add_row(list)
        elif tablename == "cart" and row[0] == genrefilter:
            table3.add_row(list)
    print(table3)
    return True


def login(user, password):
    query1 = "SELECT * FROM `user` WHERE username = '{}'".format(user)
    cursor.execute(query1)
    table1 = cursor.fetchall()
    if not table1:
        return False
    if user == table1[0][0] and password == table1[0][1]:
        global cur_user
        cur_user = user
        return True
    return False


def logout():
    global cur_user
    cur_user = ""


def update_shipping(user, newship):
    query1 = "SELECT * FROM `user` WHERE username = '{}'".format(user)
    cursor.execute(query1)
    table1 = cursor.fetchall()
    if not table1:
        return False
    query = "UPDATE `user` SET `shippinginfo`='{}' WHERE username = '{}'".format(newship, user)
    cursor.execute(query)
    con.commit()
    return True


def update_payment(user, newpay):
    query1 = "SELECT * FROM `user` WHERE username = '{}'".format(user)
    cursor.execute(query1)
    table1 = cursor.fetchall()
    if not table1:
        return False
    query = "UPDATE `user` SET `paymentinfo`='{}' WHERE username = '{}'".format(newpay, user)
    cursor.execute(query)
    con.commit()
    return True


def empty(user):
    query1 = "select * from `cart` where username = '{}'".format(user)
    cursor.execute(query1)
    table = cursor.fetchall()
    if not table:
        return False
    for row in table:
        loc = 0
        for item in row:
            if loc != 0:
                if item > 0:
                    query2 = "update `cart` set `b{}` = 0 where username = '{}'".format(loc, user)
                    cursor.execute(query2)
            loc += 1
    con.commit()
    return True


def add_transaction(user, list, cost, date):
    query = "INSERT INTO `transaction`(`username`, `purchaseList`, `cost`, `date`) VALUES ('{}','{}','{}','{}')".format(user, list, cost, date)
    cursor.execute(query)


def add_stock(count, book):
    query1 = "SELECT `stock` FROM `book` WHERE bookid = '{}'".format(book)
    cursor.execute(query1)
    table1 = cursor.fetchall()
    if not table1:
        return False
    newcount = table1[0][0] + count
    query2 = "update `book` set `stock` = '{}' where bookid = '{}'".format(newcount, book)
    cursor.execute(query2)
    con.commit()
    return True


def remove_stock(count, book):
    query1 = "SELECT `stock` FROM `book` WHERE bookid = '{}'".format(book)
    cursor.execute(query1)
    table1 = cursor.fetchall()
    if not table1:
        return False
    newcount = table1[0][0] - count
    if newcount < 0:
        return False
    query2 = "update `book` set `stock` = '{}' where bookid = '{}'".format(newcount, book)
    cursor.execute(query2)
    return True


def transact(user):
    running_total = 0
    running_string = ""
    query1 = "select * from `cart` where username = '{}'".format(user)
    cursor.execute(query1)
    table1 = cursor.fetchall()
    if not table1:
        return False
    for row in table1:
        loc = 0
        for item in row:
            if loc != 0:
                if item > 0:
                    query2 = "select price, isbn from `book` where bookid = '{}'".format(loc)
                    cursor.execute(query2)
                    table2 = cursor.fetchall()
                    if not remove_stock(item, loc):
                        return False
                    running_total += (item * table2[0][0])
                    running_string += table2[0][1] + "_" + str(item) + "_"
            loc += 1
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    add_transaction(user, running_string, running_total, date_time)
    empty(user)
    return True


def addbook(user, bookid, count):
    query1 = "select `b{}` from `cart` where username = '{}'".format(bookid, user)
    cursor.execute(query1)
    table = cursor.fetchall()
    if not table:
        return False
    query2 = "UPDATE `cart` SET `b{}`='{}' WHERE username = '{}'".format(bookid, (count+table[0][0]), user)
    cursor.execute(query2)
    con.commit()
    return True


def removebook(user, bookid, count):
    query1 = "select `b{}` from `cart` where username = '{}'".format(bookid, user)
    cursor.execute(query1)
    table = cursor.fetchall()
    if not table:
        return False
    query2 = "UPDATE `cart` SET `b{}`='{}' WHERE username = '{}'".format(bookid, (table[0][0]-count), user)
    cursor.execute(query2)
    con.commit()
    return True


def view_single_history(user):
    query1 = "select * from `transaction` where username = '{}'".format(user)
    cursor.execute(query1)
    table = cursor.fetchall()
    if not table:
        return False


def add_cart_item(user):
    query = "INSERT INTO `cart`(`username`) VALUES ('{}')".format(user)
    cursor.execute(query)
    con.commit()


def add_book_item(isbn, title, author, published, stock, price, genre):
    query1 = "INSERT INTO `book`(`isbn`, `title`, `author`, `published`, `stock`, `price`, `genre`) VALUES ('{}','{}','{}','{}','{}','{}', '{}')".format(isbn, title, author, published, stock, price, genre)
    cursor.execute(query1)
    query2 = "select * from `book` where isbn = '{}'".format(isbn)
    cursor.execute(query2)
    table = cursor.fetchall()
    query3 = "ALTER TABLE `cart` ADD b{} INT NOT NULL DEFAULT 0".format(table[0][0])
    cursor.execute(query3)
    con.commit()


def add_user_item(username, password, name, shippinginfo, paymentinfo):
    query = "INSERT INTO `user`(`username`, `password`, `name`, `shippinginfo`, `paymentinfo`) VALUES ('{}','{}','{}','{}','{}')".format(username, password, name, shippinginfo, paymentinfo)
    add_cart_item(username)
    cursor.execute(query)
    con.commit()


def delete_user(user):
    query1 = "SELECT * FROM `user` WHERE username = '{}'".format(user)
    cursor.execute(query1)
    table1 = cursor.fetchall()
    if not table1:
        return False
    query2 = "DELETE FROM `transaction` WHERE username = '{}'".format(user)
    cursor.execute(query2)
    query3 = "DELETE FROM `cart` WHERE username = '{}'".format(user)
    cursor.execute(query3)
    query4 = "DELETE FROM `user` WHERE username = '{}'".format(user)
    cursor.execute(query4)
    con.commit()


def trystr(x):
    try:
        str(x)
    except:
        print("Error: enter string input\n")
        return False
    return True


def tryint(x):
    try:
        int(x)
    except:
        print("Error: enter integer input\n")
        return False
    return True


if __name__ == '__main__':
    main()
