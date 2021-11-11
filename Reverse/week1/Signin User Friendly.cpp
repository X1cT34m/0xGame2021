#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
    int number,input_number;
    srand(time(NULL));
    number = rand()%1001;
    printf("I write down a number(0-1000) just now.\n");
    printf("Could you guess what I write?\n");
    printf("Your guess:");
    scanf("%d",&input_number);
    if(number == input_number)
        printf("0xGame{we1c0me_2_Rever5e_egin44ring}");
    else
        printf("OHH You are wrong!!!");
    return 0;
}
// 0xGame{we1c0me_2_Rever5e_egin44ring}