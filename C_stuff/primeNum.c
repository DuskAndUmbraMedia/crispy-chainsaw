#include <stdio.h>

int main()
{

int h = 0;
int i, startNum;
int rounds = 0;

printf("To find all prime numbers from zero to a number, enter a number: ");
scanf("%d", &startNum); //Input into startNum

printf("\nPrime numbers: "); //Prints content in final output before the loop.

for (h = 1; h <= startNum; ++h) { // pushes each number into the 2nd loop to be factored
    rounds = 0;
    for (i = 1; i <= h; ++i) { // factors each number into all factors
        if (h % i == 0) { // counts the number of factors for each number
            rounds++;
            }
        }
    if (rounds == 2) // prints numbers that only have two factors (primes)
        printf("%d ", h);
    else
        continue;
    }
printf("\n\n"); //Formatting
}
