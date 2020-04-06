class Dish():
     cook_book = {}
     def __init__(self):
         with  open("recipes.txt",encoding="utf8") as dish_file:
             for text in dish_file:
                 if not text.strip():
                     break
                 else:
                     dish_name = text.strip().lower()
                     self.cook_book[dish_name] = []
                     ingr_count = int(dish_file.readline().strip())
                     while ingr_count:
                         ingr_info = dish_file.readline().split('|')
                         self.cook_book[dish_name].append({"ingradient_name": ingr_info[0], "quantity" : float(ingr_info[1]), "measure" : ingr_info[2]})
                         ingr_count -= 1
                     dish_file.readline()     

     def get_shop_list_by_dishes(self, dishes, person_count = 0):
             list_dishes = {}
             dishes = [x.lower() for x in dishes]
             if not person_count:
                 person_count = int(input("Введите количестко персон "))
             if dishes:
                      for user_dish in dishes:
                         if self.cook_book.get(user_dish.lower()):
                             for dish_name in self.cook_book[user_dish]:
                                     if dish_name["ingradient_name"] in list_dishes:
                                         list_dishes[dish_name["ingradient_name"]]["quantity"] += dish_name["quantity"] * person_count
                                     else:
                                         list_dishes[dish_name["ingradient_name"]] = {"measure": dish_name["measure"], "quantity":dish_name["quantity"] * person_count}  
                         else:
                             print(f"нет такого блюда {user_dish}")
                  
             return self.show_dict(list_dishes)
        
     def show_dict(self,some_dict = {}):
                for key,item in some_dict.items():
                     print(f"{key}   {str(item)}")
         


Dish().get_shop_list_by_dishes(["омлет","Утка по-пекински"], 3)


#print(Dish().get_shop_list_by_dishes([ "Запеченный картофь",'Омлет'], 0))