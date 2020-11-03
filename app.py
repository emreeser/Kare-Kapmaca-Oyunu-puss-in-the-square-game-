def oyun_alani(sutun_say, satir_say,iki_boyut):
    satir_no = [1,2,3,4,5,6,7]
    sutun_harf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T"]
    dic_guney={"A":3,"B":11,"C":19,"D":27,"E":35,"F":43,"G":51,"H":59,"I":67,"J":75,"K":83,"L":91,"M":99,"N":107,"O":115,"P":123,"R":131,"S":139,"T":147}
    dic_dogu={"B":17,"C":25,"D":33,"E":41,"F":49,"G":57,"H":65,"I":73,"J":81,"K":89,"L":97,"M":105,"N":113,"O":121,"P":129,"R":137,"S":145,"T":153}
    dic_bati={"B":9,"C":17,"D":25,"E":33,"F":41,"G":49,"H":57,"I":65,"J":73,"K":81,"L":89,"M":97,"N":105,"O":113,"P":121,"R":129,"S":137,"T":145}
    h=0
    for i in range(5,sutun_say*8,8):
        iki_boyut[0][i]=sutun_harf[h]
        h+=1
    for i in range(2,satir_say*3+2):
        iki_boyut[i][1]="|"
    k=0
    for i in range(3,satir_say*3+1,3):
        iki_boyut[i][0]=satir_no[k]
        k+=1
    for i in range(2,sutun_say*8+1):
        iki_boyut[1][i]="_"
    for i in range(2,sutun_say*8+1):
        iki_boyut[satir_say*3+1][i] = "_"
    for i in range(2, satir_say * 3 + 2):
        iki_boyut[i][sutun_say*8+1]="|"
def dizi_yazdir(satir_say,sutun_say,iki_boyut):
    for i in range(satir_say*9):
        for j in range(sutun_say*9):
            print(iki_boyut[i][j],end="")
        print()
