def swap_case(s):
    result = ""
    for i in s:
        if i== i.lower():
            result += i.upper()
        else:
            result += i.lower()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)