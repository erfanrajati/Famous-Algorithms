def validParenthesis(s: str):
    parenthesis = {
        '(':')',
        '[':']',
        '{':'}'
    }
    stack = []
    for c in s:
        if c in parenthesis.keys():
            stack.append(c)
        elif c in parenthesis.values():
            if stack == []: 
                print("false")
                return False
            if parenthesis[stack[-1]] == c:
                stack.pop(-1)
            else:
                print("false")
                return False
    if stack == []:
        print("true")
        return True
    print("false")
    return False


def main():
    input_str = input()
    validParenthesis(input_str)


if __name__ == "__main__":
    main()