#game processing
def deger_isleme(sira,eleman1,eleman2,eleman3,iki_boyut,oyuncu1,oyuncu2,sayac1,sayac2):
    satir_no = [1, 2, 3, 4, 5, 6, 7]
    sutun_harf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T"]
    dic_guney = {"A": 3, "B": 11, "C": 19, "D": 27, "E": 35, "F": 43, "G": 51, "H": 59, "I": 67, "J": 75, "K": 83,
                 "L": 91, "M": 99, "N": 107, "O": 115, "P": 123, "R": 131, "S": 139, "T": 147}
    dic_dogu = {"A":9,"B":17,"C":25,"D":33,"E":41,"F":49,"G":57,"H":65,"I":73,"J":81,"K":89,"L":97,"M":105,"N":113,"O":121,"P":129,"R":137,"S":145,"T":153}
    dic_bati = {"B": 9, "C": 17, "D": 25, "E": 33, "F": 41, "G": 49, "H": 57, "I": 65, "J": 73, "K": 81, "L": 89,
                "M": 97, "N": 105, "O": 113, "P": 121, "R": 129, "S": 137, "T": 145}
    #eleman3 koordinatları tutar (K:kuzey ,G:Güney, B:Batı,D:Doğu)
    if eleman3 in ["D"]:
        for i in range(eleman1 * 3 - 1, eleman1 * 3 + 2):
            if eleman1 == 0:
                break
            else:
                j = dic_dogu[eleman2]
                iki_boyut[i][j] = "|"
            if iki_boyut[i][j-8]=="|" and iki_boyut[i-2][j-3]=="_" and iki_boyut[i+1][j-3]=="_":
                if sira%2!=0:
                    iki_boyut[eleman1*3][j-4]=oyuncu2
                    sira+=2
                    sayac2+=1
                else:
                    iki_boyut[eleman1 * 3][j - 4] = oyuncu1
                    sira+=2
                    sayac1 += 1

            elif iki_boyut[i][j+8]=="|" and iki_boyut[i-2][j+3]=="_" and iki_boyut[i+1][j+3]=="_":
                if sira%2!=0:
                    iki_boyut[eleman1*3][j+4]=oyuncu2
                    sira+=2
                    sayac2 += 1
                else:
                    iki_boyut[eleman1 * 3][j + 4] = oyuncu1
                    sayac1 += 1
            else:
                sira+=1
    if eleman3 in ["B"]:
        for i in range(eleman1 * 3 - 1, eleman1 * 3 + 2):
            if eleman1 == 0:
                break
            else:
                r = dic_bati[eleman2]
                iki_boyut[i][r]="|"
            if iki_boyut[i][r+8]=="|" and iki_boyut[i-2][r+3]=="_" and iki_boyut[i+1][r+3]=="_":
                if sira%2!=0:
                    iki_boyut[eleman1*3][r+4]=oyuncu2
                    sira+=2
                    sayac2 += 1
                else:
                    iki_boyut[eleman1 * 3][r + 4] = oyuncu1
                    sira+=2
                    sayac1 += 1
            elif iki_boyut[i][r-8]=="|" and iki_boyut[i-2][r-3]=="_" and iki_boyut[i+1][r-3]=="_":
                if sira%2!=0:
                    iki_boyut[eleman1*3][r-4]=oyuncu2
                    sira+=2
                    sayac2 += 1
                else:
                    iki_boyut[eleman1 * 3][r - 4] = oyuncu1
                    sira+=2
                    sayac1 += 1

            else:
                sira+=1
    if eleman3 in ["G"]:
        vedek1=sayac1
        vedek2=sayac2
        u=dic_guney[eleman2]
        for i in range(u,u+5):
            iki_boyut[eleman1*3+1][i]="_"
            if iki_boyut[eleman1*3-2][u]=="_" and iki_boyut[eleman1*3+1][u-2]=="|" and iki_boyut[eleman1*3+1][u+6]=="|":
                if sira%2!=0:
                    iki_boyut[eleman1*3][u+2]=oyuncu1
                    sira+=2
                    sayac1 += 1
                else:
                    iki_boyut[eleman1 * 3][u + 2] = oyuncu2
                    sira+=2
                    sayac2 += 1
            elif iki_boyut[eleman1*3+4][u]=="_" and iki_boyut[eleman1*3+2][u-2]=="|" and iki_boyut[eleman1*3+2][u+6]=="|":
                if sira%2!=0:
                    iki_boyut[eleman1*3+3][u+2]=oyuncu1
                    sira+=2
                    sayac1 += 1
                else:
                    iki_boyut[eleman1 * 3+3][u + 2] = oyuncu2
                    sira+=2
                    sayac2 += 1

            else:
                sira+=1
        if vedek1!=sayac1 :
            sayac1 = sayac1 -4
        if vedek2!=sayac2 :
            sayac2 = sayac2 -4
    if eleman3 in ["K"]:
        t=dic_guney[eleman2]
        yedek1=sayac1
        yedek2=sayac2
        for i in range(t,t+5):
            iki_boyut[eleman1*3-2][i]="_"
            if iki_boyut[eleman1*3+1][t]=="_" and iki_boyut[eleman1*3-1][t-2]=="|" and iki_boyut[eleman1*3-1][t+6]=="|":
                if sira%2!=0:
                    iki_boyut[eleman1*3][t+2]=oyuncu1
                    sira+=2
                    sayac1 += 1
                else:
                    iki_boyut[eleman1 * 3][t + 2] = oyuncu2
                    sira+=2
                    sayac2 += 1
            elif iki_boyut[eleman1*3-5][t]=="_" and iki_boyut[eleman1*3-2][t-2]=="|" and iki_boyut[eleman1*3-2][t+6]=="|":
                if sira%2!=0:
                    iki_boyut[eleman1*3-3][t+2]=oyuncu1
                    sira+=2
                    sayac1 += 1
                else:
                    iki_boyut[eleman1 * 3-3][t + 2] = oyuncu2
                    sira+=2
                    sayac2 += 1

            else:
                sira+=1
        if yedek1!=sayac1 :
            sayac1 = sayac1 -4
        if yedek2!=sayac2 :
            sayac2 = sayac2 -4
    return sira,iki_boyut,oyuncu1,oyuncu2,sayac1,sayac2
def oyun_yazdir(sutun_say, satir_say,iki_boyut):
    oyun_alani(sutun_say, satir_say,iki_boyut)
    for i in range(satir_say*9):
        for j in range(sutun_say*9):
            print(iki_boyut[i][j],end="")
        print()
