/*
Solving a backtracking problem ->
1. Choice -> Choose number from 1 to 9 to fill the empty cell
2. Constraints -> Check if the number break the row, column or subgrid constraint
3. Goal -> fill the board
*/

let grid = [[],[],[],[],[],[],[],[],[]];

let N = 9;

let num = 0;

let gridHTML = document.getElementsByTagName("input");


function solver() {
    let numberInCell = 0;
    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
            num = (i * 9) + (j);
            
            numberInCell = gridHTML[num].value
            // console.log(numberInCell)
            if (gridHTML[num].value == "") {
                grid[i][j] = 0
            }
            else if(isNaN(numberInCell) || numberInCell < 1 || numberInCell > 9) {
                alert("Input only number between 1 and 9")
                return;
            }
            else {
                if(checkConstraint(i,j,numberInCell)) {
                    grid[i][j] = numberInCell
                }
                else {
                    // console.log(i+" "+j+" "+grid[i][j])
                    alert("Invalid Input")
                    return
                }
            }
        }
    }

    // call the sudoku solve function
    if(solveSudoku(0, 0)) {
            // print grid
        for (let i = 0; i < N; i++) {
            for (let j = 0; j < N; j++) {
                num = (i * 9) + (j);
                gridHTML[num].value = grid[i][j];
            }
        }
    }
    else console.log("No")
}

// Sudoku Solver function

function solveSudoku(row, column) {

    if (row == N - 1 && column == N)
        return true;

    // if we reached the end of the row then go to next row and set column to start
    if (column == N) {
        row++;
        column = 0
    }

    // if cell is filled go to next column
    if (grid[row][column] > 0) {
        return solveSudoku(row, column + 1)
    }

    for (let i = 1; i <= N; i++) {
        if (checkConstraint(row, column, i)) {
            grid[row][column] = i;

            if (solveSudoku(row, column + 1))
                return true;
        }
        grid[row][column] = 0;
    }
    return false;
}

// check constraint for the number 
function checkConstraint(row, col, num) {

    // Check if we find the same num in the similar row, we return false
    for (let x = 0; x <= 8; x++)
        if (grid[row][x] == num)
            return false;

    // Check if we find the same num in the similar column, we return false
    for (let x = 0; x <= 8; x++)
        if (grid[x][col] == num)
            return false;

    // Check if we find the same num in the particular 3*3 matrix, we return false
    let startRow = row - row % 3,
        startCol = col - col % 3;

    for (let i = 0; i < 3; i++)
        for (let j = 0; j < 3; j++)
            if (grid[i + startRow][j +
                startCol] == num)
                return false;

    return true;
}