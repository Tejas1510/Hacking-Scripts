#include <bits/stdc++.h>
using namespace std;

int board[20][20];

bool isPossible(int n, int row, int col) {
    for(int i=0; i<row; i++) {      // for same coloumn
        if(board[i][col] == 1){
            return false;
        }
    }
    for(int i=row-1, j=col+1; i>=0 && j<n; i--, j++) {      // for right diagonal(up)
        if(board[i][j] == 1){
            return false;
        }
    }
    for(int i=row-1, j=col-1; i>=0 && j>=0; i--, j--) {     // for left diagonal(up)
        if(board[i][j] == 1){
            return false;
        }
    }
    return true;
}

void helper(int n, int row) {
    if(row == n){
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
        return;
    }

    for(int i=0; i<n; i++) {
        if(isPossible(n, row, i)) {
            board[row][i] = 1;
            helper(n, row+1);
            board[row][i] = 0;
        }
    }
    return;
}

void placeNQueens(int n) {
    memset(board, 0, 20*20*sizeof(int));        // for initializing with 0; (int board[20][20] = {0})

    helper(n, 0);
}

int main() {
    int n;
    cin >> n;
    placeNQueens(n);
    cout << "1 - Represents the position of Queens" << endl;
    cout << "0 - Represents the position of empty space" << endl;
    return 0;
}