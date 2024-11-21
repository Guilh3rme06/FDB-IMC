import sqlite3

# Conexão com a base de dados 'IMC.db'
conn = sqlite3.connect('IMC.db')

# Criação de um cursor para executar comandos SQL
cursor = conn.cursor()

cursor.execute('''
 CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY,
   name TEXT,
   age INTEGER,
   height FLOAT,
   weight INTEGER
   )
''')

conn.commit()

def create_user(name, age, height, weight):
    try:
        cursor.execute('INSERT INTO users (name, age, height, weight) VALUES (?,?,?,?)',
                       (name, int(age), float(height), int(weight)))
        conn.commit()
        print("User criado com sucesso")
    except Exception as e:
        print(f"ERRO AO CRIAR USER: {e}")

def calcular_imc(name):
    try:
        cursor.execute('SELECT name, height, weight FROM users WHERE name = ?', (name,))
        result = cursor.fetchone()
        if result:
            user_name, height, weight = result
            imc = weight / height ** 2
            print(f"O IMC do {user_name} é {imc:.2f}")
        else:
            print("Utilizador não encontrado")
    except Exception as e:
        print(f"ERRO AO CALCULAR IMC: {e}")

def find_user_by_name(name):
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    result = cursor.fetchone()
    if result:
        return result
    return None