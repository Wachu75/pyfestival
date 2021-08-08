from os import remove, path


class File:
    @staticmethod
    def delete(filename: str):
        remove(filename)

    @staticmethod
    def read_file(filename: str):
        file = open(filename, 'r')
        return [line.strip() for line in file.readlines()]  # tak zwrócona zostanie lista która będzie zajmować miejcse w pamięci
        #return (line.strip() for line in file.readlines())  # tak zwrócony zostanie generator po którym będzie można iterować

    @staticmethod
    def exists(filename: str):
        return path.exists(filename)


print(File.exists('test.txt'))
if File.exists('test.txt'):
    print(File.read_file('test.txt'))
    print(File.delete('test.txt'))
    print(File.exists('test.txt'))