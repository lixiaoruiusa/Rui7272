array = [1, 10, 20, 0, 59, 63, 0, 88, 0]

def move_zero(array):

    if not array:
        return

    yingxie = len(array) - 1

    for i in reversed(range(len(array) - 1)):
        if array[i] != 0:
            array[yingxie] = array[i]
            yingxie -= 1

    for i in range(yingxie + 1):
        array[i] = 0

    return array

print(move_zero(array))