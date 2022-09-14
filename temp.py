def writeToFile(listToWrite):
    l = open('test.txt', 'w')
    for z in listToWrite:
        if ('\n' not in str(z)):
            l.write(str(z) + ';')
        else:
            l.write(str(z))
    l.close()


def menu(lijst):
    print('Kies hier uw optie die u wilt kiezen:\n'
          '1: Kluis toevoegen\n'
          '2: Kluis openen\n'
          '3: Kluis teruggeven\n'
          '4: Kijken hoeveel kluizen er vrij zijn\n'
          '5: exit')
    opdracht = int(input('Vul hier het getal in van de opdracht die u wilt uitvoeren:'))

    match opdracht:
        case 1:
            print('Deze kluisnummers zijn in gebruik:')
            for j in lijstfreenumbers:
                print(j)
            nummer = int(input('Vul hier uw kluisnummer in:'))
            print('De code moet minimaal 4 characters hebben en mag geen ; bevatten')
            code = input('Vul hier uw code in:')
            lijst = addKluis(lijst, nummer, code)
            writeToFile(lijst)
            menu(lijst)
        case 2:
            nummer = int(input('Vul hier uw kluisnummer in:'))
            code = input('Vul hier uw code in:')
            kluisOpenen(lijst, nummer, code)
            menu(lijst)
        case 3:
            print('Weet u zeker dat u uw kluis terug wil geven?')
            nummer = int(input('Zo ja, vul dan hier uw nummer in:'))
            code = input('En hier uw code:')
            lijst = kluisTeruggeven(lijst, nummer, code)
            writeToFile(lijst)
            menu(lijst)
        case 4:
            print('Er zijn nog ' + str(aantalKluizenVrij(lijst)) + ' kluizen vrij\n')
            menu(lijst)
        case 5:
            exit()


def kluisTeruggeven(lijst, nummer, code):
    county = 0
    for n in lijst:
        if(county % 2 == 0):
            if(n == str(nummer)):
                if(lijst[county + 1].rstrip() == code):
                    print('U heeft uw kluis succesvol teruggegeven!\n')
                    lijst.pop(county)
                    lijst.pop(county)
                    return lijst
                else:
                    print('Dat is niet de juiste code!\n')
                    break
            elif(county == (len(lijst) - 2)):
                print('Die kluis bestaat niet!\n')
                break
            else:
                county += 1
        else:
            county += 1
            continue

def addKluis(kluizenLijst, nummer, code):
    counter = 0
    codeOk = False
    if (len(code) < 4 or ';' in code):
        print('Code is te kort of heeft een ;\n')
    else:
        codeOk = True

    for y in kluizenLijst:
        if (counter % 2 == 0):
            if (y == str(nummer)):
                print('Dat nummer kluis is al bezet, probeer een andere\n')
                break
            else:
                if (codeOk and counter == (len(kluizenLijst)) - 2):
                    lijstfreenumbers.append(str(nummer))
                    kluizenLijst.append(str(nummer))
                    kluizenLijst.append(code + '\n')
                    print('Uw kluis is toegevoegd!\n')
                    break
                else:
                    counter += 1
        else:
            counter += 1
            continue

    return kluizenLijst

def kluisOpenen(lijst, nummer, code):
    count = 0
    for m in lijst:
        if(count % 2 == 0):
            if(m == str(nummer)):
                if(lijst[count + 1].rstrip() == code):
                    print('Welkom in uw kluis!\n')
                    return True
                else:
                    print('Dat is niet de goede code!\n')
                    return False
            elif(count == len(lijst) - 2):
                print('Dat nummer bestaat nog niet!\n')
                return False
            else:
                count += 1
        else:
            count += 1
            continue

def aantalKluizenVrij(lijst):
    return int(12 - (len(lijst) / 2))



f = open('test.txt', 'r')
content = f.readlines()
f.close()
newlist = []
lijstfreenumbers = []
for x in content:
    temp = x.split(';')
    newlist.append(temp[0])
    lijstfreenumbers.append(temp[0])
    newlist.append(temp[1])
content = newlist
menu(content)