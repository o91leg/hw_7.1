import os

from pprint import pprint

def cook_book_read():
  cook_book = dict()
  with open('recipes.txt') as f:
    for line in f:
      dish_name = line.strip()
      count = int(f.readline())
      ing_list = list()
      for item in range(count):
        ingrs = {}
        ingr = f.readline().strip()
        ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
        ingrs['quantity'] = int(ingrs['quantity'])
        ing_list.append(ingrs)
      f.readline()
      cook_book[dish_name] = ing_list
    return cook_book

cook_book = cook_book_read()

def get_shop_list_by_dishes(dishes, person_count):
  ingr_dict = {}
  for dish_name in dishes:
    if dish_name in cook_book:
      for ings in cook_book[dish_name]:
        ingr_quantity = {}
        if ings['ingredient_name'] not in ingr_dict:
          ingr_quantity['measure'] = ings['measure']
          ingr_quantity['quantity'] = ings['quantity'] * person_count
          ingr_dict[ings['ingredient_name']] = ingr_quantity
        else:
          ingr_dict[ings['ingredient_name']]['quantity'] += ings['quantity'] * person_count
    else:
      print('Такого блюда нет!')
  return ingr_dict

pprint(get_shop_list_by_dishes(['Фахитос','Омлет'], 2))
