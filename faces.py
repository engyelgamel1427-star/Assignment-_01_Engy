def main():
    text = input("enter the text ")
    print(convert(text))
    
def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")
main()