
#include <iostream>
#include<windows.h>
using namespace std;
int main()
{
 int x,y,z;
 x=y=z=0;
 char ch1[100],ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9,ch10,ch11;
 cout<<"Guest Enter Your Name:";
 cin>>ch1;
 cout<<"Welcome "<<ch1<<"!!"<<" Lets start the quiz...";
 cout<<"\nEnter answer in form of 'a','b','c'and'd'";
 HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=2;
         SetConsoleTextAttribute(
            console_color, p);
 cout<<"\n1.The first computer architecture was introduced in?";
 cout<<"\na.1968\nb.1969\nc.1945\nd.1973";
 cout<<"\nYour answer:";
 cin>>ch2;
 if(ch2=='c')
 {
  x=x+10;
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=1;
         SetConsoleTextAttribute(
            console_color, p);
  cout<<"       Good Job!! Your score is "<<x;
 }
 else{
HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=2;
         SetConsoleTextAttribute(
            console_color, p);
 cout<<"          Sorry wrong answer!!";
 }

 cout<<"\n2.Which unit controls the movement of signals between CPU and I/O?";
cout<<"\na.Control unit\nb.Memory unit\nc.ALU\nd.Secondary storage ";
cout<<"\nYour answer:";
 cin>>ch2;
 if(ch2=='a')
 {
  x=x+10;
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=3;
         SetConsoleTextAttribute(
            console_color, p);
  cout<<"        Good Job!! Your score is "<<x;
 }
 else{
   HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=4;
         SetConsoleTextAttribute(
            console_color, p);
 cout<<"         Sorry wrong answer!!";
 }

 cout<<"\n3.The organization and interconnection of the various components of a computer system is ?";
cout<<"\na.Networks\nb.Architecture\nc.Graphics\nd.Designing ";
cout<<"\nYour answer:";
 cin>>ch2;
 if(ch2=='b')
 {
  x=x+10;
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=1;
         SetConsoleTextAttribute(
            console_color, p);
  cout<<"        Good Job!! Your score is "<<x;
 }
 else{
   HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=2;
         SetConsoleTextAttribute(
            console_color, p);
 cout<<"         Sorry wrong answer!!";
 }

 cout<<"\n4.A collection of wires that connects several devices is called ?";
cout<<"\na.Link\nb.Bus\nc.Cables\nd.Bidirectional wires";
cout<<"\nYour answer:";
 cin>>ch2;
 if(ch2=='b')
 {
  x=x+10;
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=3;
         SetConsoleTextAttribute(
            console_color, p);
  cout<<"         Your score is "<<x;
 }
 else{
   HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=4;
         SetConsoleTextAttribute(
            console_color, p);
 cout<<"          Sorry wrong answer!!";
 }

 cout<<"\n5.The hardware in which data may be stored for a computer system?";
cout<<"\na.Bus\nb.Register\nc.Memory\nd.Control unit ";
cout<<"\nYour answer:";
 cin>>ch2;
 if(ch2=='c')
 {
  x=x+10;
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=1;
         SetConsoleTextAttribute(
            console_color, p);
  cout<<"          Your score is "<<x;
 }
else{
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=2;
         SetConsoleTextAttribute(
            console_color, p);
cout<<"           Sorry wrong answer!!";
}

 cout<<"\n6.What is the software used to drive microprocessor-based system?";
cout<<"\na.Assembly language\nb.Machine language\nc.Firmware\nd.Micro language ";
cout<<"\nYour answer:";
 cin>>ch2;
 if(ch2=='a')
 {
  x=x+10;
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=3;
         SetConsoleTextAttribute(
            console_color, p);
  cout<<"           Your score is "<<x;
 }
 else{
   HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=4;
         SetConsoleTextAttribute(
            console_color, p);
 cout<<"            Sorry wrong answer!!";
 }
 
 cout<<"\n7.A structure is which type of datatype?";
 cout<<"\na.User defined data type\nb.Derived data type\nc.Primitive data type\nd.None of these ";
 cout<<"\nYour answer:";
 cin>>ch2;
 if(ch2=='a')
 {
  x=x+10;
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=1;
         SetConsoleTextAttribute(
            console_color, p);
  cout<<"           Your score is "<<x;
 }
 else{
   HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=2;
         SetConsoleTextAttribute(
            console_color, p);
 cout<<"            Sorry wrong answer!!";
 }
 
 cout<<"\n8.Which of the following is not a valid storage class?";
cout<<"\na.Static\nb.Extern\nc.Register\nd.Automatic ";
cout<<"\nYour answer:";
 cin>>ch2;
 if(ch2=='d')
 {
  x=x+10;
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=3;
         SetConsoleTextAttribute(
            console_color, p);
  cout<<"             Your score is "<<x;
 }
 else{
   HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=4;
         SetConsoleTextAttribute(
            console_color, p);
 cout<<"             Sorry wrong answer!!";
 }
 
 cout<<"\n9.Who was the first computer programer in the history of computer?";
cout<<"\na.Ada Lovelace\nb.Cristopher Kyana\nc.Joseph Jade\nd.Lan Morre ";
cout<<"\nYour answer:";
 cin>>ch2;
 if(ch2=='a')
 {
  x=x+10;
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=1;
         SetConsoleTextAttribute(
            console_color, p);
  cout<<"          Your score is "<<x;
 }
 else{
   HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=2;
         SetConsoleTextAttribute(
            console_color, p);
 cout<<"           Sorry wrong answer!!";
 }
 
 cout<<"\n10.The first microprocessor was developed in 1971 by?";
cout<<"\na.Apple\nb.Intel\nc.NASA\nd.All of these ";
cout<<"\nYour answer:";
 cin>>ch2;
 if(ch2=='b')
 {
  x=x+10;
  HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=3;
         SetConsoleTextAttribute(
            console_color, p);
  cout<<"           Your score is "<<x;
 }
 else{
   HANDLE console_color;
    console_color = GetStdHandle(
        STD_OUTPUT_HANDLE);
        int p=4;
         SetConsoleTextAttribute(
            console_color, p);
 cout<<"            Sorry wrong answer!!";
 }
 
 if(x==100)
 cout<<"          Perfect!! Keep it up";
 if(x==90)
 cout<<"          You are extremely intelligent!!";
 if(x==80)
 cout<<"         You are intelligent!!";
 if(50==x||x==70||x==60)
 cout<<"        You are average!! Better luck next time";
 else if(x<=40)
 cout<<"         Need to work hard";

 return 0;
}