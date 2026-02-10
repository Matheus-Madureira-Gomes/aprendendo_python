import copy

d1 = {
    "c1": "1",
    "c2": 2,
    list: [0,1,2]
}


d2 = copy.deepcopy(d1)

d2[list][1] = 999

print(d1, d2)