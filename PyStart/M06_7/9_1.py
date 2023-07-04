from os import remove, path

class File:
    @staticmethod
    def delete(filename: str):
        remove(filename)

    @staticmethod
    def read_file(filename: str):
        file = open(filename, "r")
        # return file.readlines() # z \n
        return [line.strip() for line in file.readlines()] # jako lista
        # return (line.strip() for line in file.readlines()) # jako generator


    @staticmethod
    def exists(filename: str):
        return path.exists(filename) # is file exists???


print(File.exists("test.txt")) # True
print(File.read_file("test.txt"))
print(File.delete("test.txt")) # None
print(File.exists("test.txt")) # False


















