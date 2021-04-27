# O(n) Time | O(n) Space
def arrayOfProducts(array):
    products = [1] * len(array)
    left_products = [1] * len(array)
    right_products = [1] * len(array)

    leftrunning = 1
    for i in range(len(array)):
        left_products[i] = leftrunning
    leftrunning = leftrunning * array[i]

    rightrunning = 1
    for i in reversed(range(len(array))):
        right_products[i] = rightrunning
        rightrunning = rightrunning * array[i]

    for i in range(len(array)):
        products[i] = left_products[i] * right_products[i]

    return products




