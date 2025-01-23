# Phonebook

Prosta aplikacja webowa do zarządzania kontaktami, stworzona z użyciem Flask i PostgreSQL.

## Funkcje
- Dodawanie, wyświetlanie, wyszukiwanie i usuwanie kontaktów.

---

## Jak uruchomić

1. **Uruchom bazę danych**:
   ```bash
   docker-compose up -d
   ```

2. **Utwórz środowisko wirtualne**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
   ```

3. **Zainstaluj zależności**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Zainicjalizuj bazę danych**:
   ```bash
   python init-db.py
   ```

5. **Uruchom aplikację**:
   ```bash
   python app.py
   ```

Aplikacja dostępna pod: [http://127.0.0.1:5000](http://127.0.0.1:5000).