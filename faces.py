def main():
    str = input()
    result = convert(str)
    print(result)


def convert(str):
    str1 = str.replace(":)" , "🙂")
    str2 = str1.replace(":(" , "🙁")
    return str2

main()
