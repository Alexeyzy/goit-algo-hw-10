import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  
x2 = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer') 

model += x1 + x2, "Total_Production"

model += 2 * x1 + 1 * x2 <= 100, "Water"
model += 1 * x1 <= 50, "Sugar"
model += 1 * x1 <= 30, "Lemonad"
model += 2 * x2 <= 40, "Fruit"

model.solve()

print(f"Оптимальна кількість виробленого Лимонаду: {x1.varValue}")
print(f"Оптимальна кількість виробленого Фруктового соку: {x2.varValue}")
print(f"Максимальна загальна кількість продуктів: {pulp.value(model.objective)}")
