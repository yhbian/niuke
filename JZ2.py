def replaceSpace(s):
    # write code here
    b = ''
    for item in list(s):
        if item == ' ':
            b += '%20'
        else:
            b += item
    return b


if __name__ == '__main__':
    s = 'I am'
    print(replaceSpace(s))
