#include "stdio.h"   
#include "memory.h"   
#include "time.h"   
#include "stdlib.h"   

#define PLAIN_FILE_OPEN_ERROR -1   
#define KEY_FILE_OPEN_ERROR -2   
#define CIPHER_FILE_OPEN_ERROR -3   
#define OK 1 

typedef char ElemType; 

 //????????IP   
int IP_Table[64] = {  57,49,41,33,25,17,9,1,   
                                 59,51,43,35,27,19,11,3,   
                                 61,53,45,37,29,21,13,5,   
                                 63,55,47,39,31,23,15,7,   
                                 56,48,40,32,24,16,8,0,   
                                 58,50,42,34,26,18,10,2,   
                                 60,52,44,36,28,20,12,4,   
                                 62,54,46,38,30,22,14,6};    
//?????????IP^-1   
int IP_1_Table[64] = {39,7,47,15,55,23,63,31,   
           38,6,46,14,54,22,62,30,   
           37,5,45,13,53,21,61,29,   
           36,4,44,12,52,20,60,28,   
           35,3,43,11,51,19,59,27,   
           34,2,42,10,50,18,58,26,   
           33,1,41,9,49,17,57,25,   
           32,0,40,8,48,16,56,24};   
  
//?????????E   
int E_Table[48] = {31, 0, 1, 2, 3, 4,   
                  3,  4, 5, 6, 7, 8,   
                  7,  8,9,10,11,12,   
                  11,12,13,14,15,16,   
                  15,16,17,18,19,20,   
                  19,20,21,22,23,24,   
                  23,24,25,26,27,28,   
                  27,28,29,30,31, 0};   
  
//???????P   
int P_Table[32] = {15,6,19,20,28,11,27,16,   
                  0,14,22,25,4,17,30,9,   
                  1,7,23,13,31,26,2,8,   
                  18,12,29,5,21,10,3,24};   
  
//S??   
int S[8][4][16] =//S1   
            {{{14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7},   
              {0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8},   
                {4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0},   
                {15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13}},   
                //S2   
              {{15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10},   
              {3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5},   
              {0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15},   
              {13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9}},   
              //S3   
              {{10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8},   
              {13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1},   
                {13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7},   
              {1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12}},   
              //S4   
              {{7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15},   
              {13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9},   
              {10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4},   
              {3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14}},   
              //S5   
              {{2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9},   
              {14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6},   
              {4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14},   
              {11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3}},   
              //S6   
              {{12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11},   
              {10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8},   
              {9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6},   
              {4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13}},   
              //S7   
              {{4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1},   
              {13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6},   
              {1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2},   
              {6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12}},   
              //S8   
              {{13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7},   
              {1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2},   
              {7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8},   
              {2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11}}};   
//??????1   
int PC_1[56] = {56,48,40,32,24,16,8,   
              0,57,49,41,33,25,17,   
              9,1,58,50,42,34,26,   
              18,10,2,59,51,43,35,   
              62,54,46,38,30,22,14,   
              6,61,53,45,37,29,21,   
              13,5,60,52,44,36,28,   
              20,12,4,27,19,11,3};   
  
//??????2   
int PC_2[48] = {13,16,10,23,0,4,2,27,   
              14,5,20,9,22,18,11,3,   
              25,7,15,6,26,19,12,1,   
              40,51,30,36,46,54,29,39,   
              50,44,32,47,43,48,38,55,   
              33,52,45,41,49,35,28,31};   
  
//????????????1?7?1?7   
int MOVE_TIMES[16] = {1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1};
// int DES_Print(ElemType data[64], int time, int k);

int Char8_to_Bit64(ElemType ch[8], ElemType bit[64])
{
    for(int i = 0; i < 8; ++i)
    {
        for(int j = 0; j < 8; ++j)
        {
            bit[i * 8 + j] = (ch[i] >> (7 - j)) & 1;
        }
    }
    return 0;
}

int DES_ROL(ElemType data[56], int time)
{
    ElemType temp[56];
    memcpy(temp, data, time);
    memcpy(temp + time, data + 28, time);
    memcpy(data, data + time, 28 - time);
    memcpy(data + 28 - time, temp, time);
    memcpy(data + 28, data + 28 + time, 28 - time);
    memcpy(data + 56 - time, temp + time, time);
    return 0;

}

int DES_MakeSubKeys(ElemType key[64],ElemType sub_keys[16][48])
{
    ElemType temp[56];
    // DES_Print(key, 0, 64);
    //???????????
    for(int i = 0; i < 56; ++i)
    {
        temp[i] = key[PC_1[i]];
    }
    // DES_Print(temp, 0, 56);
    
    for(int i = 0; i < 16; ++i)
    {
        DES_ROL(temp, MOVE_TIMES[i]);
        for (int j = 0; j < 48; ++j)
        {
            sub_keys[i][j] = temp[PC_2[j]];
        }
    }
    for(int i = 0; i < 16; ++i)
    {
        // DES_Print(sub_keys[i], i + 1, 48);
    }
    return 0;
}

int DES_IP_Transform(ElemType data[64])
{
    ElemType temp[64];
    for(int i = 0; i < 64; ++i)
    {
        temp[i] = data[IP_Table[i]];
    }
    memcpy(data, temp ,64);
    return 0;
}

int DES_E_Transform(ElemType data[48])
{
    ElemType temp[48];
    for (int i = 0; i < 48; ++i)
    {
        temp[i] = data[E_Table[i]];
    }
    memcpy(data, temp, 48);
    return 0;
}

int DES_XOR(ElemType data[48], ElemType key[48], int count)
{
    for (int i = 0; i < count; ++i)
    {
        data[i] ^= key[i];
    }
    return 0;
}

