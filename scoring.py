# The function how many points we get for the current configuration
# allocation : list of allocation of pizzas
# allocation[0] is a list of pizzas allocated to the 2teams
# allocation[1] is a list of pizzas allocated to the 3teams
# allocation[2] is a list of pizzas allocated to the 4teams
# Ti number of i-teams
def score(allocation, pizzas, T2, T3, T4) :
    if len(allocation[0]) % 2 != 0 :
        return 0
    if len(allocation[1]) % 3 != 0 :
        return 0
    if len(allocation[2]) % 4 != 0 :
        return 0
    if len(allocation[0]) / 2 > T2 :
        return 0
    if len(allocation[1]) / 3 > T3 :
        return 0
    if len(allocation[2]) / 4 > T4 :
        return 0
    result = 0
    for team in range(3) :  
        i = 0
        while i < len(allocation[team]) :
            ingreds = set()
            for j in range(team + 2) :
                ingreds.update(pizzas[allocation[team][i + j]])
            result += len(ingreds) ** 2
            i += team + 2
        
    return result
