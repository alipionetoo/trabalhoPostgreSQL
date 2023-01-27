import psycopg2
import random
import string

def insert_data(cursor, table, columns, values):
    cursor.execute(f"INSERT INTO {table} ({', '.join(columns)}) VALUES {values}")

conn = psycopg2.connect(
    host="localhost",
    database="empresa",
    user="postgres",
    password="2995"
)
cursor = conn.cursor()

for i in range(10000):
    cpf = ''.join(random.choices(string.digits, k=11))
    dnr = random.randint(1, 50)
    salario = round(random.uniform(1000, 500000), 2)
    insert_data(cursor, 'funcionario', ['cpf', 'dnr', 'salario'], f"('{cpf}', {dnr}, {salario})")

for i in range(50):
    dnumero = i + 1
    cpf_ger = ''.join(random.choices(string.digits, k=11))
    insert_data(cursor, 'departamento', ['dnumero', 'cpf_ger'], f"({dnumero}, '{cpf_ger}')")

for i in range(2000):
    projnumero = i + 1
    projlocal = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    dnum = random.randint(1, 50)
    insert_data(cursor, 'projeto', ['projenumero', 'projlocal', 'dnum'], f"({projnumero}, '{projlocal}', {dnum})")

conn.commit()
conn.close()
