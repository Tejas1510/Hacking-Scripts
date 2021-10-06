/**********************************
Programming a Minesweeper Game

Name: Aneesh Panchal
Github: Aneeshcoder
Language: C programming language
**********************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//FLUSH to clear the input stream
#define FLUSH fflush(stdin)

//Defining functions
void difficulty( void );
void beginner( void );
void intermediate( void );
void expert( void );
void minefield_generator( void );
void print_minefield( void );
void guess( void );
void boom( void );
void print_final_minefield( void );
void win( void );
void play_again( void );
void game_over( void );

//Global variables
int x, y;
int M, N;
float diff;
int total_mines = 0;
int mines = 0;
int minefield[30][30];                                   
int blank_minefield[30][30];                              
int final_minefield[30][30];

int main()
{
    printf("\t\tWelcome to Minesweeper\n");
    difficulty();
    return 0;
}

//Choose difficulty
void difficulty( void )                                 
{
    diff = 0;
        printf("\t\tChoose a difficulty level(1-3)");
        scanf("%f", &diff);
        FLUSH;

    if( diff == 1 )                                        
    {
        beginner();
    }
    else if( diff == 2 )
    {
        intermediate();
    }
    else if( diff == 3 )
    {
        expert();
    }

}

//At beginner level 9X9 grid with 10 Mines
void beginner( void )                                      
{
    M = 9;
    N = 9;
    total_mines = 10;
    minefield_generator();
    guess();
}

//At intermediate level 16X16 grid with 40 Mines
void intermediate( void )                                  
{
    M = 16;
    N = 16;
    total_mines = 40;
    minefield_generator();
    guess();
}

//At advanced or expert level 16X30 grid with 99 Mines
void expert( void )                                        
{
    M = 16;
    N = 30;
    total_mines = 99;
    minefield_generator();
    guess();
}

//Minefield generator for specific difficulty
void minefield_generator( void )                          
{
    int i = 0, j = 0;

    srand( time( NULL ) );                              

    while( j < N )                                         
    {
        while( i < M)
        {
            minefield[i][j] = '-';
            blank_minefield[i][j] = minefield[i][j];
            final_minefield[i][j] = minefield[i][j];
            i++;
        }
        i = 0;
        j++;
    }
    mines = 0;
    while( mines < total_mines )                            
    {
        i = rand()%(M);
        j = rand()%(N);
        if( minefield[i][j] != '*')                       
        {
            minefield[i][j] = '*';
            final_minefield[i][j] = minefield[i][j];
            mines++;
        }
    }
    i = 0;
    j = 0;

    while( j < N )                                          
    {
        while( i < M)
        {
            if( minefield[i][j] != '*')
            {
                minefield[i][j] = 0;
            }
            if((minefield[i-1][j-1] == '*') && (minefield[i][j] != '*'))
            {
                minefield[i][j]++;
            }
            if((minefield[i-1][j] == '*') && (minefield[i][j] != '*'))
            {
                minefield[i][j]++;
            }
            if((minefield[i][j-1] == '*') && (minefield[i][j] != '*'))
            {
                minefield[i][j]++;
            }
            if((minefield[i-1][j+1] == '*') && (minefield[i][j] != '*'))
            {
                minefield[i][j]++;
            }
            if((minefield[i+1][j-1] == '*') && (minefield[i][j] != '*'))
            {
                minefield[i][j]++;
            }
            if((minefield[i+1][j] == '*') && (minefield[i][j] != '*'))
            {
                minefield[i][j]++;
            }
            if((minefield[i][j+1] == '*') && (minefield[i][j] != '*'))
            {
                minefield[i][j]++;
            }
            if((minefield[i+1][j+1] == '*') && (minefield[i][j] != '*'))
            {
                minefield[i][j]++;
            }
            i++;
        }
        i = 0;
        j++;
    }
    i = 0;
    j = 0;
}

//Printing updated Minefields
void print_minefield(void)                               
{
    int i = 0, j = 0, z = 0;
    while( z < M )                                         
    {
        if( z == 0 )
        {
            printf("\t");
        }
        printf("|%d|\t", z);
        z++;
    }
    printf("\n\n");

    while( j < N )                                          
    {
        printf("|%d|\t", j);
        while( i < M)
        {
            if( blank_minefield[i][j] == '-')
            {
                printf("|%c|\t", blank_minefield[i][j]);

            }
            else if( minefield[i][j] == 0 )                
            {
                blank_minefield[i][j] = 'B';
                printf("|%c|\t", blank_minefield[i][j]);
            }
            else
            {
                printf("|%d|\t", blank_minefield[i][j]);

            }
            i++;
        }
        printf("\n");
        i = 0;
        j++;
    }
}

//Guessing function to check whether you hit mine or not
void guess( void )
{
    int q = 0, i=0, j=0, match=0;
    print_minefield();
    while( j < N )                                          
    {
        while( i < M )
        {
            if(minefield[i][j] == blank_minefield[i][j])
            {
                match++;
            }
            i++;
        }
        i = 0;
        j++;
    }
    if( match == (( M * N ) - total_mines))                 
    {
        win();
    }
    printf("\nEnter the x value, then a space, then the y value:");
    scanf("%d %d", &x, &y);                                 
    FLUSH;
    if( (x >= M) || (x < 0) || (y < 0) || (y >= N) )
    {
        printf("\nPlease enter a value inside the grid\n");
        guess();
    }
    if( minefield[x][y] == '*' )                            
    {
        boom();
    }
    if( blank_minefield[x][y] != '-' )
    {
        printf("\nPlease enter a value that has not already been entered\n");
        guess();
    }

    else                                              
    {
        blank_minefield[x][y] = minefield[x][y];
        if( minefield[x][y] == 0 )
        {
            if( minefield[x-1][y-1] == 0 )
            {
                blank_minefield[x-1][y] = minefield[x-1][y];
            }
            if( minefield[x-1][y] == 0 )
            {
                blank_minefield[x-1][y] = minefield[x-1][y];
            }
            if( minefield[x][y-1] == 0 )
            {
                blank_minefield[x][y-1] = minefield[x][y-1];
            }
            if( minefield[x-1][y+1] == 0 )
            {
                blank_minefield[x-1][y+1] = minefield[x-1][y+1];
            }
            if( minefield[x+1][y-1] == 0 )
            {
                blank_minefield[x+1][y-1] = minefield[x+1][y-1];
            }
            if( minefield[x+1][y] == 0 )
            {
                blank_minefield[x+1][y] = minefield[x+1][y];
            }
            if( minefield[x][y+1] == 0 )
            {
                blank_minefield[x][y+1] = minefield[x][y+1];
            }
            if( minefield[x+1][y+1] == 0 )
            {
                blank_minefield[x+1][y+1] = minefield[x+1][y+1];
            }
        }
        guess();
    }
}

//Hitting Mine and game lost
void boom( void )                                       
{
    print_final_minefield();
    printf("\n\t\tYou hit a mine at %d,%d\n\t\tYOU LOSE!!!!", x, y);
    play_again();
}

//Printing Final Minefield after Win or Lose
void print_final_minefield( void )                      
{
    int i = 0, j = 0, z = 0;
    while( z < M )
    {
        if( z == 0 )
        {
            printf("\t");
        }
        printf("|%d|\t", z);
        z++;
    }
    printf("\n\n");

    while( j < N )
    {
        printf("|%d|\t", j);
        while( i < M)
        {
            printf("|%c|\t", final_minefield[i][j]);
            i++;
        }
        printf("\n");
        i = 0;
        j++;
    }
}

//Winning the game
void win( void )                                       
{
    printf("\n\n\n\t\t\tYOU WIN!!!!!\n\n\n");
    play_again();
}

//Option to play again
void play_again( void )                                
{
    char option[2];
    printf("\n\t\tWould you like to play again(Y/N)?:");
    scanf("%c", &option[0]);
    FLUSH;
    if((option[0] == 'Y') || (option[0] == 'y'))       
    {
        difficulty();
    }
    else if( (option[0] == 'N') || (option[0] == 'n'))
    {
        game_over();
    }
    else
    {
        printf("Please enter either Y or N");
        play_again();
    }
}

//Game lost/ Game Over
void game_over( void )                                  
{
    printf("\n\n\t\tGame Over");
    exit(1);
}
