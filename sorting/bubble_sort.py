def bubble_sort(input, key=None):
    swapping = True
    end = len(input)

    while swapping:
        swapping = False
        for i in range(1, end):
            if key == None:
                if input[i-1] > input[i]:
                    input[i-1], input[i] = input[i], input[i-1]
                    swapping = True
            else:
                if key(input[i-1]) > key(input[i]):
                    input[i-1], input[i] = input[i], input[i-1]
                    swapping = True
        end -= 1

    return input