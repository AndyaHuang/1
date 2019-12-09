import sys


class Output:
    def write_file(self, content):
        file = open("result.txt", "w")
        file.write(content)
        file.close()

    def read_file(self):
        try:
            file = open("message.txt", "r")
            content = file.read()
            file.close()
            return content
        except FileNotFoundError:
            print("ERROR 404, input file not found")
            sys.exit(0)
