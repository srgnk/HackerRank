if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
    
    lowest = min([el[1] for el in students])
    second_low = min(list(filter(lambda a: a > lowest, [el[1] for el in students])))
    
    out = [el[0] for el in students if (el[1] == second_low)]
    out.sort()
    
    print("\n".join(out))
