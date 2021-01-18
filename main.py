path = 'data/a_example'

def parse_first_line(file):
    first_line = file.readline()
    M, T2, T3, T4 = first_line.split( )
    return M, T2, T3, T4

 

if __name__ == '__main__':
    first_line = list(map(int,input().split()))
    T4 = first_line.pop()
    T3 = first_line.pop()
    T2 = first_line.pop()
    M = first_line.pop()

    ingredients = set()
    pizzas = []
    for i in range(M) :
        cur_ingredients = input().split()
        cur_ingredients.pop(0)
        for x in cur_ingredients :
            ingredients.add(x)
        pizzas.append(cur_ingredients)
    
    ingredient_to_number = {}
    number_to_ingredient = {}

    counter = 0
    for ingredient in ingredients :
        number_to_ingredient[counter] = ingredient
        ingredient_to_number[ingredient] = counter
        counter += 1
    
    for i in range(len(pizzas)) :
        pizzas[i] = list(map(lambda x : ingredient_to_number[x], pizzas[i]))
    del ingredient_to_number

    
