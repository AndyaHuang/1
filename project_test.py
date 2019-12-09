import string
from read_file import Output


alp_list_low = string.ascii_lowercase
alp_list_up = string.ascii_uppercase
running = True
results = ""


class Code(Output):
    def __init__(self):
        # giving prompts
        print("\nPut your content in 'message.txt', result will be in 'result.txt'")
        print("What do you want to do?")
        # giving user choices
        choice_main = int(input("1-encode\n2-decode\n3-exit\n"))
        global running
        global results
        message = Code.read_file(self)
        print("Which way you want to use?")
        # if user wants to encode
        if choice_main == 1:
            choice_enc = int(input("1-caesar\n2-rail fence\n"))
            if choice_enc == 1:
                key = int(input("please write key"))
                results = Code.cae_enc(self, key, message)
                print(results)
                Code.write_file(self, results)
            elif choice_enc == 2:
                results = Code.fen_enc(self, message)
                print(results)
                Code.write_file(self, results)
        # if user wants to decode
        elif choice_main == 2:
            choice_dec = int(input("1-caesar\n2-brute force caesar\n3-coming soon\n"))
            # if user wants to decode caesar
            if choice_dec == 1:
                key = int(input("please write key"))
                results = Code.cae_dec(self, key, message)
                print(results)
                Code.write_file(self, results)
            # if user wants to decode caesar by brute force
            elif choice_dec == 2:
                key = 1
                for i in range(25):
                    results = Code.cae_dec(self, key, message)
                    print(results)
                    keys = "key is " + str(key)
                    print(keys)
                    key += 1
            # another function
            elif choice_dec == 3:
                print("This option will be ready as soon as Mount&Blade 2 is ready.")
        # if user wants to leave
        elif choice_main == 3:
            print("Have a great day!")
            running = False

    # define encoding rail fence function
    def fen_enc(self, message):
        result = ""
        one = ""
        two = ""
        letter_num = 0
        for letter in message:
            if letter_num % 2 == 0:
                one += letter
            elif letter_num % 2 == 1:
                two += letter
            letter_num += 1
        result += one
        result += two
        return result

    # define encoding caesar function
    def cae_enc(self, key, message):
        # loading alphabet
        result = ""
        # encode one letter in message every time
        for letter in message:
            # if message is lower case
            if letter in alp_list_low:
                a = alp_list_low.index(letter)
                a += key
                a = a % 26
                result += alp_list_low[a]
            # if message is uppercase
            elif letter in alp_list_up:
                a = alp_list_up.index(letter)
                a += key
                a = a % 26
                result += alp_list_up[a]
            # if it's not a letter
            else:
                result += letter
        return result

    # define decoding caesar function
    def cae_dec(self, key, message):
        # loading alphabet
        result = ""
        # decode one letter in message every time
        for letter in message:
            # if message is lower case
            if letter in alp_list_low:
                a = alp_list_low.index(letter)
                a -= key
                while a <= 0:
                    a += 26
                a = a % 26
                result += alp_list_low[a]
            # if message is upper case
            elif letter in alp_list_up:
                a = alp_list_up.index(letter)
                a -= key
                while a <= 0:
                    a += 26
                a = a % 26
                result += alp_list_up[a]
            # if it's not a letter
            else:
                result += letter
        return result


# running class
while running is not False:
    q = Code()
