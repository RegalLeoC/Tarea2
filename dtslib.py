def count_unique_values(inserted):
    reserve = []
    o = 0

    for i in range(0,len(inserted)-1,1):
        for x in range(0,len(reserve)-1,1):
            if reserve[x] == inserted(i):
                o = o + 1
        if o > 1:
            o = 0
        elif o == 1:
            reserve.append(inserted[i])
            o=0

    return reserve