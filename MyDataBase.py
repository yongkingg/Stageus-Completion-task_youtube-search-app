import sqlite3
class MyDataBase:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.result = None
        self.initDataBase()
        
    def initDataBase(self):
        self.conn = sqlite3.connect("Login_Module.db")
        self.cur = self.conn.cursor()

        # self.cur.execute("CREATE TABLE saveIDPW (Id TEXT , Pw TEXT);")
        # self.cur.execute("CREATE TABLE userInterFace (Id Text, Name TEXT,  Age INTEGER, Phonenumber INTEGER, TEAM TEXT, GRADE INTEGER);")
        # self.cur.execute("CREATE TABLE playList (PlayListName TEXT);")
        # self.cur.execute("CREATE TABLE video (PlayListName TEXT, Video TEXT);")
        # self.cur.execute("DROP TABLE saveIDPW;")
        # self.cur.execute("DROP TABLE userInterFace;")
        # self.cur.execute("DROP TABLE playList;")
        # self.cur.execute("DROP TABLE video;")

    #     self.make()

    # def make(self):
    #     self.cur.execute("INSERT INTO playList VALUES('dydwns8064');")
    #     self.conn.commit()

    def create(self, table, column, data):    
        self.sql = "INSERT INTO " + table + "(" 
        for index in range(0, len(column)):
            self.sql += column[index]
            if index < len(column)-1:
                self.sql += ", "
        self.sql += ")"
        self.sql += " VALUES("
        for index in range(0, len(column)):
            self.sql += "'" + data[index] + "'"
            if index < len(column)-1:
                self.sql += ", "
        self.sql += ");"
        self.cur.execute(self.sql)
        self.conn.commit()

    def read(self,table,column,data):
        self.sql = "SELECT * FROM " + table + " WHERE ("
        if len(column) == 1:
            for index in range(0,len(column)):
                self.sql += column[index]
                if index < len(column) -1:
                    self.sql += ", "
            self.sql += " = " + "'"
            for index in range(0,len(column)):
                self.sql += data[index]
                if index < len(column) - 1:
                    self.sql += "', '"
            self.sql += "');"
        else:
            for index in range(0,len(column)):
                self.sql += column[index] + "="
                self.sql += "'" + data[index]+"'"
                if index < len(column) -1:
                    self.sql += " and "
            self.sql += ");"
        self.cur.execute(self.sql)
        self.result = self.cur.fetchall()
        return self.result

    def update(self,table,originalColumn,setColumn,originalData,setData):
        self.sql = "UPDATE " + table + " SET " + "("
        for index in range(0,len(setColumn)):
            self.sql += setColumn[index]
            if index < len(setColumn)-1:
                self.sql += ", "
            self.sql += ")" + " = " + "('"
        for index in range(0,len(setData)):
            self.sql += setData[index]
            if index < len(setData)-1:
                self.sql += ", "
            self.sql += "')"
            self.sql += " WHERE " + "("
        for index in range(0,len(originalColumn)):
            self.sql += originalColumn[len(originalColumn)-index-1]
            if index < len(originalColumn)-1:
                self.sql += ", "
        self.sql += ")" + "=" + "('"
        for index in range(0,len(originalData)):
            self.sql += originalData[index]
            if index < len(originalData)-1:
                self.sql += ", "
            self.sql += "');"
        self.cur.execute(self.sql)
        self.conn.commit()

