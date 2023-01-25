import psycopg2
import random
import string

conn = psycopg2.connect(
    host="localhost",
    database="Empresa",
    user="postgres",
    password="2995"
)
cursor = conn.cursor()

for i in range(10000):
    cpf = ''.join(random.choices(string.digits, k=11))
    dnr = random.randint(1, 50)
    salario = round(random.uniform(1000, 500000), 2)
    cursor.execute(f"INSERT INTO funcionario (cpf, dnr, salario) VALUES ('{cpf}', {dnr}, {salario})")

for i in range(50):
    dnumero = i + 1
    cpf_ger = ''.join(random.choices(string.digits, k=11))
    cursor.execute(f"INSERT INTO departamento (dnumero, cpf_ger) VALUES ({dnumero}, '{cpf_ger}')")

for i in range(2000):
    projnumero = i + 1
    projlocal = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    dnum = random.randint(1, 50)
    cursor.execute(f"INSERT INTO projeto (projenumero, projlocal, dnum) VALUES ({projnumero}, '{projlocal}', {dnum})")

conn.commit()
conn.close()