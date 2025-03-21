import sqlite3
import pandas as pd
from IPython.display import display

# Criar conexão SQLite em memória
conn = sqlite3.connect(":memory:")

# Criando DataFrame de membros da academia
members_df = pd.DataFrame({
    "id": [1, 2, 3],  
    "name": ["Lucas Silva", "Ana Souza", "Rafael Costa"],
    "member_birth_date": ["1995-06-15", "1988-09-23", "2000-03-12"]
})

# Criando DataFrame de funcionários
employees_df = pd.DataFrame({
    "id": [1, 2, 3],  # ID do funcionário
    "name": ["Marcos Lima", "Fernanda Alves", "Ricardo Mendes"],
    "employee_position": ["Instrutor", "Recepcionista", "Gerente"]
})

# Criando DataFrame de planos de assinatura
membership_plans_df = pd.DataFrame({
    "id": [1, 2, 3],
    "plan_name": ["Básico", "Premium", "VIP"],
    "plan_price": [49.90, 79.90, 119.90]
})

# Criando DataFrame de equipamentos da academia
gym_equipment_df = pd.DataFrame({
    "id": [1, 2, 3],
    "equipment_name": ["Esteira", "Supino", "Bicicleta Ergométrica"],
    "equipment_description": ["Equipamento para corrida e caminhada", "Aparelho para treino de peitoral", "Simula uma bicicleta para exercícios"]
})

# Salvando os DataFrames no banco SQLite
members_df.to_sql("member", conn, index=False, if_exists="replace")
employees_df.to_sql("employee", conn, index=False, if_exists="replace")
membership_plans_df.to_sql("membershipPlan", conn, index=False, if_exists="replace")
gym_equipment_df.to_sql("gymEquipment", conn, index=False, if_exists="replace")

# Exibir todas as tabelas carregadas
print("Tabela: member")
display(pd.read_sql("SELECT * FROM member", conn))
print("Tabela: employee")
display(pd.read_sql("SELECT * FROM employee", conn))
print("Tabela: membershipPlan")
display(pd.read_sql("SELECT * FROM membershipPlan", conn))
print("Tabela: gymEquipment")
display(pd.read_sql("SELECT * FROM gymEquipment", conn))

# Executar INNER JOIN entre membros e planos de assinatura
query_inner = """
SELECT member.id, member.name, membershipPlan.plan_name, membershipPlan.plan_price
FROM member
INNER JOIN membershipPlan ON member.id = membershipPlan.id
"""
inner_join_df = pd.read_sql(query_inner, conn)
print("INNER JOIN:")
display(inner_join_df)

# Executar LEFT JOIN entre funcionários e equipamentos
query_left = """
SELECT employee.id, employee.name, employee.employee_position, gymEquipment.equipment_name
FROM employee
LEFT JOIN gymEquipment ON employee.id = gymEquipment.id
"""
left_join_df = pd.read_sql(query_left, conn)
print("\nLEFT JOIN:")
display(left_join_df)

# Fechar conexão
conn.close()