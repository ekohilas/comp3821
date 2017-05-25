def num_sub(a, b):
    if not a:
        return num_sub(a)
    if a and b and a[0] == b[0]:
        return num_sub(a[1:], b[1:])
    elif a[0] == b[0]:
        return num_sub(a[1:], b[1:]) + 1


def find(a_s, b_s):
    a, b = a_s, b_s
    s = 0
    while b:
        if a[0] == b[0]:
            a, b = a[1:], b[1:]
            if not a:
                s += 1
                a = a_s
        else:
            b = b[1:]
    return s

if __name__ == "__main__":
    s = 0
    a, b = "Gks", "GeeksforGeeks"
    for k in range(len(b)):
        subs = b[k:]
        if subs.startswith(a[0]):
            print(a, b[k:], find(a, subs))
            s += find(a, subs)
    print(s)





