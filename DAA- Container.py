def container_loading(weights, capacity):
    weights.sort()

    total = 0
    count = 0
    selected = []

    for weight in weights:
        if total + weight <= capacity:
            total += weight
            count += 1
            selected.append(weight)

    print("Selected containers:", selected)
    print("Number of containers:", count)
    print("Total weight:", total)


weights = [10, 20, 30, 40, 50]
capacity = 70

container_loading(weights, capacity)
