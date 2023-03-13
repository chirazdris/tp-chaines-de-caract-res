def crange(*cinterv):
    result = ""
    for interv in cinterv:
        start_char = min(interv[0], interv[1])
        end_char = max(interv[0], interv[1])
        for i in range(ord(start_char), ord(end_char)+1):
            result += chr(i)
    return result

chaine = crange(["a", "z"], ["A", "Z"], ["0", "9"])
print(chaine)
