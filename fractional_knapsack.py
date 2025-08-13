def fractional_knapsack(cargo):
    # cargo[0]: weight, cargo[1]: value
    capacity = 15

    # cargo.sort(), cargo = sorted(cargo, )의 차이
    cargo = sorted(cargo, key=lambda x: (x[1] / x[0]), reverse=True)
    total_value = 0

    # cargo[0]과 cargo[1]이 무엇을 의미하는지 풀어서 가독성 향상
    for weight, value in cargo:
        if capacity - weight >= 0:   
            capacity -= weight
            total_value += value
        else:
            fraction = capacity / weight
            total_value += value * fraction
            break
    return total_value
