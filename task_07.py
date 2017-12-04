from math import inf

data = [{"result": 27, "items": [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10]], "size": 5, "weight": 10},
        {"result": 46, "items": [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10], [6, 4], [5, 3], [7, 3]],
         "size": 10, "weight": 20}]


def knapsack(items, weight):
    opts = [{0:0}]
    for item in items:
        opts.append(opts[-1].copy())
        for o in opts[-2]:
            if o+item[1] <= weight:
                if o+item[1] not in opts[-1].keys() or opts[-1][o+item[1]]< opts[-2][o]+item[0]:
                    opts[-1][o+item[1]] = opts[-2][o]+item[0]

    max_w = max(opts[-1], key=opts[-1].get)
    total_value = opts[-1][max_w]
    result_values = []
    print(opts)
    for i in reversed(range(len(items))):
        if max_w-items[i][1] in opts[i].keys() and opts[i][max_w-items[i][1]] + items[i][0] == opts[i+1][max_w]:
            result_values.append(i)
            max_w -= items[i][1]
    return total_value, result_values
print(knapsack(data[1]["items"], data[1]["weight"]))

