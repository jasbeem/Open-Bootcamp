import sqlite3


def main():
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

    cursor.execute("INSERT INTO Alumnos VALUES(1,'Luis', 'Sanchez')")
    cursor.execute("INSERT INTO Alumnos VALUES(2,'Juanjo', 'Perez')")
    cursor.execute("INSERT INTO Alumnos VALUES(3,'Luis', 'Rodrigues')")
    cursor.execute("INSERT INTO Alumnos VALUES(4,'Lucia', 'Villanueva')")
    cursor.execute("INSERT INTO Alumnos VALUES(5,'Almudena', 'Gracia')")
    cursor.execute("INSERT INTO Alumnos VALUES(6,'Carla', 'Gonzalez')")
    cursor.execute("INSERT INTO Alumnos VALUES(7,'Laura', 'Martinez')")
    cursor.execute("INSERT INTO Alumnos VALUES(8,'Raul', 'Torres')")

    conn.commit()

    cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Luis'")
    filas = cursor.fetchall()
    cursor.close()

    print(list(filas))

    conn.close()

if (__name__=="__main__"):
    main()