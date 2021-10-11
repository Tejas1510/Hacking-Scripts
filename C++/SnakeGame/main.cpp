#include <iostream>
#include<conio.h>
#include<windows.h>

HANDLE console=GetStdHandle(STD_OUTPUT_HANDLE);
using namespace std;
bool gameover;
const int width=20,height=17;
int x,y,fruitX,fruitY,score;
int tailX[100],tailY[100];
int nTail=0,sleeptime=170;
enum Direction {STOP=0,LEFT,RIGHT,UP,DOWN} ;
Direction dir;

void Setup()
{
    gameover=false;
    dir=STOP;
    x=width/2;
    y=height/2;
    fruitX=rand()%width;
    fruitY=rand()%height;
    score=0;
}
void Draw()
{
    system("cls");
    cout<<char(201);
    for(int i=0; i<width-2; i++)
        cout<<char(205);
    cout<<char(187);
    cout<<endl;
    for(int i=0; i<height; i++)
    {
        for(int j=0; j<width; j++)
        {
            if(j==0)
            {
                cout<<char(186);
            }
            else if(i==y&&j==x)
            {
                {
                    SetConsoleTextAttribute(console,10);
                    cout<<"O";
                    SetConsoleTextAttribute(console,15);
                }
            }

            else if(j==fruitX&&i==fruitY)
            {
                SetConsoleTextAttribute(console,12);
                cout<<"#";
                SetConsoleTextAttribute(console,15);
            }
            else if(j==width-1)
                cout<<char(186);
            else
            {
                bool print=false;
                SetConsoleTextAttribute(console,10);
                for(int k=0; k<nTail; k++)
                {
                    if(tailX[k]==j&&tailY[k]==i)
                    {
                        cout<<"o";
                        print=true;
                    }
                }

                SetConsoleTextAttribute(console,15);
                if(!print)
                    cout<<" ";
            }
        }
        cout<<endl;
    }
    cout<<char(200);
    for(int i=0; i<width-2; i++)
        cout<<char(205);
    cout<<char(188);
    cout<<endl<<"Score : "<<score;
}
void Input()
{
    switch(_getch())
    {
    case 'a':
        dir=LEFT;
        break;
    case 's':
        dir=DOWN;
        break;
    case 'w':
        dir=UP;
        break;
    case 'd':
        dir=RIGHT;
        break;
    case 'x':
        gameover=true;
    }
}
void Logic()
{
    int prevX=tailX[0];
    int prevY=tailY[0];
    int prev2X,prev2Y;
    tailX[0]=x;
    tailY[0]=y;
    for(int i=1; i<nTail; i++)
    {
        prev2X=tailX[i];
        prev2Y=tailY[i];
        tailX[i]=prevX;
        tailY[i]=prevY;
        prevX=prev2X;
        prevY=prev2Y;
    }
    switch(dir)
    {
    case DOWN:
        y++;
        break;
    case UP:
        y--;
        break;
    case RIGHT:
        x++;
        break;
    case LEFT:
        x--;
        break;
    }
    if(x==0)
        x=width-2;
    else if(x==width-1)
        x=0;
    else if(y>height-1)
        y=0;
    else if(y<0)
        y=height-2;
    for(int i=0; i<nTail; i++)
    {
        if(tailX[i]==x&&tailY[i]==y)
            gameover=true;
    }
    if(fruitX==x&&fruitY==y)
    {
        score+=10;
        if(sleeptime>60)
            sleeptime-=10;
        fruitX=rand()%width;
        fruitY=rand()%height;
        nTail++;
    }

}
int main()
{
    Setup();
    while(!gameover)
    {
        Draw();
        if(_kbhit())
            Input();
        Logic();
        Sleep(sleeptime);
    }
    return 0;
}
