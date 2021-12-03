print("1.feladat")
fv = open('kosar.txt', 'r')
vasarlasok = []
termekek = []
F_db = 0
i = 0
aru = set()
for sor in fv:
    sor = sor.rstrip()

    if sor != 'F':
        aru.add(sor)
        termekek[i] = sor
        i += 1
    else:
        F_db += 1
        termekek = sorted(termekek)
        vasarlasok.append(termekek)
        termekek = []
        i = 0
fv.close()

print("2.feladat")
print('A fizetések száma:', F_db)

print("3.feladat")
while True:
     try:
          vsz=int(input('Adja meg egy vásárlás sorszámát! '))
          if vsz<1 or vsz>len(vasarlasok):
               print('1-{} közötti számot kérek!'.format(len(vasarlasok)))
          else:
               break
     except ValueError:
          print('Nem jó!')

while True:
    aru_neve=(input('Adja meg egy árucikk nevét! '))
    if aru_neve not in aru:
        print('Ilyen árut nem vásároltak')
    else:
        break

while True:
     try:
          vdb=int(input('Adja meg a vásárolt darabszámot! '))
          if vdb<1 or vdb>20:
               print('1-20 közötti számot kérek!')
          else:
               break
     except ValueError:
          print('Nem jó!')

eloszor=0
utoljara=0
v_alkalom=0
for i in range(len(vasarlasok)):
    if vasarlasok[i].count(aru_neve)>0:
        utoljara=i
        if eloszor==0:
            eloszor=i
        v_alkalom+=1

print('Az első vásárlás sorszáma: ', eloszor+1)
print('Az utolsó vásárlás sorszáma: ', utoljara+1)
print('%d vásárlás során vettek belőle.' %v_alkalom)

def vizsgalat78(index,iras):
    vizsg=vasarlasok[index]
    osszeg=0
    db=1
    i=1
    while vizsg[i-1]!='{':
        if vizsg[i]==vizsg[i-1]:
            db+=1
        else:
            if iras:
                print(db, vizsg[i-1])
            osszeg+=ertek(db)
            db=1
        i+=1
    return osszeg

vizsgalat78(vsz-1,True)


print("4.feladat")
arucikk = input("Kérem az árucikk nevét: ")
eloszor=0
utoljara=0
v_alkalom=0
for i in range(len(vasarlasok)):
    if vasarlasok[i].count(aru_neve)>0:
        utoljara=i
        if eloszor==0:
            eloszor=i
        v_alkalom+=1
print('Az első vásárlás sorszáma: ', eloszor+1)
print('Az utolsó vásárlás sorszáma: ', utoljara+1)
print('%d vásárlás során vettek belőle.' %v_alkalom)

print("5.feladat")
fki=open('osszeg.txt','w')
for i in range(len(vasarlasok)):
    print('%d: %d' %(i+1,vizsgalat78(i,False)),file=fki)
fki.close()

