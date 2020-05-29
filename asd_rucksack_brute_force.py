from itertools import combinations

items = (
   ('светр', 3, 50), 
   ('футболка', 0.1, 60),
   ('ліхтарик', 0.2, 70),
   ('книга', 1, 20),
   ('дощовик', 0.5, 50),
   ('карта', 0.3, 50),
   ('компас', 0.4, 40),
   ('консерви', 0.7, 70), 
   ('печиво', 2.8, 20),
   ('вода', 2.2, 25),
   ('термос', 0.25, 45),
)

total_volume = 0
for item in items:
   total_volume += item[1]


VOLUME = 6


def calcRucksackVol(rucksack):
   total_volume = 0
   for item in rucksack:
       total_volume += item[1]

   return total_volume


def calcRucksackCost(rucksack):
   total_cost = 0
   for item in rucksack:
       total_cost += item[2]

   return total_cost


print("у розпорядженні {} предметів загальним обсягом {} л,які необхідно покласти в рюкзак {} літрів".\
     format(len(items), total_volume, VOLUME))


counter = 0
max_cost = 0
result_items = []
result_costs = []

for num in range(1, len(items) + 1):
   for i, combination in enumerate(combinations(items, num), 1):
       current_volume = calcRucksackVol(combination)
       current_cost = calcRucksackCost(combination)
       if current_volume <= VOLUME and current_cost >= max_cost:
           counter += 1
           max_cost = current_cost
           result_items.append(combination)
           result_costs.append(current_cost)
           print("комбінація {} набрала ціну {} и об'єм {:3.2f} л: {}".\
                 format(counter, current_cost, current_volume, combination))

max_cost_count = result_costs.count(max_cost)

print("вдалося {} раз досягти максимальної цінности {}".\
     format(max_cost_count, max_cost))


best_result = result_items[result_costs.index(max_cost)]

print(calcRucksackVol(best_result))

[print(item) for item in best_result]