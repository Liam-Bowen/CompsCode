
def batters():
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 = []
    list16 = []
    list17 = []
    list18 = []
    list19 = []
    list20 = []
    list21 = []
    list22 = []
    list23 = []
    list24 = []
    list25 = []
    list26 = []
    list27 = []
    list28 = []
    list29 = []
    list30 = []
    list31 = []

    with open('batters.txt') as f:
        for line in f.readlines():
            l = line.strip().split(',')
            list1.append(l[0])
            list2.append(l[1])
            list3.append(l[2])
            list4.append(l[3])
            list5.append(l[4])
            list6.append(l[5])
            list7.append(l[6])
            list8.append(l[7])
            list9.append(l[8])
            list10.append(l[9])
            list11.append(l[10])
            list12.append(l[11])
            list13.append(l[12])
            list14.append(l[13])
            list15.append(l[14])
            list16.append(l[15])
            list17.append(l[16])
            list18.append(l[17])
            list19.append(l[18])
            list20.append(l[19])
            list21.append(l[20])
            list22.append(l[21])
            list23.append(l[22])
            list24.append(l[23])
            list25.append(l[24])
            list26.append(l[25])
            list27.append(l[26])
            list28.append(l[27])
            list29.append(l[28])
            list30.append(l[29])
            list31.append(l[30])


    data = [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12, list13, list14, list15, list16, list17, list18, list19, list20, list21, list22, list23, list24, list25, list26, list27, list28, list29, list30, list31]

    player = []
    for set in data:
        player.append(set[701])


    print(player)



