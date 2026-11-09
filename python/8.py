#a1=11
b=[i for i in range(11,10**4)]
for a2 in b:
    if a1<=a2:
        for a3 in b:
            if a2<=a3:
                for a4 in b:
                    if a3<=a4:
                        for a5 in b:
                            if a4<=a5:
                                for a6 in b:
                                    if a5<=a6:
                                        for a7 in b:
                                            if a6<=a7:
                                                if a2-a1==a3-a2 and a4-a3==a5-a4 and a6-a5==a7-a6:
                                                    if a3*a3==a2*a4 and a5*a5==a4*a6:
                                                        print(a1,a2,a3,a4,a5,a6,a7)
                                                        print(a1,a2,a3,a4,a5,a6,a7)