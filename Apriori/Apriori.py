
def createC1(data_set):
    C1 = set()
    for data in data_set:
        for item in data:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1

def isApriori(Ck_item, Lksub1):
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lksub1:
            return False
    return True

def createCk(Lksub1, k):
    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]:
                Ck_item = list_Lksub1[i] | list_Lksub1[j]
                if isApriori(Ck_item, Lksub1):
                    Ck.add(Ck_item)
    return Ck


def generateLkByCk(data_set, Ck, min_support, support_data):
    Lk = set()
    item_count = {}
    for data in data_set:
        for item in Ck:
            if item.issubset(data):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    data_count = float(len(data_set))
    for item in item_count:
        if (item_count[item] / data_count) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / data_count
    return Lk



def generateLk(data_set, k, min_support):
    support_data = {}
    C1 = createC1(data_set)
    L1 = generateLkByCk(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    Lk = []
    Lk.append(Lksub1)
    for i in range(2, k+1):
        Ci = createCk(Lksub1, i)
        Li = generateLkByCk(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        Lk.append(Lksub1)
    return Lk, support_data


if __name__ == "__main__":
    data_set =  [['M1', 'M2', 'M5'], ['M2', 'M4'], ['M2', 'M3'], ['M1', 'M2', 'M4'], ['M1', 'M3'],['M2','M3'],['M1','M3'],
           ['M1', 'M2', 'M3','M5'],['M1','M2','M3']]
    L, support_data = generateLk(data_set, k=3, min_support=0.1)

    for Lk in L:
        print("=" * 20)
        print("frequent " + str(len(list(Lk)[0])) + "-itemsets\t\tsupport")
        print("=" * 20)
        for freq_set in Lk:
            print(freq_set, support_data[freq_set])


