def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return(3 * number + 1)


def main():
    attempts = 0
    while attempts < 3:
        try:

            number = int(input("Please enter an integer: "))
            break
        except ValueError:
            attempts += 1
            print("You have tried " + str(attempts) + " times out of 3 times!")

            if attempts == 3:
                print("You have failed to enter a valid integer after 3 attempts. End of the program.")
                return
            else:
                print("Your input is not a number. Please enter a number.")
    while number != 1:
        number = collatz(number)


if __name__ == "__main__":
    main()
