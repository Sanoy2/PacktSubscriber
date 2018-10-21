class FileReader:
    def ReadLines(self, fileName):
        file = open(fileName, 'r')
        lines = file.readlines()
        file.close()
        return lines
