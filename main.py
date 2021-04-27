print("Bryson Thadhani")
print()
def createMajor(num):
    majorGrades = []
    cnt = 0
    while num > 0:
        cnt += 1
        ma = float(input("Add major grade #" + str(cnt) + ": "))
        majorGrades.append(ma)
        num -= 1
    return majorGrades

def createMinor(num2):
    minorGrades = []
    cnt = 0
    while num2 > 0:
        cnt += 1
        mi = float(input("Add minor grade #" + str(cnt) + ": "))
        minorGrades.append(mi)
        num2 -= 1
    return minorGrades

def createOther(num3):
    otherGrades = []
    cnt = 0
    while num3 > 0:
        cnt += 1
        ot = float(input("Add other grade #" + str(cnt) + ": "))
        otherGrades.append(ot)
        num3 -= 1
    drop = input("Would you like to drop the lowest other grade?: ")
    if 'no' in drop:
        pass
    else:
        small = min(otherGrades)
        otherGrades.remove(small)
    return otherGrades

def calcMajorAvg(maList):
    total = sum(maList)
    avg = total/len(maList)
    return avg

def calcMinorAvg(miList):
    total = sum(miList)
    avg = total/len(miList)
    return avg

def calcOtherAvg(otList):
    total = sum(otList)
    avg = total/len(otList)
    return avg

def calcSixWeeksAvg(majorAvg, minorAvg, otherAvg):
    majAvg = float(majorAvg)
    minAvg = float(minorAvg)
    othAvg = float(otherAvg)
    totalAvg = ((majAvg * .55) + (minAvg * .30) + (othAvg * .15))
    if totalAvg >= 90:
        return (Colors.A + str(totalAvg) + Colors.END)
    elif totalAvg >= 80:
        return (Colors.B + str(totalAvg) + Colors.END)
    elif totalAvg >= 70:
        return (Colors.C + str(totalAvg) + Colors.END)
    else:
        return (Colors.F + str(totalAvg) + Colors.END)

class Colors:
    F = "\033[0;31m"
    A = "\033[0;32m"
    B = "\033[1;32m"
    C = "\033[1;33m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
