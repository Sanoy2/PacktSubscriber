from TitleGetter import TitleGetter

def GetTitle():
    Getter = TitleGetter()
    title = Getter.GetTitle()
    return title


def main():
    print(GetTitle())
    

if __name__ == "__main__":
    main()