class FileReader:
    def ReadLines(self, fileName):
        file = open(fileName, 'r')
        lines = file.readlines()
        file.close()
        return lines

    def ReadOneLine(self, fileName):
        file = open(fileName, 'r')
        line = file.readline()
        file.close()
        return line