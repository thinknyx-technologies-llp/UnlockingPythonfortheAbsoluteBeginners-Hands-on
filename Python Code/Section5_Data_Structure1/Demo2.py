fruits_colors = [["Apple","Red"],["Banana","Yellow"],["Grape","Purple"]]
print("Fruits and their colors.")
for fruit in fruits_colors:
    fruit_name = fruit[0]
    fruit_color = fruit[1]
    print(f"The color of {fruit_name} is {fruit_color}.")

first_fruit_name = fruits_colors[0][0]
second_fruit_color = fruits_colors[1][1]
print("\n Specific Elements: ")
print("First fruit name: ", first_fruit_name)
print("Second fruit color: ", second_fruit_color)

print("\n Updating an element: ")
fruits_colors[0][1] = "Crimson Red"
print("Updated fruits and their colors.")
for fruit in fruits_colors:
    fruit_name = fruit[0]
    fruit_color = fruit[1]
    print(f"The color of {fruit_name} is {fruit_color}.")