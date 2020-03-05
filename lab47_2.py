def disconnected_users(net, users, source, crushes):

    if source in crushes:
        return sum(users.values())
    
    safe = [source]
    print(safe) # ['A']

    while True:
        n1 = len(set(safe))
        print(n1) # 1

        for a,b in net: 
            if a in safe and b not in crushes:
                safe.append(b)
                print(b)
            elif b in safe and a not in crushes:
                safe.append(a)
                print(a)
        print(safe) # ['A', 'B']
        n2 = len(set(safe)) # 2
        print(n2)

        if n1==n2:
            break
    print(sum(users.values()) - sum([users[i] for i in set(safe)]))
    return sum(users.values()) - sum([users[i] for i in set(safe)])


if __name__ == '__main__':
    #assert disconnected_users([['A', 'B'],['B', 'C'],['C', 'D']], {'A': 10,'B': 20,'C': 30,'D': 40},'A', ['C']) # == 70
    #assert disconnected_users([['A', 'B'],['B', 'D'],['A', 'C'],['C', 'D']], {'A': 10,'B': 0,'C': 0,'D': 40},'A', ['B']) #== 0
    #assert disconnected_users([['A', 'B'],['A', 'C'],['A', 'D'],['A', 'E'],['A', 'F']], {'A': 10,'B': 10,'C': 10,'D': 10,'E': 10,'F': 10 },'C', ['A']) #== 50
    assert disconnected_users([['A', 'B'],['B', 'C'],['C', 'D'],['A', 'E'],['A', 'F']], {'A': 10,'B': 10,'C': 10,'D': 10,'E': 10,'F': 10 },'C', ['B'])
