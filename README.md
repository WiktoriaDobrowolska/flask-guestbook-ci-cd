# 📘 **Guestbook** – Wiktoria i Marta

**Guestbook** to prosta aplikacja internetowa, stworzona przy użyciu **Flask** i **MySQL**.  
Umożliwia użytkownikom wpisywanie swojego imienia oraz wiadomości, które następnie wyświetlają się poniżej formularza.

---

## Spis treści

- [Funkcjonalności](#funkcjonalność)  
- [Wymagania](#wymagania)  
- [Instalacja](#instalacja)  
- [Uruchamianie aplikacji](#uruchamianie-aplikacji)  
- [Testowanie](#testowanie)  
---

## Funkcjonalność

- 📝 Formularz do wpisywania **imienia** i **wiadomości**  
- 📜 Wyświetlanie listy wpisów z imionami i wiadomościami  
- 💾 Dane przechowywane w bazie **MySQL**    
- 🚀 Integracja z GitHub Actions (CI)  

---

## Wymagania

- Python 3.8 lub nowszy  
- pip  
- MySQL (lokalnie lub w kontenerze Docker)  
- virtualenv (opcjonalnie)  
- Docker (jeśli chcesz uruchomić bazę w kontenerze)  

---

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone git@github.com:twoja_nazwa/myapp.git
cd myapp
```
2. Zainstaluj zależność:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Uruchom MySQL w Dockerze:
   
```bash
docker run --name myapp-mysql -e MYSQL_ROOT_PASSWORD=rootpassword -e MYSQL_DATABASE=myapp -p 3306:3306 -d mysql:latest
```
4. Stwórz plik .env i skonfiguruj go.
5. Uruchom aplikację:
   
```bash
export FLASK_APP=app.py      
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5001
```

---

## Instalacja z Dockerem

Aby ułatwić uruchomienie aplikacji razem z bazą danych, dołączony jest plik `docker-compose.yml`, który automatycznie zbuduje i odpali wszystkie potrzebne usługi w trybie produkcyjnym.

1. Upewnij się, że masz zainstalowane i działające **Docker** oraz **Docker Compose**.

2. Utwórz plik `.env` na podstawie `.env.example` i skonfiguruj w nim zmienne środowiskowe.

3. W terminalu przejdź do katalogu, w którym znajduje się plik `docker-compose.yml` (np. katalog `app`):

   ```bash
   cd app
   ```

4. Uruchom aplikację i bazę danych poleceniem:

   ```bash
   docker-compose up --build
   ```

Po wykonaniu tych kroków aplikacja będzie dostępna pod adresem `http://localhost:5001`.

---
## Testowanie

Aby uruchomić testy aplikacji, wykonaj w terminalu następujące polecenie:

```bash
pytest
```

Upewnij się, że masz aktywne środowisko wirtualne (`venv`) i zainstalowane wszystkie zależności przed uruchomieniem testów.

---



