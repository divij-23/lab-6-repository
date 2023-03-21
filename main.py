def main():
    menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Exit"         # menu with 3 options
    print(menu)


def encoder(num1):          # add 3 to each digit but make sure not more than 1 digit
    encode = []
    for i in range(len(num1)):
        nums = int(num1[i])
        nums = (nums + 3) % 10
        nums = str(nums)
        encode.append(nums)
    return "".join(encode)


def decoder(num2):
    pass


if __name__ == "__main__":
    encoder = True
    while encoder:
        main()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            num = input("Please enter your password to encode: ")
            print(encoder(num))
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            num = input("Please enter your password to decode: ")
            print(f"The encoded password is {num}, and the original password is {decoder(num)}.")      # print both decoded and encoded
        elif user_input == 3:
            break
