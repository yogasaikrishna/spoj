#include<stdio.h>
#include<vector>
#include<cmath>

int no_of_squares(int);

using namespace std;

int main()
{
    vector<int> input_array;
    int n;
   
    scanf("%d", &n);
    while (n != 0)
    {
        input_array.push_back(n);
        scanf("%d", &n);
    }
    
    for (int i = 0; i < input_array.size(); i++)
    {
        printf("%d\n", no_of_squares(input_array[i]));
    }
    
    return 0;    
}

int no_of_squares(int num)
{
    int count = 0;
    for (int i = 1; i <= num; i++)
    {
        count += pow(i, 2); 
    }
    return count;
}
