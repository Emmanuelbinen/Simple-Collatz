# Simple-Collatz

This Python program is designed to implement and demonstrate the Collatz sequence for a given integer input by the user.

## How does this Collatz Sequence Calculator Work?

If the number is even, divide it by 2; if the number is odd, multiply it by 3 and add 1. The sequence continues until the number reaches 1.

## How to Use

1. **Run the Program**: Execute the script directly in your Python environment.

2. **Enter an Integer**: When prompted, enter an integer. The program will attempt to validate your input up to 3 times. If you fail to enter a valid integer after 3 attempts, the program will terminate.


## Code Overview

### `collatz(number)` Function

This function takes an integer `number` as input and performs the Collatz sequence operation on it. 

### `main()` Function

The program starts by initializing a counter `attempts` to 0, which keeps track of the number of times the user has failed to enter a valid integer. The function then enters a loop that attempts to get a valid integer input from the user up to 3 times. If the input is not a valid integer, it increments the `attempts` counter and prints a message indicating the number of failed attempts. If the user fails to enter a valid integer after 3 attempts, the function prints a message and exits. If the input is valid, the function proceeds to the next step.

### Collatz Sequence Calculation

Once a valid integer is obtained, the program enters a loop where it repeatedly calls the `collatz` function with the current number until the number reaches 1. This loop demonstrates the Collatz sequence for the given number.

## Execution

The `if __name__ == "__main__":` line ensures that the `main()` function is called when the script is run directly. 
