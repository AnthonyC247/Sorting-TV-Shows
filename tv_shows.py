# Type your code here

filename = input()
d = {}

with open(str(filename), 'r') as txt:
    lines = txt.readlines()
    for i in range(0, len(lines), 2):

        if i % 2 == 0:
            if lines[i].strip('\n') not in d:
                list1 = []
                list1.append(lines[i + 1].strip('\n'))
                d[lines[i].strip('\n')] = list1
            else:
                d[lines[i].strip('\n')].append(lines[i + 1].strip('\n'))
    f = open('output_keys.txt', 'w')
    v = sorted(d)
    for x in range(len(v)):
        print(f"{v[x]}")
        if len(d.get(v[x])) < 2:
            f.write(str(v[x]).lstrip('0') + ": " + d.get(v[x])[0] + "\n")
        else:
            f.write(str(v[x]).lstrip('0') + ": ")
            for j in range(len(d.get(v[x]))):
                if j == len(d.get(v[x])) - 1:
                    f.write(d.get(v[x])[j] + "\n")
                else:
                    f.write(d.get(v[x])[j] + "; ")
    f.close()

    x = []
    for i in d.values():
        for item in i:
            x.append(item)

    f = open('output_titles.txt', 'w')
    for i in sorted(x):
        f.write(i + "\n")
    f.close()



