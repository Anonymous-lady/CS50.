#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt height size
    int h, r, c, s;
    do
    {
        h = get_int ("Enter your preferred height: ");
    }
    while (h < 1 || h > 8);

    //organize bricks in a pyramid
    for ( r = 1; r < h; r++)
    {
        for (s = 0; s < h - r - 1; s++)
        {
            printf(" ");
        }
        for (c = 0; c < r; c++)
        {
            printf("#");
        }
        printf("\n");
    }
}