import mysql.connector

def conectar():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="loja_tecnologia",
        charset="latin1"  

    )
    return conn

if __name__ == "__main__":
    try:
        conn = conectar()
        print("Conexão bem-sucedida!")
        conn.close()
    except Exception as e:
        print("Erro na conexão:", e)
