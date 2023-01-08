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
    print("\nStan rejestrów procesora Intel 8086: \n")
    for register in registers:
        print(register, "=", registers[register])


def user_input():
    for r in registers:
        registers[r] = hex(int(input("Podaj wartość przechowywaną w rejestrze {r}: "), 16))


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
            "\nWybierz czynność, którą chcesz wykonać:\n\nZmiana wartości rejestrów - 1\nWprowadź polecenie pomiędzy rejestrami do wykonania przez program - 2\nWprowadź polecenie pomiędzy rejestrami a pamięcią do wykonania przez program- 3\nZamknij - 4\n\n"))
        if action == 1:
            wrong_inputs = True
            while wrong_inputs:
                user_input()
                if inputs_hex_and_8_bit():
                    wrong_inputs = False
                else:
                    print("\nDane nie są 8 bitowe!\n")
        elif action == 2:
            instruction = int(
                input(
                    "\nWybierz polecenie dla symulacji:\nMOV  - 1\nXCHG - 2\nNOT  - 3\nINC  - 4\nDEC  - 5\nAND  - 6\nOR   - 7\nXOR  - 8\nADD  - 9\nSUB  - 10\n\n"))
            if instruction == 1:
                reg1 = input("Wybierz pierwszy rejestr dla polecenia MOV: ").upper()
                reg2 = input("Wybierz drugi rejestr dla polecenia MOV: ").upper()
                if reg1 and reg2 in registers:
                    MOV(reg2, reg1)
                    print("\n")
                else:
                    print("\nZły rejestr!")
            elif instruction == 2:
                reg1 = input("Wybierz pierwszy rejestr dla polecenia XCHG: ")
                reg2 = input("Wybierz drugi rejestr dla polecenia XCHG: ")
                if reg1 and reg2 in registers:
                    XCHG(reg1, reg2)
                else:
                    print("\nZły registers!")
            elif instruction == 3:
                reg = input("Wybierz rejestr dla polecenia NOT: ")
                if reg in registers:
                    NOT(reg)
                else:
                    print("\nZły rejestr!")
            elif instruction == 4:
                reg = input("Wybierz rejestr dla polecenia INC: ")
                if reg in registers:
                    INC(reg)
                else:
                    print("\nZły rejestr!")
            elif instruction == 5:
                reg = input("Wybierz rejestr dla polecenia DEC: ")
                if reg in registers:
                    DEC(reg)
                else:
                    print("\nZły rejestr!")
            elif instruction == 6:
                reg1 = input("Wybierz pierwszy rejestr dla polecenia AND: ")
                reg2 = input("Wybierz drugi rejestr dla polecenia AND: ")
                if reg1 and reg2 in registers:
                    AND(reg1, reg2)
                else:
                    print("\nZły rejestr!")
            elif instruction == 7:
                reg1 = input("Wybierz pierwszy rejestr dla polecenia OR: ")
                reg2 = input("Wybierz drugi rejestr dla polecenia OR: ")
                if reg1 and reg2 in registers:
                    OR(reg1, reg2)
                else:
                    print("\nZły rejestr!")
            elif instruction == 8:
                reg1 = input("Wybierz pierwszy rejestr dla polecenia XOR: ")
                reg2 = input("Wybierz drugi rejestr dla polecenia XOR: ")
                if reg1 and reg2 in registers:
                    XOR(reg1, reg2)
                else:
                    print("\nZły rejestr!")
            elif instruction == 9:
                reg1 = input("Wybierz pierwszy rejestr dla polecenia ADD: ")
                reg2 = input("Wybierz drugi rejestr dla polecenia ADD: ")
                if reg1 and reg2 in registers:
                    ADD(reg1, reg2)
                else:
                    print("\nZły rejestr!")
            elif instruction == 10:
                reg1 = input("Wybierz pierwszy rejestr dla polecenia SUB: ")
                reg2 = input("Wybierz pierwszy rejestr dla polecenia SUB: ")
                if reg1 and reg2 in registers:
                    SUB(reg1, reg2)
                else:
                    print("\nZły rejestr!")
            else:
                print("Złe polecenie!")
        elif action == 3:
            try:
                object1 = input("Wybierz rejestr lub komórkę pamięci dla polecenia: ")
                if object1.upper() in registers:
                    object2 = input("Wybierz komórkę pamięci dla polecenia: ")
                    if 255 < object2 < 65536:
                        registers[object1] = memory[int(object2, 16)]
                    else:
                        print("Zła komórka pamięci!")
                elif int(object1, 16) < 65536:
                    object2 = input("Wybierz drugi rejestr dla polecenia: ")
                    if object2.upper() in registers:
                        memory[int(object1, 16)] = registers[object2]
                    else:
                        print("Zły rejestr!")
                else:
                    print("Zły rejestr lub komórka pamięci!")
            except ValueError:
                print("BŁĄD")
        elif action == 4:
            break
        else:
            print("Zła czynność!")
    except ValueError:
        print("\nBŁĄD!")