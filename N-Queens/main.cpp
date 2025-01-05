// The 8 Queens problem

#include <iostream>
#include <string>
// #include <windows.h>

using namespace std;



//------------------------------------------- Property Section



int correctCol(int chessBoard[8][8], int col);
int queenInitializer(int chessBoard[8][8], int col);
void moveQueen(int chessBoard[8][8]);


int queenCount = 0; // Counts the number of queens in the board
int chessBoard[8][8] = {0}; // Simple 8*8 chess board
int position_counter = 0;



//------------------------------------------- Method Section



/*

A function of type boolean that we will later use to find whether the given coordinate is safe or not.
originally it was designed to loop on all 8 directions a queen can move scanning every single square looking for a queen.
but for this problem we only need this function to check the top, bottom, left, top left & bottom left directions. you will see why soon enough.

*/
bool isThreatened(int m, int n) {

    int i = m;
    int j = n;

    // Checking the TOP
    while (i > 0) {
        i -= 1;
        if (chessBoard[i][j] == 1) { return true; }
        else { continue; }
    }

    i = m;
    j = n;

    // Checking the LEFT
    while (j > 0) {
        j -= 1;
        if (chessBoard[i][j] == 1) { return true; }
        else { continue; }
    }

    i = m;
    j = n;

	// Checking the BOTTOM
    while (i < 7) {
        i += 1;
        if (chessBoard[i][j] == 1) { return true; }
        else { continue; }
    }

    i = m;
    j = n;

    // Checking the TOP LEFT
    while (i > 0 && j > 0) {
        i -= 1;
        j -= 1;
        if (chessBoard[i][j] == 1) { return true; }
        else { continue; }
    }

    i = m;
    j = n;

    // Checking the BOTTOM LEFT
    while (i < 7 && j > 0) {
        i += 1;
        j -= 1;
        if (chessBoard[i][j] == 1) { return true; }
        else { continue; }
    }

    i = m;
    j = n;


    return false;
}


/*

to print the board since C++ does not have a built in function to prints arrays.

*/
void printBoard() {
    int a = 0;
    int b = 0;

    while (a < 8) {
        while (b < 8) {
            cout << chessBoard[a][b] << " ";
            b += 1;
        }
        cout << "\n";
        a += 1;
        b = 0;
    }
    a = 0;
    b = 0;
}



/*

queenInitializer() function is declared to place queens in safe position, it iterates on each square of columns one by one
and initializes the queen as soon as it reaches a safe square, this algorithm uses the isThreatened() function to Scan squares.
later on, as soon as all 8 queens are placed, it returns a 0 to instantly jump out of the function.

 */
int queenInitializer(int inputBoard[8][8], int col) {

    // to break out if all queens are placed.
    if (queenCount == 8) {

		position_counter += 1;
		cout << "\n Solution Number " << position_counter << ": \n\n";
		printBoard();
		cout << "---------------------------------\n";

		moveQueen(chessBoard);
		if (position_counter == 92) { return 0; }

	}

    if (col < 8) {

        // iterates on a every square of a column.
        for (int row = 0; row < 9; row++) {

            if (queenCount == 8) { return 0; }
            if (position_counter == 92) { return 0; }


            // it will call the "correctCol()" function for the previous column, if all the squares were unsafe.
            if (row == 8) {
                    correctCol(chessBoard, col -= 1);
            }


            // If the function finds any safe square, it will instantly assign a queen.
            if ( !isThreatened(row, col) ) {

                chessBoard[row][col] = 1;
                queenCount += 1;

                queenInitializer(chessBoard, col += 1); // The function continues by moving to the next column.
            }
        }
    }
}



/*

of course it is likely that the first safe squares won't give us a complete solution for the matter.
therefore we designed another algorithm called correctCol() which runs as soon as queenInitializer() hits a dead end.
correctCol() will move to the previous column and moves the places queen of that column to the next safe square.
there two algorithms call each other and work together back and forth until the queenCount variable reaches the 8 desired value.
when the solution is given the functions return 0 to simply jump out.

*/
int correctCol(int inputBoard[8][8], int col) {

    if (queenCount == 8) { return 0; }

    for (int row = 0; row < 9; row++) { // by this loop, we are able to iterate on the cells of a column


        if (queenCount == 8) { return 0; }
        if (position_counter == 92) { return 0; }



        if (row == 8) { // If the function was not able to assign the new queen to any other cell of the column, it will call it self for the previous column

            correctCol(chessBoard, col -= 1);

        } else if (chessBoard[row][col] == 1) { // If the function finds the cell where queen assigned to it, it will remove the queen

            chessBoard[row][col] = 0;
            queenCount -= 1;

        } else if(!isThreatened(row, col)) { // after removing queen, it iterates the next cells of the column. If it finds the next possible cell (cell that won't be threated by any other queen) it assings the removed queen to that cell and runs the "queenInitializer()" for the next column.

            chessBoard[row][col] = 1;
            queenCount += 1;

            queenInitializer(chessBoard, col += 1);

        }
    }
}



/*

the very last function is declared to run after a solution was given by other algorithms.
moveQueen() is to make a very subtle change to the board in order to trigger the whole  code to run all over again
presenting another solution to the 8 Queens problem.
meaning our code will keep running until all 92 possible combinations are found and printed.

*/
void moveQueen(int chessBoard[8][8]){

	bool moved = false;

	for(int i = 0; i < 9; i++){

		if (moved == false){

			if(chessBoard[i][7] == 1){

				chessBoard[i][7] = 0;
				queenCount -= 1;
				moved = true;

			}

		} else if (i == 8) { // the correctCol() will be called if all the remaining squares are threatened by queens.

		    correctCol(chessBoard, 6);

        } else if ( !isThreatened(i, 7) ) { // To place the queen on the first safe square.

            chessBoard[i][7] = 1;
            queenCount += 1;
            queenInitializer(chessBoard, 8); // Getting back to the original function to continue initializing queens.

        }
	}
}



//------------------------------------------- Main Function



int main() {

	cout << "\n Cells with value of 1 represents queens : \n\n";
    queenInitializer(chessBoard, 0);

	system("pause");

}

/*

Contributors:
Erfan Rajati, Saleh Taleb Khojasteh, Mahdi Mahmoudkhani,
Mohammad Fallahi, AmirHossein Hashemi, Arman Akhoundy(c)

*/
