# Lösenordsgenerator



En enkel Python-applikation för att kontrollera lösenordssäkerhet och generera säkra lösenord.

---

## Syfte/Mål

Syftet med projektet är att:
- Kontrollera om lösenord har läckt mot Have I Been Pwned-databasen
- Analysera och bedöma lösenordsstyrka med detaljerad feedback
- Generera säkra slumpmässiga lösenord enligt best practices
- Tillhandahålla dold lösenordsinmatning för privat miljö
- Demonstrera användning av API-integration och säker hantering i Python

Applikationen är **enbart läs- och kontrollbaserad** och gör inga ändringar i systemet.

---

## Funktionalitet

Applikationen utför följande:

### 1. Lösenordskontroll
- **Läckakontroll** - Jämför lösenord mot Have I Been Pwned-databasen med k-anonymity
- **Styrkeanalys** - Bedömer lösenordsstyrka baserat på:
  - Längd (8-12+ tecken)
  - Stora och små bokstäver
  - Siffror och specialtecken
  - Varningar för sekvenser och upprepningar
- **Färgfeedback** - Visuell återkoppling:
  - 🔴 Röd (Svag)
  - 🟡 Gul (Medel)
  - 🟢 Grön (Mycket stark)

### 2. Lösenordsgenerering
- Skapa slumpmässiga säkra lösenord
- Valfri längd (standard 16 tecken)
- Generera flera förslag på en gång
- Använder `secrets`-modulen för kryptografisk slumpmässighet

### 3. Säkerhet
- **K-anonymity** - Endast första 5 tecknen av hash skickas till API
- **Ingen lagring** - Lösenord lagras aldrig på disk
- **Dold inmatning** - Lösenord syns inte när du skriver

---

## Systemkrav

### Operativsystem
- **Linux, macOS eller Windows**
- Python 3.6 eller senare

### Beroenden
- `requests` (för Have I Been Pwned API)
- Installeras via `pip install -r requirements.txt`

### Behörigheter
- Normala användarrättigheter räcker
- Internet-anslutning krävs för läckakontroll

---

## Installation

### Rekommenderad installation

```bash
# Klona eller ladda ner projektet
git clone https://github.com/daneljs/egna-projekt/password_generator.git
cd password_generator

# Installera beroenden
pip install -r requirements.txt

# Kör applikationen
python password_generator.py
```

---

##  Användning

### Starta applikationen

```bash
python password_manager.py
```

### Visa hjälptext

```bash
python password_manager.py --help
```

### Menyalternativ

| Val | Beskrivning |
|-----|-------------|
| 1 | Kontrollera lösenord (synligt) |
| 2 | Kontrollera lösenord (dolt) - Ingen ser vad du skriver |
| 3 | Generera nytt lösenord |
| 4 | Generera flera lösenordsförslag |
| 5 | Avsluta |

### Exempel på körning

```
LÖSENORDSHANTERARE
============================================================

1. Kontrollera lösenord (synligt)
2. Kontrollera lösenord (dolt)
3. Generera nytt lösenord
4. Generera flera förslag
5. Avsluta

Välj (1-5): 1

Ange lösenord: MySecurePass123!

Analyserar lösenord...
============================================================

Lösenordet finns inte i kända läckor.

Styrka: Mycket stark
Poäng: 6/6

Förslag:
  - Undvik upprepade tecken
```

### Exempel - Generera lösenord

```
Välj (1-5): 3

Lösenordslängd (standard 16): 20

Lösenord: k$9mP#vL2qX@wRt5yB8nJ
Styrka: Mycket stark
```

---

##  Loggning

All aktivitet kan loggas beroende på systemkonfiguration.

**Viktigt:** Have I Been Pwned API lagrar inte dina lösenord eller sökningar tack vare k-anonymity-principen.

---

##  Säkerhetsinformation

### K-anonymity Princip
- Lösenordet hashas lokalt med SHA-1
- Endast första 5 tecknen av hashen skickas till API
- Möjligheten för API:et att se ditt fullständiga lösenord är virtuellt omöjlig
- Läs mer: [Have I Been Pwned - Search Safely](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange)

### Lösenordsgenerering
- Använder `secrets`-modulen för kryptografisk slumpmässighet
- Inte samma som `random` - säkrare för känsliga data
- Kombinerar bokstäver, siffror och specialtecken

### Lokal Behandling
- Ingen inmatad data lagras
- Analyser sker lokalt på din dator
- Endast hash-prefix skickas till Have I Been Pwned

---

## Lösenordstips

### Gör detta
- Använd minst 12-16 tecken
- Blanda stora och små bokstäver
- Lägg till siffror (0-9)
- Lägg till specialtecken (!@#$%^&*)
- Använd unikt lösenord för varje tjänst
- Använd en lösenordshanterare för att spara dem

### Undvik detta
- Ord eller namn
- Datum (födelsedag, årtal)
- Sekvenser (123, abc, qwerty)
- Upprepade tecken (aaaa, 1111)
- Användarnamn eller mejladress
- Samma lösenord på flera sajter

---

##  Bidra

Bidrag är välkomna! För att bidra:

1. Forka projektet
2. Skapa en feature branch (`git checkout -b feature/AmazingFeature`)
3. Committa dina ändringar (`git commit -m 'Add some AmazingFeature'`)
4. Pusha till branchen (`git push origin feature/AmazingFeature`)
5. Öppna en Pull Request

---

##  Felhantering

Applikationen hanterar fel på följande sätt:

- **Ingen internetanslutning** - Meddelar att API-kontroll inte är möjlig
- **Ogiltig inmatning** - Visar felmeddelande och ber om nya försök
- **API-fel** - Loggar fel men fortsätter med lokal analys

---

##  Licens

Detta projekt är gjort i utbildningssyfte


---

##  Resurser

- [Have I Been Pwned API](https://haveibeenpwned.com/API/v3)
- [OWASP Password Guidelines](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Python Getpass Module](https://docs.python.org/3/library/getpass.html)
- [Python Requests Library](https://docs.python-requests.org/)

---

