#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define UINT32 unsigned int

int enc[40] = {145, 119, 251, 14, 183, 204, 228, 56, 17, 148, 253, 133, 92, 145, 132, 92, 125, 103, 39, 308, 309, 10, 216, 35, 13, 48, 101, 62, 19, 69, 84, 82, 81, 62, 176, 217, 19, 51, 195, 255};
int check[40] = {161,15,188,111,218,169,159,94,41,246,197,228,110,242,177,56,27,1,17,256,256,50,233,65,104,2,4,6,42,112,55,107,48,93,130,232,37,87,242,130};
int encrypt(int a,int b)
{
    int t1,t2;
    t1 = a&~b;
    t2 = b&~a;
    return t1 | t2;
}

int main()
{
    char input[41];
    printf("input:");
    scanf("%40s",input);
    if(strlen(input) != 40)
    {
        printf("Wrong!!!\n");
        exit(0);
    }
    for (int i = 0; i < 40; ++i)
    {
        if(encrypt(input[i],check[i]) != enc[i])
        {
            printf("Wrong!!!");
            exit(0);
        }
    }
    printf("Congratulation!!!\n");
    printf("What you input is flag");
    return 0;
}
// 0xGame{f8b8a2c5dff64581be2a895c9ac216d1}
// 145, 119, 251, 14, 183, 204, 228, 56, 17, 148, 253, 133, 92, 145, 132, 92, 125, 103, 39, 308, 309, 10, 216, 35, 13, 48, 101, 62, 19, 69, 84, 82, 81, 62, 176, 217, 19, 51, 195, 255