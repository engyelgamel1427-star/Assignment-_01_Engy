def main():
    text = input("Input: ")
    vowels = "aeiouAEIOU"
    for c in text:
        if c in vowels:
            text = text.replace(c, "")
    print(f"Output: {text}")
main()
