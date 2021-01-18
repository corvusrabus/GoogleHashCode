# allocation : list of allocation of pizzas
# allocation[0] is a list of pizzas allocated to the 2teams
# allocation[1] is a list of pizzas allocated to the 3teams
# allocation[2] is a list of pizzas allocated to the 4teams

def write_allocation_to_file(allocation, filename) :
    D =  len(allocation[0]) / 2 + len(allocation[1]) / 3 + len(allocation[2]) / 4
    file = open(filename, "w")
    file.write(str(int(D)))
    file.write("\n")
    file.write("2")
    for pizza in allocation[0] :
        file.write(" " + str(pizza))
    file.write("\n")
    
    file.write("3")
    for pizza in allocation[1] :
        file.write(" " + str(pizza))
    file.write("\n")

    file.write("4")
    for pizza in allocation[2] :
        file.write(" " + str(pizza))
    file.write("\n")

    file.close()


        