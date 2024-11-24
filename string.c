#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string name = get_string ("what is your name? ");
    int length = strlen(name);

    for ( int i = 0; i < length; i++)
    {
        printf("%i ", name[i]);
    }
    printf("\n");
}