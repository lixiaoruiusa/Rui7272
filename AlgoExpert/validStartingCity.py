# O(n) time | O(n) space
# 如果0到2 不可以，说明1和2都不可以，因为到1的时候肯定有多余的油，then skip to 3
# 先检查if total gas > total cost

def validStartingCity(distances, fuel, mpg):
    total_fule = sum(fuel) * mpg
    total_cost = sum(distances)

    print(total_fule)
    print(total_cost)

    if total_fule < total_cost:
        return -1

    current_dis = 0
    start = 0

    for i in range(len(distances)):
        current_dis = current_dis - distances[i] + (fuel[i] * mpg)
        if current_dis < 0:
            current_dis = 0
            start = i + 1
    return start