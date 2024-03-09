from pprint import pprint


def get_cookbook(file):
    cookbook = {}
    with open(file, "r", encoding="utf-8") as book:
        lines = book.readlines()
        symbols = " | "
        name = ""
        for i, line in enumerate(lines):
            if symbols not in line and len(line) != 1 and len(line) != 2:
                line = line[:-1]
                ingredients_total = int(lines[i + 1])
                cookbook[line] = []
                name = line
                id_ = 0
                for _ in range(ingredients_total):
                    cookbook[name].append({})
            if symbols in line:
                line = line[:-1]
                ingredients_list = line.split(symbols)
                if id_ < ingredients_total:
                    count = 0
                    if count == 0:
                        cookbook[name][id_]['ingredient_name'] = (ingredients_list[count])
                        count += 1
                    if count == 1:
                        cookbook[name][id_]['quantity'] = (ingredients_list[count])
                        count += 1
                    if count == 2:
                        cookbook[name][id_]['measure'] = (ingredients_list[count])
                else:
                    id_ = 0
                id_ += 1

    return cookbook

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cookbook = get_cookbook('Recipes.txt')
    for u in dishes:
        for i in cookbook[u]:
            if i['ingredient_name'] not in shop_list:
                ingredients_count = int(i['quantity']) * person_count
                shop_list[i['ingredient_name']] = ({'measure':i['measure'], 'quantity':ingredients_count})
            else:
                ingredients_count = int(i['quantity']) * person_count
                shop_list[i['ingredient_name']]['quantity'] += ingredients_count
    return shop_list

pprint(get_cookbook('Recipes.txt'))
pprint(get_shop_list_by_dishes(['Омлет', 'Пицца', 'Блинчики'], 6))
