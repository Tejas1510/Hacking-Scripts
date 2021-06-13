#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int randomnumber(int n)
{
    srand(time(NULL));
    return rand() % n;
}

int winner(char p1, char p2)
{ // it returns the status of player 1

    //equal charcater
    if (p1 == p2)
    {
        return -1;
    }
    // rock-scissors mode
    else if ((p1 == 'r') && (p2 == 's'))
    {
        return 1;
    }
    else if ((p1 == 's') && (p2 == 'r'))
    {
        return 0;
    }
    // rock-paper mode

    else if ((p1 == 'r') && (p2 == 'p'))
    {
        return 0;
    }
    else if ((p1 == 'p') && (p2 == 'r'))
    {
        return 1;
    }
    // paper-scissors mode

    else if ((p1 == 'p') && (p2 == 's'))
    {
        return 0;
    }
    else if ((p1 == 's') && (p2 == 'p'))
    {
        return 1;
    }
    else
    {
        return 404;
    }
}

int main()
{
    char name[50];
    int Player_score = 0, Computer_score = 0, temp;
    char player_char, comp_char;
    char dict[] = {'r', 'p', 's'};
    printf("Write your name please\n");
    scanf("%s", name);

    printf("\nWelcome %s to Rock-Paper-Scissor Game !!  \n \n", name);
    for (int i = 0; i < 3; i++)
    {
        // for Player - user (you)
        printf("\n%s's Turn !! \n", name);
        printf("Choose :- \n 1 for Rock(r) \n 2 for Paper(p)\n 3 for Scissors(s) \n");
        scanf("%d", &temp);
        getchar();
        player_char = dict[temp - 1];
        printf("%s Choose : %c \n ", name, player_char);

        // for Computer
        printf("\nComputer's Turn !! \n");
        printf("Computer is choosing one of them :-\n 1 for Rock(r) \n 2 for Paper(p)\n 3 for Scissors(s) \n");
        temp = randomnumber(3) + 1;
        comp_char = dict[temp - 1];
        printf("\nComputer Choose : %c \n ", comp_char);

        // comparing Score
        if (winner(comp_char, player_char) == 1)
        {
            Computer_score += 1;
            printf("\nWooow , Computer wins this  chance  !! \n ");
        }
        else if (winner(comp_char, player_char) == -1)
        {
            Computer_score += 1;
            Player_score += 1;
            printf("\nOoopss  ,  This  chance  is draw !! \n ");
        }
        else if (winner(comp_char, player_char) == 0)
        {
            Player_score += 1;
            printf("\nGreat  , %s wins this  chance  !! \n ", name);
        }
        else
        {
            printf("Invalid Choice !! by %s \n Play Again \n Thank you !!", name);
            exit(0);
        }

        printf("\nSCORE:-\n %s Got %d Points \n Computer Got %d Points \n ", name, Player_score, Computer_score);
    }
    if (Player_score > Computer_score)
    {
        printf("\nCongrats !! , %s had won this Game !! \n Better Luck Next Time Computer ", name);
    }
    else if (Player_score < Computer_score)
    {
        printf("\nWell Done !! , Computer had won this Game !! \n  Better Luck Next Time %s", name);
    }
    else
    {
        printf("\nAhhh!! , Game is Draw \n");
    }
    printf("\n\nThanks for playing Game!! ");
    return 0;
}