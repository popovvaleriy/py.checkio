def bigger_price(limit, data):
    price = 0
    for i in range(len(data)): 
        for j in range(i, len(data)):
            if data[j]["price"] > data[i]["price"]:
                box = data[i]
                data[i] = data[j]
                data[j] = box
    #print(data)
    ans = []
    for i in range(limit):
        ans.append(data[i])
    print(ans)
    return ans


if __name__ == '__main__':
    from pprint import pprint

    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"
