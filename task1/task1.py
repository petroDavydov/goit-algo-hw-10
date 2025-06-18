import pulp
from colorama import Fore, Style, init
init(autoreset=True)


# Ініціалізація моделі для вирішення задачі виробництва напоїв
model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Визначення змінних для напоїв
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Функція цілі для максимізації вироблених напоїв
model += lemonade + fruit_juice, "Total_Products"


# Додавання обмежень до моделі виробництва
model += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"  # Обмеження на воду
model += 1 * lemonade + 2 * fruit_juice <= 50, "Sugar_Constraint"  # Обмеження на цукор
model += 1 * lemonade <= 30, "Lemon_Juice"   # Обмеження на лимонний сік
model += 2 * fruit_juice <= 40, "Fruit_Puree"  # Обмеження на фруктове пюре

# Розв'язання моделі
model.solve()

# use hint for check

lemonade_value = pulp.value(lemonade) if pulp.value(
    lemonade) is not None else 0
fruit_juice_value = pulp.value(fruit_juice) if pulp.value(
    fruit_juice) is not None else 0


# Вивід результатів у консолі
print(
    f"{Fore.LIGHTBLUE_EX}Status: {pulp.LpStatus[model.status]}{Style.RESET_ALL}")
print(f"{Fore.LIGHTGREEN_EX}Lemonade_produced: {pulp.value(lemonade_value)}{Style.RESET_ALL}")
print(f"{Fore.LIGHTYELLOW_EX}Fruit Juice produced: {pulp.value(fruit_juice_value)}{Style.BRIGHT}")
print(f"{Fore.LIGHTRED_EX}Total Profit: {pulp.value(model.objective)}{Style.BRIGHT}")
