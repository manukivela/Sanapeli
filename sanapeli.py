import random
import pickle
import os
import requests
from bs4 import BeautifulSoup
import re
import random
import hashlib
import getpass

def cleanhtml(raw_html):
    CLEANR = re.compile('<.*?>') 
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


def signup():
    nimi = input("Syötä nimi: ").upper()

    if nimi in accounts:
        print("Nimi käytössä, kirjaudu sisään")
        input('Paina mitä tahansa näppäintä')
        return ""


    pwd = getpass.getpass("Syötä salasana: ")
    conf_pwd = getpass.getpass("Vahvista salasana: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()

        accounts[f'{nimi}'] = hash1

        with open("accounts", "wb") as f:
            pickle.dump(accounts, f)
        f.close()
        print("Rekisteröinti onnistui")
        input("Paina mitä tahansa näppäintä")
    else:
        print("Salasanat ei täsmää")
        print("Rekisteröinty epäonnistui")
        input("Paina mitä tahansa näppäintä")

def login():
    clearConsole()
    print('Kirjaudu sisään \n')
    pelaaja = input("Nimi: ").upper()
    pwd = getpass.getpass("Salasana: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()

    with open('accounts', 'rb') as f:
        accounts = pickle.load(f)
    f.close()
    
    if pelaaja in accounts and auth_hash == accounts[f'{pelaaja}']:
        print("Kirjautuminen onnistui")
        return pelaaja
    else:
        print("Kirjautuminen epäonnistui! \n")
        input('Paina mitä tahansa näppäintä')
        


def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

def SetList(list_, index, value):
    try:
        # Try to input the index into the list
        list_[index] = value
        return list_
    except IndexError:
        # Create new 'None' items into the list for placeholder
        for _ in range(index - len(list_) + 1):
            list_.append(None)
        # Now that the index has been initialized you can set the
        # index the value you want
        list_[index] = value
        return list_

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


with open('sanasto.txt', 'r') as f:
    allWords = [line.strip() for line in f]

kolmoset = []
neloset = []
vitoset = []
kutoset = []
seiskat = []
kasit = []

for i in allWords:
    if len(i) == 3:
        kolmoset.append(i)
    if len(i) == 4:
        neloset.append(i)
    if len(i) == 5:
        vitoset.append(i)
    if len(i) == 6:
        kutoset.append(i)
    if len(i) == 7:
        seiskat.append(i)
    if len(i) == 8:
        kasit.append(i)


def päivänSana(sanapituus=vitoset):
    sana = random.choice(sanapituus)
    return sana


#print(kirjaimet)

def arvauksetisolla(arvaus):
    for i in arvaus:
        print("          ", i.upper())

def vastausisolla(vastaus):
    for i in vastaus:
        print(" ", i.upper(), end=" ")

def alkuprint(pelaaja, vastaus, temp2, temp3, arvaukset, attempt):
    print(f'Pelaaja: {pelaaja} \n')
    vastausisolla(vastaus)
    print('\n\n')
    print('Oikeat kirjaimet: ')
    vastausisolla(temp2)
    print()
    print()
    print('Kokeillut väärät kirjaimet: ')
    vastausisolla(temp3)
    print()
    print()
    print("Arvaukset: ")
    arvauksetisolla(arvaukset)
    print()
    print()
    print(f'Yritys {attempt}/6')
    print()    

def play_wordle():

    oikeaSana = päivänSana()
    kirjaimet = list(oikeaSana)
    #print(oikeaSana)
    bet = 0
    arvaukset = []
    temp3 = []
    temp2 = []
    temp = []
    vastaus = ["-","-","-","-","-"]

    attempt = 0

    # Betting
    if pisteet > 0:
        bet = -1
        print(f'Sinulla on {pisteet} pistettä.')
        if pisteet < 500:
            print(f'Voit panostaa 0-{pisteet}')
            while (bet > pisteet) or (bet < 0):
                bet = int(input('Kuinka paljon haluat panostaa? '))

        if pisteet >= 500:
            while (bet > 500) or (bet < 0):
                print(f'Voit panostaa 0-500')
                bet = int(input('Kuinka paljon haluat panostaa? '))

        data[f'{pelaaja}'] -= bet
        with open('tilastot', 'wb') as f:
            pickle.dump(data, f)
        f.close()



    while attempt < 6:
        clearConsole()
        alkuprint(pelaaja, vastaus, temp2, temp3, arvaukset, attempt)
        while True:
            
            arvaus = input('Arvaus: ').lower()
            
            if len(arvaus) != 5:
                print('Anna viisi kirjainta')
            
            elif arvaus not in allWords:
                    print('Syötä oikea sana')
            else:
                attempt += 1
                arvaukset.append(arvaus)
                arvaus = list(arvaus)
                break

        if arvaus == kirjaimet:
            print('OIKEIN')
            if attempt == 0:
                data[f'{pelaaja}'] += 100
                data[f'{pelaaja}'] += bet
                file = open('tilastot', 'wb')

                # dump information to that file
                pickle.dump(data, file)

                # close the file
                file.close()
            if attempt == 1:
                data[f'{pelaaja}'] += 90
                data[f'{pelaaja}'] += bet
                file = open('tilastot', 'wb')

                # dump information to that file
                pickle.dump(data, file)

                # close the file
                file.close()
            if attempt == 2:
                data[f'{pelaaja}'] += 80
                data[f'{pelaaja}'] += bet
                file = open('tilastot', 'wb')

                # dump information to that file
                pickle.dump(data, file)

                # close the file
                file.close()
            if attempt == 3:
                data[f'{pelaaja}'] += 70
                data[f'{pelaaja}'] += bet
                file = open('tilastot', 'wb')

                # dump information to that file
                pickle.dump(data, file)

                # close the file
                file.close()
            if attempt == 4:
                data[f'{pelaaja}'] += 60
                data[f'{pelaaja}'] += bet
                file = open('tilastot', 'wb')

                # dump information to that file
                pickle.dump(data, file)

                # close the file
                file.close()
            if attempt == 5:
                data[f'{pelaaja}'] += 50
                data[f'{pelaaja}'] += bet
                file = open('tilastot', 'wb')

                # dump information to that file
                pickle.dump(data, file)

                # close the file
                file.close()
            break
        
        temp = []
        
        


        for i in range(len(kirjaimet)):
            if kirjaimet[i] == arvaus[i]:
                temp.append(arvaus[i])
                vastaus = SetList(vastaus, i, arvaus[i])

            elif arvaus[i] in kirjaimet:
                temp.append('-')
                if arvaus[i] not in temp:
                    if arvaus[i] not in temp2:
                        temp2.append(arvaus[i])
            
            elif arvaus[i] not in kirjaimet:
                temp.append('-')
                if arvaus[i] not in temp3:
                    temp3.append(arvaus[i])

            else:
                temp.append('-')
        clearConsole()

        #print(temp)
    alkuprint(pelaaja, vastaus, temp2, temp3, arvaukset, attempt)
    print(f'Oikea sana oli {oikeaSana}!')
    try:
        url = f'https://www.suomisanakirja.fi/{oikeaSana}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        sana_tarkoittaa = soup.findAll('p')[0]
        print(cleanhtml(str(sana_tarkoittaa)[0:500]))
    except:
        pass
    print()

    if attempt > 6:
        data[f'{pelaaja}'] -= 50
        with open('tilastot', 'wb') as f:
            pickle.dump(data, f)
        f.close()
    if data[f'{pelaaja}'] < 0:
        data[f'{pelaaja}'] == 0
        with open('tilastot', 'wb') as f:
            pickle.dump(data, f)
        f.close()

    


if __name__ == "__main__":
    try:
        with open('accounts', 'rb') as f:
            accounts = pickle.load(f)
        f.close
    except FileNotFoundError:
        accounts = {}
        with open('accounts', 'wb') as f:
            pickle.dump(accounts, f)
        f.close()

    try:
        with open('tilastot', 'rb') as f:
            data = pickle.load(f)
        f.close()
    except FileNotFoundError:
        data = {}
        with open('tilastot', 'wb') as f:
            pickle.dump(data, f)
        f.close()


    
    clearConsole()





    while True:
        clearConsole()
        print('TERVETULOA SANAPELIIN!')
        print('1. Kirjaudu sisään')
        print('2. Rekisteröidy')

        x = input()
        if x == "1":
            try:
                pelaaja = login()
                if pelaaja not in data:
                        data[f'{pelaaja}'] = 0
                        # open a file, where you ant to store the data
                        file = open('tilastot', 'wb')

                        # dump information to that file
                        pickle.dump(data, file)

                        # close the file
                        file.close()
                
            except:
                print('Käyttäjää ei löydy')
                print('Paina mitä tahansa näppäintä')
                input()
            finally:
                if pelaaja != None:
                    break

        elif x == "2":
            signup()
        else:
            print('Valitse 1-2')
        

    while True:
        pisteet = data[f'{pelaaja}']
        clearConsole()
        print(f'TERVETULOA {pelaaja}! Sinulla on {pisteet} pistettä!')
        print('(1) Uusi peli')
        print('(2) Tilastot')
        print('(3) Vaihda pelaajaa')
        print('(4) Lopeta')
        x = input('Valitse 1-4: ')
        if x == "4":
            break
        elif x == "3":
            while True:
                clearConsole()
                print('TERVETULOA SANAPELIIN!')
                print('1. Kirjaudu sisään')
                print('2. Rekisteröidy')

                x = input()
                if x == "1":
                    try:
                        pelaaja = login()
                        if pelaaja not in data:
                                data[f'{pelaaja}'] = 0
                                # open a file, where you ant to store the data
                                file = open('tilastot', 'wb')

                                # dump information to that file
                                pickle.dump(data, file)

                                # close the file
                                file.close()
                        
                    except:
                        print('Käyttäjää ei löydy')
                        print('Paina mitä tahansa näppäintä')
                        input()
                    finally:
                        if pelaaja != None:
                            break


                elif x == "2":
                    signup()
                else:
                    print('Valitse 1-2')

        elif x == "2":
            try:
                clearConsole()
                tilastot_sorted = sort_dict_by_value(data, True)
                print('-------------- \n TOP 10 \n--------------  ')
                print('   PISTEET\tNIMI')
                print()
                x = 1
                for i in tilastot_sorted:
                    if tilastot_sorted[i] > 999 or tilastot_sorted[i] < 0:
                        print(f'{x}. {tilastot_sorted[i]} \t{i}')
                    else:
                        print(f'{x}. {tilastot_sorted[i]} \t\t{i}')
                    x += 1
                    if x > 10:
                        break

                print()
                input('Paina mitä tahansa näppäintä')
            except:
                print('Tilastoja ei saatavilla')
                input('Paina mitä tahansa näppäintä')
        elif x == "1":
                
            clearConsole()
            play_wordle()
            
            input('Paina mitä tahansa näppäintä')

        else:
            print('Valitse 1-4')
