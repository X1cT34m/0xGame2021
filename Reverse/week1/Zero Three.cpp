#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define BYTE unsigned char
#define UINT32 unsigned int
#define UINT64 unsigned long long
#define INT64 long long

__int64 n1;
__int64 n2;
__int64 n3;
__int64 n4;
__int64 n5;

int main()
{
    INT64 num[8];
    UINT32 *p_num;
    BYTE *p;
    printf("Please input your flag:\n");
    scanf("%s",&n5);
    p = (BYTE *)(&n5);
    p_num = (UINT32 *)p;
    for (int i = 0; i <8; ++i)
    {
        num[i] = (INT64)(*(p_num + i));
        // printf("%llx\n",num[i]);
    }
    if(strlen((char *)p) != 32)
    {
        printf("Wrong!!!");
        exit(0);
    }
    if( 0x2021 - p[0] * 1 - p[3] * 9 - p[4] * 1 + p[5] * 2 - p[9] * 1 + p[10] * 1 - p[11] * 6 - p[13] * 1 - p[14] * 3 - p[15] * 5 != 0x160b ||
        0x2021 - p[0] * 6 - p[1] * 1 - p[2] * 3 - p[5] * 2 + p[8] * 3 + p[10] * 8 - p[11] * 8 + p[12] * 4 + p[14] * 3 - p[15] * 6 != 0x19dc ||
        0x2021 - p[0] * 2 - p[1] * 3 - p[2] * 1 - p[3] * 5 - p[4] * 7 - p[5] * 6 - p[6] * 7 - p[8] * 2 - p[12] * 5 + p[13] * 6 != 0x15a2 ||
        0x2021 - p[0] * 2 + p[1] * 2 - p[3] * 2 + p[4] * 3 + p[5] * 2 - p[8] * 2 - p[10] * 1 - p[12] * 1 - p[14] * 2 - p[15] * 2 != 0x1e0d ||
        0x2021 - p[1] * 2 - p[2] * 2 - p[3] * 9 + p[4] * 2 - p[7] * 5 + p[8] * 2 - p[9] * 9 - p[10] * 4 - p[14] * 6 - p[15] * 6 != 0x127f ||
        0x2021 + p[0] * 5 - p[2] * 1 + p[5] * 1 - p[6] * 5 + p[9] * 8 - p[10] * 7 - p[11] * 8 - p[12] * 1 + p[14] * 9 - p[15] * 9 != 0x1b94 ||
        0x2021 - p[0] * 3 - p[1] * 4 - p[2] * 3 - p[4] * 4 - p[6] * 1 - p[7] * 5 + p[10] * 9 + p[13] * 1 - p[14] * 2 - p[15] * 6 != 0x16e8 ||
        0x2021 - p[0] * 6 + p[1] * 9 - p[3] * 5 - p[7] * 4 - p[10] * 3 - p[11] * 2 - p[12] * 2 + p[13] * 1 - p[14] * 9 + p[15] * 9 != 0x1ce1 ||
        0x2021 + p[2] * 9 - p[4] * 1 + p[5] * 3 - p[6] * 3 - p[7] * 7 - p[8] * 5 + p[9] * 6 + p[10] * 7 - p[13] * 2 - p[14] * 1 != 0x20fa ||
        0x2021 - p[1] * 8 - p[2] * 7 - p[3] * 1 + p[4] * 6 + p[6] * 8 - p[7] * 1 + p[8] * 5 - p[10] * 4 - p[14] * 1 + p[15] * 7 != 0x20b8)
    {
        printf("Wrong!!!");
        exit(0);
    }
    else if(0  - num[0] * 0x7e58 - num[5] * 0x9686 + num[1] * 0x55e0 - num[4] * 0x592b != -0x598cb22e1383 ||
            0  + num[0] * 0x3c2d - num[5] * 0x20f4 - num[4] * 0x91cc - num[2] * 0x9547 != -0x77bfbf8de4b6 ||
            0  - num[5] * 0x292a - num[3] * 0x870c - num[1] * 0x710e + num[7] * 0x2aae != -0x6edc040c4340 ||
            0  + num[7] * 0x86be - num[5] * 0x4ff7 - num[2] * 0x59ce - num[6] * 0x75a5 != -0x33ec462bb644 ||
            0  + num[2] * 0x7ad5 + num[1] * 0x862c - num[4] * 0x4b87 - num[5] * 0x8158 != 0x333ca3587682 ||
            0  - num[4] * 0x674f - num[2] * 0x4d66 + num[0] * 0x39a6 - num[5] * 0x34fe != -0x49c3f52450ef ||
            0  - num[0] * 0x832a + num[7] * 0x4fef - num[1] * 0x3dc9 + num[5] * 0x652a != -0x1a3fa2e8fedc ||
            0  - num[3] * 0x3a68 - num[6] * 0x7081 + num[2] * 0x8ef2 - num[7] * 0x8a65 != -0x2946caf39b69
    )
    {
        printf("Wrong!!!");
        exit(0);
    }
    printf("Congradution!!!\n");
    printf("flag is 0xGame{what you input}");
    return 0;
}


// udydYCBxUB6vqsAt5VCs6LKDRqXLUhSW