#display player score
def puan_durumu(oyuncu1,oyuncu2,sayac1,sayac2):
    print("PUAN DURUMU")
    print("-----------")
    print("|",oyuncu1," : ",sayac1," | ")
    print("|",oyuncu2," : ",sayac2," | ")
    print("-----------")

#main function
def main():
    oyuncu1 = input("1. oyuncuyu temsil etmek için büyük harfle bir harf giriniz:")
    while len(oyuncu1) != 1:
        oyuncu1 = input("!!(sadece tek harf giriniz...) 1.oyuncuyu temsil etmek için bir karakter giriniz:")
    while oyuncu1 not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S",
                          "T", "U", "Ü", "V", "Y", "Z", "X", "W", "Q"]:
        oyuncu1 = input("!!(sadece tek harf giriniz...) 1.oyuncuyu temsil etmek için bir karakter giriniz:")
    oyuncu2 = input("2. oyuncuyu temsil etmek için büyük harfle bir harf giriniz:")
    while len(oyuncu2) != 1:
        oyuncu2 = input("!!(sadece tek harf giriniz... 2.oyuncuyu temsil etmek için bir karakter giriniz:")
    while oyuncu2 not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S",
                          "T", "U", "Ü", "V", "Y", "Z", "X", "W", "Q"]:
        oyuncu2 = input("2.oyuncuyu temsil etmek için bir karakter giriniz:")
    satir_say = int(input("oyun alanının satır sayısını giriniz(3-7):"))
    while satir_say < 3 or satir_say > 7:
        satir_say = int(input("!!(Aralıktaki değerlerden birini giriniz)oyun alanının satır sayısını giriniz(3-7):"))
    sutun_say = int(input("oyun alanının sütun sayısını giriniz(3-19):"))
    while sutun_say < 3 or sutun_say > 19:
        sutun_say = int(input("!!(Aralıktaki değerlerden birini giriniz)oyun alanının sütun sayısını giriniz(3-19):"))
    eleman1 = 0
    eleman2 = 0
    eleman3 = 0
    iki_boyut = []
    for i in range(satir_say * 9):
        iki_boyut += [[" "] * (sutun_say * 9)]
    for i in range(satir_say * 9):
        for j in range(sutun_say * 9):
            iki_boyut[i][j] = " "
    sira = 1
    sayac1=0
    sayac2=0
    oyun_yazdir(sutun_say, satir_say,iki_boyut)
    while True:
        if sira % 2 != 0:
            print("oyuncu", oyuncu1, "lütfen tercihinizi giriniz:", end='')
            #example -->  1AD    1:column index ; A:row index  ;  D: coordinate(east)
            deger_alma = input()
            list(deger_alma)
            eleman1 = int(deger_alma[0])
            eleman2 = deger_alma[1]
            eleman3 = deger_alma[2]
            deger_isleme(sira,eleman1,eleman2,eleman3,iki_boyut,oyuncu1,oyuncu2,sayac1,sayac2)
            sira,iki_boyut,oyuncu1,oyuncu2,sayac1,sayac2 = deger_isleme(sira,eleman1,eleman2,eleman3,iki_boyut,oyuncu1,oyuncu2,sayac1,sayac2)
            dizi_yazdir(satir_say,sutun_say,iki_boyut)

            puan_durumu(oyuncu1, oyuncu2, sayac1, sayac2)

        else:

            print("oyuncu", oyuncu2, "lütfen tercihinizi giriniz:", end='')
            deger_alma = input()
            list(deger_alma)
            eleman1 = int(deger_alma[0])
            eleman2 = deger_alma[1]
            eleman3 = deger_alma[2]
            deger_isleme(sira,eleman1,eleman2,eleman3,iki_boyut,oyuncu1,oyuncu2,sayac1,sayac2)
            sira,iki_boyut,oyuncu1,oyuncu2,sayac1,sayac2 = deger_isleme(sira,eleman1,eleman2,eleman3,iki_boyut,oyuncu1,oyuncu2,sayac1,sayac2)
            dizi_yazdir(satir_say,sutun_say,iki_boyut)

            puan_durumu(oyuncu1, oyuncu2, sayac1, sayac2)
    return sutun_say, satir_say, iki_boyut, eleman1,eleman2,eleman3,oyuncu1,oyuncu2,sayac1,sayac2
main()