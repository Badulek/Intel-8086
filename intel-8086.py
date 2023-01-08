from random import *
memory = []
for i in range(65536):
    memory.append(randint(0, 255))

registers = {"AL": None,
             "AH": None,
             "BL": None,
             "BH": None,
             "CL": None,
             "CH": None,
             "DL": None,
             "DH": None,
             }


def register_state():
    print("\nState of the registers of Intel 8086 processor: \n")
    for register in registers:
        print(register, "=", registers[register])


def user_input():
    for r in registers:
        registers[r] = hex(int(input(f"Enter value stored in {r} register: "), 16))


def inputs_hex_and_8_bit():
    try:
        return all(int(value, 16) <= 255 for value in registers.values())
    except ValueError:
        return False


def MOV(a, b):
    registers[a] = registers[b]


def XCHG(x, y):
    registers[x], registers[y] = registers[y], registers[x]


def NOT(x):
    temp = int(registers[x], 16)
    registers[x] = hex(255 - temp)


def INC(x):
    temp = int(registers[x], 16)
    temp += 1
    registers[x] = hex(temp)


def DEC(x):
    temp = int(registers[x], 16)
    temp -= 1
    registers[x] = hex(temp)


def AND(x, y):
    registers[x] = hex(int(registers[x], 16) & int(registers[y], 16))


def OR(x, y):
    registers[x] = hex(int(registers[x], 16) | int(registers[y], 16))


def XOR(x, y):
    registers[x] = hex(int(registers[x], 16) ^ int(registers[y], 16))


def ADD(x, y):
    registers[x] = hex(int(registers[x], 16) + int(registers[y], 16))


def SUB(x, y):
    registers[x] = hex(int(registers[x], 16) - int(registers[y], 16))


while True:
    register_state()
    try:
        action = int(input(
            "\nEnter action you want to execute:\n\nChange values of the registers - 1\nEnter instruction between registers for program to execute - 2\nEnter instruction between registers and memory for program to execute - 3\nQuit - 4\n\n"))
        if action == 1:
            wrong_inputs = True
            while wrong_inputs:
                user_input()
                if inputs_hex_and_8_bit():
                    wrong_inputs = False
                else:
                    print("\nInputs not 8 bit !\n")
        elif action == 2:
            instruction = int(
                input(
                    "\nChoose instruction for simulation:\nMOV  - 1\nXCHG - 2\nNOT  - 3\nINC  - 4\nDEC  - 5\nAND  - 6\nOR   - 7\nXOR  - 8\nADD  - 9\nSUB  - 10\n\n"))
            if instruction == 1:
                reg1 = input("Enter first register for MOV instruction: ").upper()
                reg2 = input("Enter second register for MOV instruction: ").upper()
                if reg1 and reg2 in registers:
                    MOV(reg2, reg1)
                    print("\n")
                else:
                    print("\nWrong registers!")
            elif instruction == 2:
                reg1 = input("Enter first register for XCHG instruction: ")
                reg2 = input("Enter second register for XCHG instruction: ")
                if reg1 and reg2 in registers:
                    XCHG(reg1, reg2)
                else:
                    print("\nWrong registers!")
            elif instruction == 3:
                reg = input("Enter register for NOT instruction: ")
                if reg in registers:
                    NOT(reg)
                else:
                    print("\nWrong register!")
            elif instruction == 4:
                reg = input("Enter register for INC instruction: ")
                if reg in registers:
                    INC(reg)
                else:
                    print("\nWrong register!")
            elif instruction == 5:
                reg = input("Enter register for DEC instruction: ")
                if reg in registers:
                    DEC(reg)
                else:
                    print("\nWrong register!")
            elif instruction == 6:
                reg1 = input("Enter first register for AND instruction: ")
                reg2 = input("Enter second register for AND instruction: ")
                if reg1 and reg2 in registers:
                    AND(reg1, reg2)
                else:
                    print("\nWrong registers!")
            elif instruction == 7:
                reg1 = input("Enter first register for OR instruction: ")
                reg2 = input("Enter second register for OR instruction: ")
                if reg1 and reg2 in registers:
                    OR(reg1, reg2)
                else:
                    print("\nWrong registers!")
            elif instruction == 8:
                reg1 = input("Enter first register for XOR instruction: ")
                reg2 = input("Enter second register for XOR instruction: ")
                if reg1 and reg2 in registers:
                    XOR(reg1, reg2)
                else:
                    print("\nWrong registers!")
            elif instruction == 9:
                reg1 = input("Enter first register for ADD instruction: ")
                reg2 = input("Enter second register for ADD instruction: ")
                if reg1 and reg2 in registers:
                    ADD(reg1, reg2)
                else:
                    print("\nWrong registers!")
            elif instruction == 10:
                reg1 = input("Enter first register for SUB instruction: ")
                reg2 = input("Enter second register for SUB instruction: ")
                if reg1 and reg2 in registers:
                    SUB(reg1, reg2)
                else:
                    print("\nWrong registers!")
            else:
                print("Wrong instruction!")
        elif action == 3:
            try:
                object1 = input("Enter register or memory cell for instruction: ")
                if object1.upper() in registers:
                    object2 = input("Enter memory cell for instruction: ")
                    if 255 < object2 < 65536:
                        registers[object1] = memory[int(object2, 16)]
                    else:
                        print("Wrong memory cell!")
                elif int(object1, 16) < 65536:
                    object2 = input("Enter second register for instruction: ")
                    if object2.upper() in registers:
                        memory[int(object1, 16)] = registers[object2]
                    else:
                        print("Wrong register!")
                else:
                    print("Wrong register or memory cell!")
            except ValueError:
                print("ERROR")
        elif action == 4:
            break
        else:
            print("Wrong action!")
    except ValueError:
        print("\nERROR!")
