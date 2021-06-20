#include <iostream>

using namespace std;

int main()
{       
    string character,color,animal,celebrity,song_name,company,subject;
    int funny_number;
    cout << "Enter a character name " ;
    getline(cin,character);
    cout << "Enter any color " ;
    getline(cin,color);
    cout << "Enter a song name " ;
    getline(cin,song_name);
    cout << "Enter an animal " ;
    getline(cin,animal);
    cout << "Enter your favourite celebrity name " ;
    getline(cin,celebrity);
    cout << "Enter a Company name " ;
    getline(cin,company);
    cout << "Enter a subject " ;
    getline(cin,subject);
    cout << "Enter a funny number " ;
    cin >> funny_number;

    cout << "Hello everyone my name is "<<song_name<<".\n";
    cout << "I'm going to be talking about " << funny_number<<".\n";
    cout << "now what is a "<<celebrity<<".\n";
    cout << "it is the most important "<< animal << " that runs on a "<<character<<", ";
    cout << "which manages all the "<<color<<" memory and processes, as well as its "<<subject<<" and "<<celebrity<<".\n";
    cout << "it allows you to "<<funny_number<<" with a computer without knowing how to "<<company<<" the computer "<<song_name<<".\n";
    cout << "without a "<<animal<<", a "<<celebrity<<" is useless .\n ";

    return 0;
}

