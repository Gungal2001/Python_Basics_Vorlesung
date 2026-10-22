my_list = ["1", "pollutant", "stoff", "substanz"]
print(my_list[0]) # 0 bedeutet Anfang von list
print(my_list[-1]) # -1 bedeutet Ende von list
my_list[1] = "Banana"
print(my_list)
my_list.append("Orange") # fügt ein neues Element am Ende der Liste hinzu
print(my_list)
my_list.remove("Banana") # entfernt ein Element aus der Liste
print(my_list)

my_tuple = ("1", "pollutant", "stoff",  True) #die Tuple ist unveränderlich
print(my_tuple)


my_dick = {"1": "pollutant", "2": "stoff", "3": "substanz"} #DICTIONARY ist als excel Tabelle
print(my_dick)
print(my_dick["1"]) # gibt den Wert von key 1 aus

my_dick["1"] += ", Schadstoff" # fügt den Wert von key 1 hinzu
print(my_dick)
people = [
    {"name": "Max", "age": 28, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "New Jearsey"}
    ] # LISTE von DICTIONARY
print(people)

people.append({"name": "Alice", 
               "age": 25, 
               "city": "Los Angeles"}) # fügt ein neues Dictionary in die Liste hinzu
print(people)
del people[1] # entfernt das zweite Dictionary aus der Liste
print(people)
del people[0]["city"] # entfernt den Wert von key "age" aus dem ersten Dictionary
print(people)
#Set 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1.add(6) # fügt ein Element zum Set hinzu
print(set1)
set1.remove(3) # entfernt ein Element aus dem Set
print(set1)
print(set1.union(set2)) # gibt die Vereinigung von set1 und set2 aus
print(set1.intersection(set2)) # gibt die Schnittmenge von set1 und set2 aus
print(set1.difference(set2)) # gibt die Differenz von set1 und set2 aus






set3 = {1, 2, 3, 3, 5}
print(set3) # gibt {1, 2, 3, 5} aus, da Duplikate entfernt werden







#Docstring

