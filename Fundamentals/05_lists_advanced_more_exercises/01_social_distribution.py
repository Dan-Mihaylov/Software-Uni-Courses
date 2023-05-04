def distribute(pop_list, minimum):
    if sum(pop_list) < minimum * len(pop_list):
        return "No equal distribution possible"
    else:
        wealthiest = pop_list.index(max(pop_list))
        for i in range(len(pop_list)):
            if pop_list[i] < minimum:
                pop_list[wealthiest] -= minimum - pop_list[i]
                pop_list[i] = minimum
                wealthiest = pop_list.index(max(pop_list))
        return pop_list


population = [int(x) for x in input().split(", ")]
min_wealth = int(input())
print(distribute(population, min_wealth))


# if sum(population) < min_wealth * len(population):
#     print(f"No equal distribution possible")
# else:
#     wealthiest = population.index(max(population))
#     new_pop = list(filter(lambda x: x < min_wealth))
#     for i in range(len(population)):
#         if population[i] < min_wealth:
#             population[wealthiest] -= min_wealth - population[i]
#             population[i] = min_wealth
#             wealthiest = population.index(max(population))
#     print(population)
