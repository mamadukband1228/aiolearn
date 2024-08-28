def finder5(adad):
    adad_str = str(adad)

    tedad = 0

    for x in range(len(adad_str)):
        if adad_str[x]=="5":
            tedad = tedad + 1

    return tedad


tedad_col = 0

for i in range(15+1):
    tedad_col = tedad_col + finder5(i)

print(tedad_col)

