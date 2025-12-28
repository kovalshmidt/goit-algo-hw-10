
import pulp

problem = pulp.LpProblem("Maximize_Beverages", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("FruitJuice", lowBound=0, cat='Integer')

problem += lemonade + fruit_juice, "Total_Products"

problem += 2*lemonade + 1*fruit_juice <= 100, "Water"
problem += 1*lemonade <= 50, "Sugar"
problem += 1*lemonade <= 30, "LemonJuice"
problem += 2*fruit_juice <= 40, "FruitPuree"

problem.solve()

print("Status:", pulp.LpStatus[problem.status])
print("Lemonade to produce:", int(lemonade.varValue))
print("Fruit juice to produce:", int(fruit_juice.varValue))
print("Total products:", int(lemonade.varValue + fruit_juice.varValue))
