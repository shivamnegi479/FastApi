def fun():
    dic = {0: 2, 1: 3, 2: 4, 3: 5, 6: 8, 7:9, 8: 10, 10:12, 11:13, 4:15,34:55,35:44,44:57,58:64,57:67,5:14,67:71,71:85}
    lis=[[x,y] for x,y in dic.items()]
    for i in lis:
        for j in lis:
            if i[1]==j[0]:
                i[1]=j[1]
    seen_second_elements = {}
    new_list = []
    for element in lis:
        second_element = element[1]
        if second_element not in seen_second_elements:
            seen_second_elements[second_element] = True
            new_list.append(element)
    print(new_list)
    op={x[0]:x[1] for x in new_list}
    print(op)
fun()