int DES_SBOX(ElemType data[48])
{
    int line,row,output;
    int cur_1,cur_2;
    for (int i = 0; i < 8; ++i)
    {
        cur_1 = i * 6;
        cur_2 = i * 4;
        line = (data[cur_1] << 1) + (data[cur_1 + 5]);
        row = (data[cur_1 + 1] << 3) + (data[cur_1 + 2] << 2) + (data[cur_1 + 3] << 1) + data[cur_1 + 4];
        output = S[i][line][row];
        data[cur_2] = (output & 0x8) >> 3;
        data[cur_2 + 1] = (output & 0x4) >> 2;
        data[cur_2 + 2] = (output & 0x2) >> 1;
        data[cur_2 + 3] = output & 0x1;
    }
    return 0;
}

int DES_P_Transform(ElemType data[32])
{
    ElemType temp[32];
    for (int i = 0; i < 32; ++i)
    {
        temp[i] = data[P_Table[i]];
    }
    memcpy(data, temp ,32);
    return 0;
}

int DES_Swap(ElemType data_1[32], ElemType data_2[32])
{
    ElemType temp[32];
    memcpy(temp, data_1, 32);
    memcpy(data_1, data_2, 32);
    memcpy(data_2, temp, 32);
    return 0;
}

int DES_IP_1_Transform(ElemType data[64])
{
    ElemType temp[64];
    for (int i = 0; i < 64; ++i)
    {
        temp[i] = data[IP_1_Table[i]];
    }
    memcpy(data, temp ,64);
    return 0;
}

int Bit64_to_Char8(ElemType bit[64], ElemType chr[8])
{
    memset(chr, 0, 8);
    for (int i = 0; i < 8; ++ i)
    {
        for (int j = 0; j < 8; ++j)
        {
            int cnt = 8 * i + j;
            chr[i] |= (bit[cnt] << (7 - j));
        }
    }
    return 0;
}

// int DES_Print(ElemType data[64], int time, int k)
// {
//     printf("%10d: \n",time);
//     for(int i = 0; i < k; i+=4)
//     {
//         char c;
//         int temp = (data[i] << 3) + (data[i + 1] << 2) + (data[i + 2] << 1) + data[i +3];
//         if(temp >= 10)
//         {
//             c = temp + 55;
//         }
//         else
//         {
//             c = temp + 48;
//         }
//         printf("%c ",c);
//     }
//     printf("\n");
//     return 0;
// }

int DES_Encrypt_Block(ElemType plain_block[8], ElemType sub_keys[16][48],ElemType cipher_block[8])
{
    ElemType plain_bits[64];
    ElemType copy_right[64];

    Char8_to_Bit64(plain_block, plain_bits);
    DES_IP_Transform(plain_bits);
    // DES_Print(plain_bits, 9999, 64);
    for (int i = 0; i < 16; ++i)
    {
        // DES_Print(plain_bits, 9999, 64);
        memcpy(copy_right, plain_bits + 32, 32);
        DES_E_Transform(copy_right);
        DES_XOR(copy_right, sub_keys[i], 48);
        DES_SBOX(copy_right);
        DES_P_Transform(copy_right);
        DES_XOR(plain_bits, copy_right, 32);
        // DES_Print(copy_right, 9999, 32);
        // memcpy(plain_bits + 32, copy_right, 32);
        // DES_Print(plain_bits, i + 1, 64);
        if(i != 15)
        {
            DES_Swap(plain_bits, plain_bits + 32);
        }
    }
    // DES_Print(plain_bits, 888, 64);
    DES_IP_1_Transform(plain_bits);
    // DES_Print(plain_bits, 999, 64);
    Bit64_to_Char8(plain_bits,cipher_block);
    return 0;
}

int DES_Encrypt(char * plain_file, char * key_str, char *cipher_file)
{
    FILE *plain, *cipher;
    int count;
    ElemType plain_block[8],cipher_block[8],key_block[8];
    ElemType bkey[64];
    ElemType sub_keys[16][48];
    plain = fopen(plain_file, "rb");
    cipher = fopen(cipher_file, "wb");
    if(plain == NULL)
        return PLAIN_FILE_OPEN_ERROR;
    if(cipher == NULL)
        return CIPHER_FILE_OPEN_ERROR;
    //???????
    memcpy(key_block, key_str, 8);
    //???????????????
    Char8_to_Bit64(key_block,bkey);
    DES_MakeSubKeys(bkey, sub_keys);
    while(!feof(plain))
    {
        count = fread(plain_block, sizeof(char), 8, plain);
        if(count == 8)
        {
            DES_Encrypt_Block(plain_block, sub_keys, cipher_block);
            fwrite(cipher_block, sizeof(char), 8, cipher);
        }
    }
    if(count)
    {
        memset(plain_block + count, '\0', 8 - count);
        // plain_block[7] = 8- count;
        DES_Encrypt_Block(plain_block, sub_keys, cipher_block);
        fwrite(cipher_block,sizeof(char),8,cipher);
    }
    fclose(plain);
    fclose(cipher);
    return 0;
}

int main()
{
    printf("保存密码 plain.txt 文件似乎丢失了.\n");
    printf("你能根据被加密后的 cipher.txt 文件还原出原本的 plain.txt 密码文件吗 ?\n");
    printf(" flag 的形式为 0xGame{md5(plain.txt)}, md5 中字符均为小写.");
    char plain[64] = {"plain.txt"};
    char cipher[64] = {"cipher.txt"};
    DES_Encrypt(plain, "0xgame21", cipher);
    getchar();
    getchar();
    return 0;
}

//0xGame{83b9879f334340ef42dbb9f40468fc84}