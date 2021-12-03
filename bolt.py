


class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    def __init__(self):
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """
        pass

    def feladat_1(self, filepath: str) -> None:
        """
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        while True:
            try:
                vsz = int(input('Adja meg egy vásárlás sorszámát! '))
                if vsz < 1 or vsz > len(vasarlasok):
                    print('1-{} közötti számot kérek!'.format(len(vasarlasok)))
                else:
                    break
            except ValueError:
                print('Nem jó!')

    def feladat_2(self) -> None:
        """
        Kiírja, hányan fizettek a pénztárnál.
        """
        while True:
            aru_neve = (input('Adja meg egy árucikk nevét! '))
            if aru_neve not in aru:
                print('Ilyen árut nem vásároltak')
            else:
                break

    def feladat_3(self) -> None:
        """
        Bekéri egy vásárlás sorszámát és kiírja:
            - hány darab árucikk volt a kosárban,
            - mely árucikkekből és milyen mennyiségben vásároltak,
            - a vásárlás összegét.
        """
        while True:
            try:
                vdb = int(input('Adja meg a vásárolt darabszámot! '))
                if vdb < 1 or vdb > 20:
                    print('1-20 közötti számot kérek!')
                else:
                    break

    def feladat_4(self) -> None:
        """
        Bekéri egy árucikk nevét és kiírja:
            - melyik vásárlásnál vettek először a termékből
            - melyik vásárlásnál vettek utoljára a termékből
            - összesen hány alkalommal vásároltak a termékből
        """
        eloszor = 0
        utoljara = 0
        v_alkalom = 0
        for i in range(len(vasarlasok)):
            if vasarlasok[i].count(aru_neve) > 0:
                utoljara = i
                if eloszor == 0:
                    eloszor = i
                v_alkalom += 1

    def feladat_5(self, filepath: str) -> None:
        """
        Elmenti a megadott fájlba a vásárlásonként fizetendő összeget.
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """
        print('%d vásárlás során vettek belőle.' %v_alkalom)
