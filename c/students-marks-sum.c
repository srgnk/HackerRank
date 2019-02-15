int marks_summation(int *marks, int number_of_students, char gender) {
    int result = 0;
    
    for (int i = gender == 'b' ? 0 : 1; i < number_of_students; i += 2)
        result += marks[i];
    
    return result;
}