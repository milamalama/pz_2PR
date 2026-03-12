import logging
logging.basicConfig(
    filename="log_file.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filemode="w"
)

costs = [
    [6, 12, 20, 24],
    [9, 7, 9, 28],
    [23, 18, 15, 19],
    [27, 24, 21, 15],
]

alpha = 0.4  #коэффициент пессимизма для Гурвица

#критерий Вальда (минимакс затрат)
#находим макс затрату для каждой стратегии
max_costs = [max(row) for row in costs]
logging.info(f"maximum cost: {max_costs}")

#выбираем стратегию с наименьшим из максимумов
Vald_number = min(range(len(max_costs)), key=lambda i: max_costs[i])
logging.info(f"Vald strategy: {Vald_number + 1}")

#критерий Сэвиджа (минимакс рисков)
#сначала находим минимальную затрату в каждом столбце
num_rows = len(costs)
num_cols = len(costs[0])
min_in_columns = []
for j in range(num_cols):
    column_values = [costs[i][j] for i in range(num_rows)]
    min_in_columns.append(min(column_values))

logging.info(f"minimum values by columns: {min_in_columns}")

#строим матрицу рисков (риск = текущая затрата - минимальная в столбце)
risks = []
for i in range(num_rows):
    risk_row = []
    for j in range(num_cols):
        risk_row.append(costs[i][j] - min_in_columns[j])
    risks.append(risk_row)


#находим макс риск для каждой стратегии
max_risks = [max(row) for row in risks]
Savag_number = min(range(len(max_risks)), key=lambda i: max_risks[i])
logging.info(f"Savag strategy: {Savag_number + 1}")

#критерий Гурвица
#оценка= alpha * max + (1 - alpha) * min
Gurvic_values = []
for row in costs:
    score = alpha * max(row) + (1 - alpha) * min(row)
    Gurvic_values.append(score)

logging.info(f"Gurvic score: {Gurvic_values}")

Gurvic_number= min(range(len(Gurvic_values)), key=lambda i: Gurvic_values[i])
logging.info(f"Gurvic strategy: {Gurvic_number + 1}")

print("матрица рисков:")
for row in risks:
    print(row)

print(f"критерий Вальда:  {Vald_number + 1}")
print(f"критерий Сэвиджа:  {Savag_number + 1}")
print(f"критерий Гурвица: {Gurvic_number + 1}")
