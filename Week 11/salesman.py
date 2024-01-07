import math
import time
import random

def salesman(city_map):

    n = len(city_map)

    def greedy_estimate_2(city_map):
        n = len(city_map)
        visited = set([0])
        path = [0]

        current_city = 0
        total_cost = 0

        while len(visited) < n:
            min_distance = math.inf
            min_city = None

            for next_city, distance in enumerate(city_map[current_city]):
                if next_city not in visited and 0 < distance < min_distance:
                    min_distance = distance
                    min_city = next_city

            if min_city is not None:
                total_cost += min_distance
                path.append(min_city)
                visited.add(min_city)
                current_city = min_city

        total_cost += city_map[current_city][0]
        return total_cost

    def greedy_estimate(city_map, cur_path, c):
        n = len(city_map)
        if len(cur_path) == n:
            return c + city_map[cur_path[-1]][0]

        min_cost = math.inf
        min_city = None
        cur_city = cur_path[-1]

        for city in range(n):
            if city not in cur_path and city_map[cur_city][city] < min_cost:
                min_cost = city_map[cur_city][city]
                min_city = city

        if min_city is None:
            return c + city_map[cur_path[-1]][0]
        else:
            return greedy_estimate(city_map, cur_path + [min_city], c + min_cost)


    estimate = greedy_estimate_2(city_map)


    solution_json = {"path" : [], "cost" : estimate} #If the greedy estimate is correct the algorithm will otherwise fail

    def b_and_b(cur_path, cur_cost):
        cur_city = cur_path[-1]
        if len(cur_path) == n:
            if cur_cost + city_map[cur_city][0] < solution_json["cost"]:
                #cur_path.append(0)
                solution_json['path'] = cur_path + [0]
                solution_json['cost'] = cur_cost + city_map[cur_city][0]
            return

        for city in range(n):
            if city not in cur_path:
                predicted_cost = cur_cost + city_map[cur_city][city]
                if predicted_cost < solution_json['cost']:
                    #cur_path.append(city)
                    b_and_b(cur_path + [city], predicted_cost)
                #else:
                #    print("No " + str(cur_path))

    b_and_b([0], 0)

    return solution_json["path"]



if __name__ == "__main__":

    cost = 0

    city_map = [
        #     0   1   2   3   4
        [0, 12, 19, 16, 29],  # 0
        [12, 0, 27, 25, 5],  # 1
        [19, 27, 0, 8, 4],  # 2
        [16, 25, 8, 0, 14],  # 3
        [29, 5, 4, 14, 0]  # 4
    ]


    def generate_large_city_map(num_cities, max_distance=100):
        city_map = [[0 if i == j else random.randint(1, max_distance) for j in range(num_cities)] for i in
                    range(num_cities)]
        return city_map


    num_cities = 15
    city_map = generate_large_city_map(num_cities)

    start_time = time.time()
    path = salesman(city_map)
    end_time = time.time()
    print("Time " + str(end_time - start_time))



    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i + 1]]

    print(path)  # [0, 1, 4, 2, 3, 0]
    print(cost)  # 45