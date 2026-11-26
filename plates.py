def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")
def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False
    if not s.isalnum():
        return False
    if s[0] == "0":
        return False
    for i in range(len(s) - 1):
        if s[i].isdigit() and not s[i + 1].isdigit():
            return False
    return True
main() 