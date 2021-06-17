#include <bits/stdc++.h>

using namespace std;

class Player
{
 public:
        void play();           //for the computer players only
        string hand;
        int hands_won;
        string name;
};

void Player::play()
{
    string choices[3]{"rock", "paper", "scissors"};
    
    hand = choices[rand()%3];                   
}
vector<Player> players(2);

void print_winner(int mode);

bool GAME_OVER();

void game_start(){
    cout << "-------------------------------------------\n";
    cout << "       Select a mode: \n";
    cout << "--> 1. Human v/s Computer\n";
    cout << "-------------------------------------------\n";
    int mode;
    cin >> mode;
    if (mode == 1){
        cout << "Enter your name: ";
        cin >> players[0].name;
        players[1].name = "Computer";
    }
    while (mode == 1)
	{ 
        while (!GAME_OVER())
		{
            cout << "\nWhat will you Choose? rock, paper, or scissors? ";
            cin >> players[0].hand;
            players[1].play();
            cout << endl;
            cout << "You Choose: " << players[0].hand << "  Computer Choose: " << players[1].hand << endl; 
            print_winner(1);
            while (players[0].hand == players[1].hand)
			{ 
                cout << "\n What will you Choose? rock, paper, or scissors? ";
                cin >> players[0].hand;
                players[1].play();
                cout << endl;
                cout << "You Choose: " << players[0].hand << "   Computer Choose: " << players[1].hand <<endl;
                print_winner(1);
            }
        }
        if (GAME_OVER())
		{ 
            if (players[0].hands_won == 2)
			{
                cout << "Congrats , " << players[0].name << ". You win the game!\n";
                return;
            }
			else
			{
                cout << "Game over. You lose.\n";
                return ;
            }
        }

    }
}
void print_winner(int mode)
{ 
    if (mode == 1)
	{
        if (players[0].hand == "rock" && players[1].hand == "scissors")
		{
            cout << "     You win!";
            players[0].hands_won += 1;
        }
		else if (players[0].hand == "scissors" && players[1].hand == "paper")
		{
            cout << "    You win!";
            players[0].hands_won += 1;
        }
		else if (players[0].hand == "paper" && players[1].hand == "rock")
		{
            cout << "    You win!";
            players[0].hands_won += 1;
        }
		else if (players[0].hand == players[1].hand)
		{
            cout << "        It's a draw!";
        }
		else
		{
        cout << "        Computer wins!";
        players[1].hands_won += 1;
        }
    }
	else
	{
        if (players[0].hand == "rock" && players[1].hand == "scissors")
		{
            cout << "        Computer 1 wins!";
            players[0].hands_won += 1;
        }
		else if (players[0].hand == "scissors" && players[1].hand == "paper")
		{
            cout << "        Computer 1 wins!";
            players[0].hands_won += 1;
        }
		else if (players[0].hand == "paper" && players[1].hand == "rock")
		{
            cout << "        Computer 1 wins!";
            players[0].hands_won += 1;
        }
		else if (players[0].hand == players[1].hand)
		{
            cout << "        It's a draw!";
        }
		else
		{
            cout << "        Computer 2 wins!";
        players[1].hands_won += 1;
        }
    }
}
int main()
{   
    srand(time(NULL));
    cout << "---------------------------------------------------\n";
    cout << "Welcome to Rock, Paper, Scissors.\nTo play, type '1'. \nTo exit, type '2'.\n";
    cout << "---------------------------------------------------\n";
    int choice;
    cin >> choice;
    switch (choice)
	{
        case 1:
            game_start();
            break;
        case 2:
            return 0;
        default:
            cout << "You made an invalid choice. Exiting game...";
            return 0;
    }
    
    if (GAME_OVER())
	{ 
        cout << "Would you like to play again? <y/n>   ";
        char input;
        cin >> input;
        if (input == 'y')
		{
            game_start();
        }
        return 0;
    }
}

bool GAME_OVER()
{
    if(players[0].hands_won == 2 || players[1].hands_won == 2)
	{                                                   
        return true;
    }
    return false;
}