import math
import random
import time


def salesman(city_map):
    n = len(city_map)

    # Optimized Nearest Neighbor Heuristic
    def optimized_nearest_neighbor():
        def nn_from_city(start_city):
            visited = set([start_city])
            path = [start_city]
            total_cost = 0
            current_city = start_city

            while len(visited) < n:
                min_distance = math.inf
                next_city = None

                for city in range(n):
                    if city not in visited and city_map[current_city][city] < min_distance:
                        min_distance = city_map[current_city][city]
                        next_city = city

                if next_city is not None:
                    path.append(next_city)
                    visited.add(next_city)
                    total_cost += min_distance
                    current_city = next_city

            total_cost += city_map[current_city][start_city]
            return total_cost, path

        best_cost = math.inf
        best_path = []

        for start_city in range(n):
            cost, path = nn_from_city(start_city)
            if cost < best_cost:
                best_cost = cost
                best_path = path

        return best_cost, best_path

    best_cost, best_path = optimized_nearest_neighbor()

    # Initialize solution
    solution_json = {"path": best_path, "cost": best_cost}

    # Branch and Bound Algorithm
    def b_and_b(cur_path, cur_cost):
        cur_city = cur_path[-1]
        if len(cur_path) == n:
            if cur_cost + city_map[cur_city][0] < solution_json["cost"]:
                solution_json['path'] = cur_path + [0]
                solution_json['cost'] = cur_cost + city_map[cur_city][0]
            return

        for city in range(n):
            if city not in cur_path:
                predicted_cost = cur_cost + city_map[cur_city][city]
                if predicted_cost < solution_json['cost']:
                    b_and_b(cur_path + [city], predicted_cost)

    b_and_b([0], 0)

    return solution_json["path"]


# Example usage
city_map = [[0, 2, 9, 10],
            [1, 0, 6, 4],
            [15, 7, 0, 8],
            [6, 3, 12, 0]]

solution = salesman(city_map)
#print(f"Path: {solution['path']}, Cost: {solution['cost']}")


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

