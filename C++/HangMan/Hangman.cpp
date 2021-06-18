#include <bits/stdc++.h>

using namespace std;

const int MAX = 4;

int letters(char guess, string secretword, string &guessword)
{
	int i;
	int matches = 0;
	int len = secretword.length();
	for (i = 0; i< len; i++)
	{
		if (guess == guessword[i])
			return 0;
		
		if (guess == secretword[i])
		{
			guessword[i] = guess;
			matches++;
		}
	}
	return matches;
}

int main ()
{
	string name;
	char letter;
	int guesses = 0;
	string word;
	string words[] = {"india", "pakistan", "nepal", "malaysia", "srilanka", "australia", "iran", "ethiopia","indonesia"};

	srand(time(NULL));
	int n = rand()% 10;
	word = words[n];
	
	string s1(word.length(),'$');

	
	cout << "\n\nWelcome to Hangman.......\nGuess a country Name............";
	cout << "\n\nEach letter is represented by a $ .";
	cout << "\n\nYou have to type only one letter in one try";
	cout << "\n\nYou have " << MAX << " tries to try and guess the word.";
	cout << "\n-------------------------------------------------------";


	while (guesses < MAX)
	{
		cout << "\n\n" << s1;
		cout << "\n\nGuess a letter:- ";
		cin >> letter;
		
		if (letters(letter, word, s1)==0)
		{
			cout << endl << "Whoops! That letter isn't in there!" << endl;
			guesses++;
		}
		else
		{
			cout << endl << "You found a letter! Isn't that exciting!" << endl;
		}

		cout << " You have " << MAX - guesses;
		cout << " Guesses left." << endl;

		if (word == s1)
		{
			cout << word << endl;
			cout << "Yeah! You got it!";
			break;
		}

	}
	if(guesses == MAX)
	{
		cout << "\nSorry, You lose...You've been Hanged." << endl;
		cout << "\nThe word was : " << word << endl;
	}
	cin.ignore();
	cin.get();
	return 0;
}

