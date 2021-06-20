#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int dates[180][3];
    int seat;
    int dd,mm,yy;
    char name[10];
    char names[5][10];
    for(int i =0;i<180;i++){
        for(int j=0;j<3;j++){
            dates[i][j]=0;
        }
    }
    for(int i =0;i<5;i++){
        for(int j=0;j<10;j++){
            names[i][j]='\0';
        }
    }
    do{
        cout<<"Please enter your name.(Only 1 word allowed.)\n";
        cin>>name;
        int i, j;
        int flag = 1;
        for (i = 0; i < 5; i++)
        {
            int ret;
            for (j = 0; j < 10; j++){
                ret = memcmp(names[i],name,10);
                if (ret==0){
                    cout<<"Found name in registry.\n";
                    flag = 0;
                    break;
                }
                else if(names[i][0]=='\0'){
                    cout<<"No more names in registry, adding name.\n";
                    for(int j=0;j<10;j++){
                        names[i][j]=name[j];
                    }
                    flag = 0;
                    break;
                }
                else{
                    continue;
                }
            }
            if (flag == 1){
                cout<<"Name not matching, checking next slot.\n";
                continue;
            }

            break;
        }

        char choice;
        cout<<"What would you like to do? Book(b) or Cancel(c)?\n";
        cin>>choice;
        if (choice=='b'){
            cout<<"Please enter date in DD MM YY\n";
            cin>>dd>>mm>>yy;
            if((1 <= dd)&&(dd <= 31) && (1 <= mm)&&(mm <= 12) && (yy == 21)){
                cout<<"Your chosen date is:\n"<<dd<<"-"<<mm<<"-"<<yy<<"\n";
                while(1){
                    cout<<"Please choose a seat from 1-180\t";
                    cin>>seat;
                    if (seat>180||seat<=0)
                        continue;
                    break;
                }
                for(int a=0;a<180;a++){
                    if(dates[a][0]==mm&&dates[a][1]==dd){
                        if (dates[a][2]==seat){
                            cout<<"This seat on this date has already been booked by"<<names[a]<<", sorry!\n";
                            break;
                        }
                    } 
                    else if(dates[a][0]==0&&dates[a][1]==0){
                        dates[a][0]=mm;
                        dates[a][1]=dd;
                        dates[a][2]=seat;
                        cout<<"Your seat,"<<seat<<", has been booked on: "<<dd<<"-"<<mm<<"-"<<yy<<"\n";
                        break;
                    }
                }
            }
            else
                cout<<"Please enter a valid date\n";
        }
        else if(choice=='c'){
            cout<<"Which date's seat would you like to cancel? (DD MM YY format)\n";
            cin>>dd>>mm>>yy;
            if((1 <= dd)&&(dd <= 31) && (1 <= mm)&&(mm <= 12) && (yy == 21)){
                while(1){
                    cout<<"Please choose a seat from 1-180\t";
                    cin>>seat;
                    if (seat>180||seat<=0)
                        continue;
                    break;
                }
                for (int a=0; a<180;a++){
                    if (dates[a][0]==mm&&dates[a][1]==dd){
                        if (dates[a][2]==seat&&!(memcmp(names[a],name,10))){
                            cout<<"This seat on this date has been cancelled!\n";
                            dates[a][0]=0;
                            dates[a][1]=0;
                            dates[a][2]=0;
                            break;
                        }
                        else if(dates[a][2]==seat){
                            cout<<"Sorry but this seat has been booked by another person. \n";
                            break;
                        }
                    }
                    else if(dates[a][0]==0&&dates[a][1]==0){
                        cout<<"This seat has not been booked on this day...\n";
                        break;
                    }
                }
            }
            else
                cout<<"Please enter a valid date\n";
        }
        else{
            cout<<"Please enter a valid choice...\n";
        }
    }while(true);
}
