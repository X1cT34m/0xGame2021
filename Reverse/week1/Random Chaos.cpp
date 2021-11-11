#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// unsigned char enc1[41] = {"0xGame{d6ca93397ecb4d4e83792a7100737932}"};
unsigned char enc[41] = {0x22, 0xca, 0x7, 0x19, 0xf8, 0xfb, 0x28, 0x9d, 0x1e, 0x80, 0xac, 0xc9, 0x60, 0x46, 0x18, 0x21, 0xdf, 0x95, 0xd5, 0x70, 0xc5, 0x19, 0xea, 0xb0, 0x9c, 0x83, 0x11, 0x4a, 0x93, 0xc7, 0x91, 0xf6, 0x14, 0x71, 0x2f, 0x22, 0x14, 0xbf, 0x58, 0x76}; 

int main()
{
    char input[41];
    srand(0x2021);
    printf("input:");
    scanf("%40s",input);
    if(strlen(input) != 40)
    {
        printf("Wrong!!!\n");
        exit(0);
    }
    for (int i = 0; i < 40; ++i)
    {
        if((input[i] ^ (rand() & 0xff)) != enc[i])
        {
            printf("Wrong!!!\n");
            exit(0);
        }
    }
    printf("Rigth!!!\n");
    printf("What you input is flag!!!");
    return 0;
}