def flatten(l):
    unbox = []
    if isinstance(l, list) or isinstance(l, tuple) or isinstance(l, set):
        return sum(map(flatten, l), unbox)
    else:
        return [l]

def flatten_w_d(l):
    unbox = []
    if isinstance(l, list) or isinstance(l, tuple) or isinstance(l, set) or isinstance(l, dict):
        return sum(map(flatten_w_d, l), unbox)
    else:
        return [l]

def sum_data(data):
    num = 0
    lit = 0
    for i in range(len(data)):
        if type(data[i]) == int:
            num = num + data[i]
        else:
            lit = lit + len(data[i])
    return num + lit

def dict_unbox(my_dict1):
    un_dict_v = []
    for i in range(len(my_dict1)):
        if isinstance(my_dict1[i], dict):
            un_dict_v.append(my_dict1[i])
    un_dict_over = []
    for i in range(len(un_dict_v)):
        un_dict_over.append(sum(un_dict_v[i].values()))
    a = sum(un_dict_over)
    return a

def calculate_structure_sum(data_sructure):
    result1 = flatten_w_d(data_structure)
    result2 = (sum_data(result1))
    result3 = flatten(data_structure)
    result4 = dict_unbox(result3)
    result = result2 + result4
    print(result)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

calculate_structure_sum(data_structure)