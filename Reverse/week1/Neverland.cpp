#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define UINT32 unsigned int

UINT32 enc[40] = {786380, 3221225348, 50331715, 221, 89, 97, 12582791, 805306421, 49049, 3145778, 54, 4294967241, 4294967192, 48, 4294967199, 4294967244, 4294967240, 98, 4294967193, 48, 4294967240, 4294967194, 4294967237, 4294967198, 50, 4294967236, 4294967240, 96, 61, 53, 61, 4294967243, 52, 60, 4294967199, 101, 101, 51, 102, 121};
UINT32 idx[40] = {9, 15, 12, 3, 2, 16, 11, 14, 7, 10, 46, 45, 43, 46, 47, 45, 47, 40, 49, 58, 49, 51, 51, 43, 50, 55, 55, 56, 60, 48, 4294967246,4294967187,4294967256,4294967282,4294967263,4294967152,4294967154,4294967248,4294967206,4294967194};

UINT32 func(UINT32 num)
{
    if(num == 0)
        return 7;
    if(num == 1)
        return 8;
    return 3*func(num-1) + 4*func(num-2);
}

int main()
{
    printf("Here is your flag.\n");
    for(int i = 0; i < 40; ++i)
    {
        // int c = func(idx[i]) ^ enc[i];
        printf("%c",char(func(idx[i]) ^ enc[i]));
    }
    return 0;
}

// 0xGame{1e625d4c04fe44f9b684d919708caa7b}
// 786380, 3221225348, 50331715, 221, 89, 97, 12582791, 805306421, 49049, 3145778, 54, 4294967241, 4294967192, 48, 4294967199, 4294967244, 4294967240, 98, 4294967193, 48, 4294967240, 4294967194, 4294967237, 4294967198, 50, 4294967236, 4294967240, 96, 61, 53, 61, 4294967243, 52, 60, 4294967199, 101, 101, 51, 102, 121