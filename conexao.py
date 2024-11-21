import sqlite3
# Conexão com a base de dados 'escola.db'
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
        cursor.execute('INSERT INTO users (name, age,height,weight) VALUES (?,?,?,?)',
                       (name, int(age), float(height), int(weight)))
        conn.commit()
        print("User criado com sucesso")
    except:
        print("ERRO AO CRIAR USER")

def calcular_imc(name):
    try:
        cursor.execute('SELECT name,height,weight FROM users WHERE name = ? ', (name,))
        result = cursor.fetchone()
        if result:
            height, weight = result
            imc = weight / height ** 2
            print(f"O IMC do {name} é {imc:.2f}")
        else:
            print("ERRO AO CALCULAR IMC")
    except:
        print("ERRO AO CALCULAR IMC")