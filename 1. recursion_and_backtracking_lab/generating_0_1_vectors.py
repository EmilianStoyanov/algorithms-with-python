def gen01(idx, vector):
    if idx >= len(vector):
        print("".join([str(x) for x in vector]))
        return

    for number in range(0, 2):
        vector[idx] = number
        gen01(idx + 1, vector)


# def gen01(idx, vector):
# if idx >= len(vector):
#     print(*vector, sep='')
#     return
# for num in range(2):
#     vector[idx] = num
#     gen01(idx + 1, vector)


# 3
n = int(input())
vector = [0] * n

gen01(0, vector)

"""  

000
001
010
011
100
101
110
111


"""
