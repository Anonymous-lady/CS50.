#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get name of a persom
    string answer = get_string("What's your name? ");
    printf("Hello,%s\n", answer);
}
