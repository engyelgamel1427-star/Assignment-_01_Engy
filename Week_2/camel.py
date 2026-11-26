def main():
    camel = input("camelcase:").strip()
    snake = ""
    for c in camel:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    print(f"snake_case: {snake}")
main()
