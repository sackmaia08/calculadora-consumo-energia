
print("=== Calculadora de Consumo Elétrico ===")

# Entrada de dados
aparelho = input("Nome do aparelho: ")
potencia = float(input("Potência (em watts - W): "))
horas_dia = float(input("Horas de uso por dia: "))

# Cálculo do consumo mensal (kWh)
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo de custo (opcional)
valor_kwh = 0.75
custo = consumo_mensal * valor_kwh

# Saída
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f}")