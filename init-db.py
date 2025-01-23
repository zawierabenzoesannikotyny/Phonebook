from database import db, app
from models import Contact  # Trzeba zaimportować model, aby SQLAlchemy mógł utworzyć tabelę

with app.app_context():
    print("Tworzenie tabel w bazie danych...")
    db.create_all()  # Tworzy tabelę na podstawie modelu
    print("Tabele zostały pomyślnie utworzone!")