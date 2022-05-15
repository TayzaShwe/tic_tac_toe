# printing the tic tac toe table
def print_table(table):
    print("")
    print(f"  {table[0]}  |  {table[1]}  |  {table[2]}  ")
    print("-----------------")
    print(f"  {table[3]}  |  {table[4]}  |  {table[5]}  ")
    print("-----------------")
    print(f"  {table[6]}  |  {table[7]}  |  {table[8]}  ")
    print("")

print_table(["O", "", "", "X", "", "", "O", "O", "X"])