#include <cs50.h>
#include <stdio.h>

int main (void)
{
    //Prompting the user for a starting # of llamas
    int start;
    do
    {
        start = get_int ("Start size= ");
    }
    while (start < 9);

    // Prompting the user for an end # of llamas
    int end;
    do
    {
        end = get_int ("End size: ");
     }
     while(end < start);

     //How many years will it take to get to the goal?
     int years = 0;
     {
     start += start / 12;
     years ++;
     }
}
