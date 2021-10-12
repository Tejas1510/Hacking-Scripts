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

//Global variables
int x, y;
int M, N;
float difficulty;
int totalMines = 0;
int mines = 0;
int minefield[30][30];                                   
int blank[30][30];                              
int final[30][30];

//Defining functions
void level();
void beginner();
void intermediate();
void advanced();
void generator();
void print();
void guess();
void boom();
void print_final();
void Win();
void playAgain();
void gameLost();

//Choose difficulty
void level(){
    difficulty=0;
        printf("\t\tChoose a difficulty level(1-3)");
        scanf("%f", &difficulty);
        FLUSH;
    if(difficulty==1){
        beginner();
    }
    else if(difficulty==2){
        intermediate();
    }
    else if(difficulty==3){
        advanced();
    }
}

//At beginner level 9X9 grid with 10 Mines
void beginner(){
    M = 9;
    N = 9;
    totalMines = 10;
    generator();
    guess();
}

//At intermediate level 16X16 grid with 40 Mines
void intermediate(){
    M = 16;
    N = 16;
    totalMines = 40;
    generator();
    guess();
}

//At advanced or expert level 16X30 grid with 99 Mines
void advanced(){
    M = 16;
    N = 30;
    totalMines = 99;
    generator();
    guess();
}

//Minefield generator for specific difficulty
void generator(){
    int i=0,j=0;
    srand(time(NULL));                              
    while(j<N){
        while(i<M){
            minefield[i][j]='-';
            blank[i][j]=minefield[i][j];
            final[i][j]=minefield[i][j];
            i++;
        }
        i=0;
        j++;
    }
    mines=0;
    while(mines<totalMines){
        i=rand()%(M);
        j=rand()%(N);
        if(minefield[i][j]!='*'){
            minefield[i][j]='*';
            final[i][j]=minefield[i][j];
            mines++;
        }
    }
    i=0;
    j=0;
    while(j<N){
        while(i<M){
            if(minefield[i][j]!='*'){
                minefield[i][j]=0;
            }
            if((minefield[i-1][j-1]=='*')&&(minefield[i][j]!='*')){
                minefield[i][j]++;
            }
            if((minefield[i-1][j]=='*')&&(minefield[i][j]!='*')){
                minefield[i][j]++;
            }
            if((minefield[i][j-1]=='*')&&(minefield[i][j]!='*')){
                minefield[i][j]++;
            }
            if((minefield[i-1][j+1]=='*')&&(minefield[i][j]!='*')){
                minefield[i][j]++;
            }
            if((minefield[i+1][j-1]=='*')&&(minefield[i][j]!='*')){
                minefield[i][j]++;
            }
            if((minefield[i+1][j]=='*')&&(minefield[i][j]!='*')){
                minefield[i][j]++;
            }
            if((minefield[i][j+1]=='*')&&(minefield[i][j]!='*')){
                minefield[i][j]++;
            }
            if((minefield[i+1][j+1]=='*')&&(minefield[i][j]!='*')){
                minefield[i][j]++;
            }
            i++;
        }
        i=0;
        j++;
    }
    i=0;
    j=0;
}

//Printing updated Minefields
void print(){
    int i=0,j=0,z=0;
    while(z<M){
        if(z==0){
            printf("\t");
        }
        printf("|%d|\t",z);
        z++;
    }
    printf("\n\n");
    while(j<N){
        printf("|%d|\t",j);
        while(i<M){
            if(blank[i][j]=='-'){
                printf("|%c|\t",blank[i][j]);
            }
            else if(minefield[i][j]==0){
                blank[i][j]='B';
                printf("|%c|\t",blank[i][j]);
            }
            else{
                printf("|%d|\t",blank[i][j]);
            }
            i++;
        }
        printf("\n");
        i=0;
        j++;
    }
}

//Guessing function to check whether you hit mine or not
void guess(){
    int q=0,i=0,j=0,match=0;
    print();
    while(j<N){
        while(i<M){
            if(minefield[i][j]==blank[i][j]){
                match++;
            }
            i++;
        }
        i=0;
        j++;
    }
    if(match==((M*N)-totalMines)){
        Win();
    }
    printf("\nEnter the x value, then a space, then the y value:");
    scanf("%d %d",&x,&y);                                 
    FLUSH;
    if((x>=M)||(x<0)||(y<0)||(y>=N)){
        printf("\nPlease enter a value inside the grid\n");
        guess();
    }
    if(minefield[x][y]=='*'){
        boom();
    }
    if(blank[x][y]!='-'){
        printf("\nPlease enter a value that has not already been entered\n");
        guess();
    }
    else{
        blank[x][y]=minefield[x][y];
        if(minefield[x][y]==0){
            if(minefield[x-1][y-1]==0){
                blank[x-1][y]=minefield[x-1][y];
            }
            if(minefield[x-1][y]==0){
                blank[x-1][y]=minefield[x-1][y];
            }
            if(minefield[x][y-1]==0){
                blank[x][y-1]=minefield[x][y-1];
            }
            if(minefield[x-1][y+1]==0){
                blank[x-1][y+1]=minefield[x-1][y+1];
            }
            if(minefield[x+1][y-1]==0){
                blank[x+1][y-1]=minefield[x+1][y-1];
            }
            if(minefield[x+1][y]==0){
                blank[x+1][y]=minefield[x+1][y];
            }
            if(minefield[x][y+1]==0){
                blank[x][y+1]=minefield[x][y+1];
            }
            if(minefield[x+1][y+1]==0){
                blank[x+1][y+1]=minefield[x+1][y+1];
            }
        }
        guess();
    }
}

//Hitting Mine and game lost
void boom(){
    print_final();
    printf("\n\t\tYou hit a mine at %d,%d\n\t\tYOU LOSE!!!!",x,y);
    playAgain();
}

//Printing Final Minefield after Win or Lose
void print_final(){
    int i=0,j=0,z=0;
    while(z<M){
        if(z==0){
            printf("\t");
        }
        printf("|%d|\t",z);
        z++;
    }
    printf("\n\n");
    while(j<N){
        printf("|%d|\t",j);
        while(i<M){
            printf("|%c|\t",final[i][j]);
            i++;
        }
        printf("\n");
        i=0;
        j++;
    }
}

//Winning the game
void Win(){
    printf("\n\n\n\t\t\tYOU WIN!!!!!\n\n\n");
    playAgain();
}

//Option to play again
void playAgain(){
    char option[2];
    printf("\n\t\tWould you like to play again(Y/N)?:");
    scanf("%c",&option[0]);
    FLUSH;
    if((option[0]=='Y')||(option[0]=='y')){
        level();
    }
    else if((option[0]=='N')||(option[0]=='n')){
        gameLost();
    }
    else{
        printf("Please enter either Y or N");
        playAgain();
    }
}

//Game lost/ Game Over
void gameLost(){
    printf("\n\n\t\tGame Over");
    exit(1);
}

//Main driving function
int main(){
    printf("\t\tWelcome to Minesweeper\n");
    level();
    return 0;
}
