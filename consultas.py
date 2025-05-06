from conexao import conectar

def buscar_produto(id):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM produtos WHERE id LIKE %s"
    cursor.execute(query, (f"%{id}%",))
    resultado = cursor.fetchall()
    conn.close()
    return resultado