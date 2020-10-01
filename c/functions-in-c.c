#include <stdio.h>  //headerFile
int max_of_four(int , int , int , int); //function declaration

int max_of_four(int a, int b, int c, int d) //function definition
{
    //body of function
    int res = a;

    if (b > res)
        res = b;
    if (c > res)
        res = c;
    if (d > res)
        res = d;

    return res;
}

//main function
int main() {
    int num_1, num_2, num_3, num_4;
    printf("Enter FOUR numbers : ");
    scanf("%d %d %d %d", &num_1, &num_2, &num_3, &num_4);
    int answer = max_of_four(num_1, num_2, num_3, num_4);
    printf("\nLargest Number is : %d", answer);
    return 0;
}
