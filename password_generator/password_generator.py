#!/usr/bin/env python3
# Lösenordsgenerator med säkerhetskontroll

import requests
import hashlib
import secrets
import string
import re
import getpass


class LosenordsHanterare:
    # Have I Been Pwned API för att kontrollera läckta lösenord
    API_URL = "https://api.pwnedpasswords.com/range/"
    
    def __init__(self):
        # Skapa session för API-anrop
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'LosenordsHanterare/1.0'})
    
    def kontrolleraa_laecka(self, losenord):
        # Kontrollera om lösenord finns i databas av läckta lösenord
        try:
            # Kryptera lösenordet med SHA-1
            hash_kod = hashlib.sha1(losenord.encode()).hexdigest().upper()
            
            # Skicka bara första 5 tecken (säker metod)
            prefix = hash_kod[:5]
            suffix = hash_kod[5:]
            
            # Fråga API:et
            svar = self.session.get(f"{self.API_URL}{prefix}")
            svar.raise_for_status()
            
            # Sök efter matchning i resultatet
            for rad in svar.text.split('\r\n'):
                if ':' in rad:
                    hash_del, antal = rad.split(':')
                    if hash_del == suffix:
                        return True, int(antal)
            
            return False, 0
            
        except requests.RequestException as e:
            print(f"Kunde inte kontrollera: {e}")
            return False, 0
    
    def kontrollera_styrka(self, losenord):
        # Kontrollera hur stark lösenordet är
        poang = 0
        feedback = []
        
        # Längd
        if len(losenord) >= 8:
            poang += 1
        else:
            feedback.append("För kort (minst 8 tecken)")
        
        if len(losenord) >= 12:
            poang += 1
        else:
            feedback.append("12 tecken eller mer är bättre")
        
        # Små bokstäver
        if re.search(r'[a-z]', losenord):
            poang += 1
        else:
            feedback.append("Lägg till små bokstäver")
        
        # Stora bokstäver
        if re.search(r'[A-Z]', losenord):
            poang += 1
        else:
            feedback.append("Lägg till stora bokstäver")
        
        # Siffror
        if re.search(r'[0-9]', losenord):
            poang += 1
        else:
            feedback.append("Lägg till siffror")
        
        # Specialtecken
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', losenord):
            poang += 1
        else:
            feedback.append("Specialtecken ökar säkerheten")
        
        # Varning för upprepade tecken
        if re.search(r'(.)\1{2,}', losenord):
            feedback.append("Undvik upprepade tecken")
        
        # Varning för sekvenser
        if re.search(r'(012|123|234|345|abc|bcd)', losenord.lower()):
            feedback.append("Undvik sekvenser")
        
        # Bestäm styrka med ANSI-färger
        if poang >= 6:
            styrka = "Mycket stark"
            farg = "\033[92m"  # Grön
        elif poang >= 5:
            styrka = "Stark"
            farg = "\033[92m"  # Grön
        elif poang >= 4:
            styrka = "Medel"
            farg = "\033[93m"  # Gul
        else:
            styrka = "Svag"
            farg = "\033[91m"  # Röd
        
        reset = "\033[0m"  # Återställ färg
        
        return {
            'styrka': styrka,
            'farg': farg,
            'reset': reset,
            'poang': poang,
            'max': 6,
            'feedback': feedback
        }
    
    def generera_losenord(self, langd=16):
        # Generera ett slumpmässigt säkert lösenord
        if langd < 8:
            langd = 8
        
        # Använd bokstäver, siffror och specialtecken
        tecken = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}:;<>?,./"
        
        # Skapa lösenord
        losenord = ''.join(secrets.choice(tecken) for _ in range(langd))
        return losenord
    
    def generera_flera(self, antal=5, langd=16):
        # Generera flera lösenord på en gång
        return [self.generera_losenord(langd) for _ in range(antal)]
    
    def analysera(self, losenord):
        # Gör fullständig analys av lösenord
        print(f"\n{'='*60}")
        print("Analyserar lösenord...")
        print(f"{'='*60}\n")
        
        # Kontrollera läcka
        ar_laeckt, antal = self.kontrolleraa_laecka(losenord)
        
        if ar_laeckt:
            print(f"VARNING: Lösenordet har läckt!")
            print(f"Funnet i {antal} databaskränkningar.")
            print("Du BÖR byta det!\n")
        else:
            print("Lösenordet finns inte i kända läckor.\n")
        
        # Kontrollera styrka
        info = self.kontrollera_styrka(losenord)
        
        print(f"Styrka: {info['farg']}{info['styrka']}{info['reset']}")
        print(f"Poäng: {info['poang']}/{info['max']}\n")
        
        if info['feedback']:
            print("Förslag:")
            for tips in info['feedback']:
                print(f"  - {tips}")
        
        print()


def main():
    # Huvudprogram
    hanterare = LosenordsHanterare()
    
    while True:
        print("\n" + "="*60)
        print("LÖSENORDSHANTERARE")
        print("="*60)
        print("\n1. Kontrollera lösenord (synligt)")
        print("2. Kontrollera lösenord (dolt)")
        print("3. Generera nytt lösenord")
        print("4. Generera flera förslag")
        print("5. Avsluta\n")
        
        val = input("Välj (1-5): ").strip()
        
        if val == "1":
            # Kontrollera lösenord (synligt)
            losenord = input("\nAnge lösenord: ")
            if losenord:
                hanterare.analysera(losenord)
            else:
                print("Ingen inmatning!")
        
        elif val == "2":
            # Kontrollera lösenord (dolt)
            losenord = getpass.getpass("\nAnge lösenord (syns inte): ")
            if losenord:
                hanterare.analysera(losenord)
            else:
                print("Ingen inmatning!")
        
        elif val == "3":
            # Genererar ett lösenord
            try:
                langd = input("\nLösenordslängd (standard 16): ").strip()
                langd = int(langd) if langd else 16
                
                nytt = hanterare.generera_losenord(langd)
                info = hanterare.kontrollera_styrka(nytt)
                
                print(f"\nLösenord: {nytt}")
                print(f"Styrka: {info['farg']}{info['styrka']}{info['reset']}\n")
                
            except ValueError:
                print("Ogiltig längd!")
        
        elif val == "4":
            # Generera flera lösenord
            try:
                antal = input("\nAntal förslag (standard 5): ").strip()
                antal = int(antal) if antal else 5
                langd = input("Lösenordslängd (standard 16): ").strip()
                langd = int(langd) if langd else 16
                
                losenord_lista = hanterare.generera_flera(antal, langd)
                
                print(f"\nLösenordsförslag:\n")
                for i, pwd in enumerate(losenord_lista, 1):
                    info = hanterare.kontrollera_styrka(pwd)
                    print(f"{i}. {pwd}")
                    print(f"   Styrka: {info['farg']}{info['styrka']}{info['reset']}\n")
                
            except ValueError:
                print("Ogiltiga värden!")
        
        elif val == "5":
            print("Ha det!")
            break
        
        else:
            print("Ogiltigt val!")


if __name__ == "__main__":
    main()