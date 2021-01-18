from scoring import score
path = 'data/a_example'

def parse_first_line(file):
    first_line = file.readline()
    M, T2, T3, T4 = first_line.split( )
    M, T2, T3, T4 = int(M), int(T2), int(T3), int(T4)
    return M, T2, T3, T4



if __name__ == '__main__':
    with open(path) as file:
        M, T2, T3, T4 = parse_first_line(file)
        ingredients = set()
        pizzas = []
        lines = file.readlines()
        for line in lines[1:]:
            cur_ingredients = line.split()[1:]
            ingredients.update(cur_ingredients)
            pizzas.append(cur_ingredients) # TODO why are we doing this?
    
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
    del ingredients

    # # test scoring function
    # allocation = [[1,4], [0,2,3], []]
    # result = score(allocation,pizzas,T2,T3, T4)

    
