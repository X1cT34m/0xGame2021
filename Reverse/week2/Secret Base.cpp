#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char table[80] = {"123DfgabcQeEFh4pklmnojqGHIJKLMNOPdRSTUVWXYZrstuvwxyz0ABCi56789+/="};
char enc[80] = {"FbdbHqAUNzoiIDdUIDhSEnF54DHthDT5Hm05HVlREnoAhaF0Hn2dFBQVFC0="};

void encrypt(char *s, char *res)
{
    int length = strlen(s);
    int t = length / 3;
    int i;
    for (i = 0; i < t; ++i)
    {
        res[4 * i] = table[s[3 * i] >> 2];
        res[4 * i + 1] = table[((s[3 * i] & 0b11) << 4) + (s[3 * i + 1] >> 4)];
        res[4 * i + 2] = table[((s[3 * i + 1] & 0b1111) << 2) + ((s[3 * i + 2] & 0b11000000) >> 6)];
        res[4 * i + 3] = table[s[3 * i + 2] & 0b00111111];
    }
    if(length % 3 == 1)
    {
        res[4 * i] = table[s[3 * i] >> 2];
        res[4 * i + 1] = table[(s[3 * i] & 0b11) << 4];
        res[4 * i + 2] = table[64];
        res[4 * i + 3] = table[64];
    }
    if(length % 3 == 2)
    {
        res[4 * i] = table[s[3 * i] >> 2];
        res[4 * i + 1] = table[((s[3 * i] & 0b11) << 4) + (s[3 * i + 1] >> 4)];
        res[4 * i + 2] = table[(s[3 * i + 1] & 0b1111) << 2];
        res[4 * i + 3] = table[64];
    }
}

int main()
{
    char input[80];
    char res[80];
    memset(res,0,80);
    memset(input,0,80);
    printf("Please input your flag:\n");
    scanf("%60s",input);
    if(strlen(input) != 44)
    {
        printf("Wrong length!!!\n");
        exit(0);
    }
    encrypt(input,res);
    for (int i = 0; i < 60; ++i)
    {
        if(res[i] != enc[i])
        {
            printf("Wrong flag!!!\n");
            exit(0);
        }
    }
    printf("Congratulation to you.\nit's a right flag!!!\n");
    return 0;
}
// 0xGame{58d8ed3c-3986-499a-9bdb-554c4a0a3bf3}

// 0xf9, 0x57, 0xd0, 0x57, 0xb5, 0x29, 0xb5, 0xa, 0x54, 0x5d, 0x49, 0x63, 0xe7, 0x95, 0x8d, 0x5a, 0x3b, 0xb4, 0x36, 0x1, 0x17, 0xf3, 0x3, 0xb1, 0x8a, 0x25, 0xce, 0xe0, 0x41, 0x99, 0x66, 0x4b, 0x9,