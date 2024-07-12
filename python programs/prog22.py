import mariadb as DB
class DBHelper:
    def __init__(self):
        self.db = DB.connect(host="localhost", username="root", password="")
        self.cur = self.db.cursor()
        self.cur.execute("Create Database if not exists kb")
        self.db = DB.connect(host="localhost", username="root", password="", database="kb")
        self.cur = self.db.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS kb (id int PRIMARY KEY AUTO_INCREMENT,name char(200) , pwd char(200))")

    def insert(self, name, pwd):
        res = self.cur.execute(f"INSERT INTO kb(name,pwd) VALUES('{name}','{pwd}')")
        self.db.commit()
        print("Insert Done")

    def update(self, id, name, pwd):
        res = self.cur.execute(f"UPDATE kb SET name='{name}' , pwd='{pwd}' where id='{id}'")
        self.db.commit()
        print(res)

    def delete(self, id):
        res = self.cur.execute(f"DELETE FROM kb where id='{id}'")
        self.db.commit()
        print(res)

    def show(self, *args):
        if (len(args) < 1):
            self.cur.execute("Select * from kb ")
            data = self.cur.fetchall()
            for i in data:
                print(f"Id : {i[0]} , Name : {i[1]} , Password : {i[2]}")


obj = DBHelper()
while True:
    n = int(input(
        "\n1 for Insertion \n2 for updation \n3 for deletion \n4 for viewing data \n5 for exit \nEnter Your Choice : "))
    if n == 1:
        nm = input("Enter Name : ")
        pwd = input("Enter Password : ")
        obj.insert(nm, pwd)
    elif n == 2:
        id = int(input("Enter Id : "))
        nm = input("Enter Name : ")
        pwd = input("Enter Password : ")
        choice = input("Do You Really Want To Update `Y` For YES `N` For NO : ")
        if choice == 'Y':
            obj.update(id, nm, pwd)
        else:
            print("You Have Canceled the Transaction!!!")
    elif n == 3:
        id = int(input("Enter Id : "))
        choice = input("Do You Really Want To Delete `Y` For YES `N` For NO : ")
        if choice == 'Y':
            obj.delete(id)
        else:
            print("You Have Canceled the Transaction!!!")
    elif n == 4:
        obj.show()
    elif n == 5:
        break
    else:
        print("Enter Valid Choice !_! ")