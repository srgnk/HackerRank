def get_avg(marks, student):
    return (sum(marks[student])/len(marks[student]))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format(get_avg(student_marks, query_name)))
