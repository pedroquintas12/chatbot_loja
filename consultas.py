from conexao import conectar

def buscar_produto(nome):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM produtos WHERE nome LIKE %s"
    cursor.execute(query, (f"%{nome}%",))
    resultado = cursor.fetchall()
    conn.close()
    return resultado