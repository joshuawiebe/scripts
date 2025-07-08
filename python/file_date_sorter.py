import os
import shutil
import datetime
from PIL import Image

# Erlaubte Dateiformate für Bilder und Videos
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "bmp", "tiff", "mp4", "mov", "avi", "mkv", "wmv", "flv", "webm"}

def get_file_creation_date(file_path):
    """Gibt das Aufnahmedatum der Datei zurück, falls verfügbar, sonst das Erstellungsdatum."""
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data and 36867 in exif_data:
                return datetime.datetime.strptime(exif_data[36867], "%Y:%m:%d %H:%M:%S").strftime("%Y_%m_%d")
    except Exception:
        pass
    return datetime.datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y_%m_%d")

def move_all_files_to_root(source_folder):
    """Holt alle Dateien aus Unterordnern und verschiebt sie in den Hauptordner."""
    for root, _, files in os.walk(source_folder, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Überprüfen, ob der Ordner 'extracted' ist und den überspringen
                if os.path.isfile(file_path) and root != source_folder and "extracted" not in root:
                    shutil.move(file_path, os.path.join(source_folder, file))
            except PermissionError:
                print(f"Zugriff verweigert: {file_path}")
            except Exception as e:
                print(f"Fehler beim Verschieben von {file_path}: {e}")

def remove_empty_folders(source_folder):
    """Löscht alle leeren Unterordner im Quellordner."""
    for root, dirs, _ in os.walk(source_folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                if not os.listdir(dir_path) and "extracted" not in dir_name:
                    os.rmdir(dir_path)
            except PermissionError:
                print(f"Zugriff verweigert: {dir_path}")
            except Exception as e:
                print(f"Fehler beim Löschen von {dir_path}: {e}")

def sort_files_by_date(source_folder):
    """Sortiert nur Bilder und Videos im angegebenen Ordner nach Aufnahmedatum und erstellt Jahresordner."""
    if not os.path.exists(source_folder):
        print("Der angegebene Ordner existiert nicht.")
        return
    
    move_all_files_to_root(source_folder)
    remove_empty_folders(source_folder)

    # Durchlaufen aller Dateien im Hauptordner
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        file_extension = file_name.lower().split(".")[-1]
        
        if os.path.isfile(file_path) and file_extension in ALLOWED_EXTENSIONS:
            try:
                # Überspringen des 'extracted'-Ordners
                if "extracted" in file_path:
                    continue
                
                creation_date = get_file_creation_date(file_path)
                year = creation_date.split("_")[0]
                year_folder = os.path.join(source_folder, year)  # Ordner für das Jahr

                if not os.path.exists(year_folder):
                    os.makedirs(year_folder)
                
                date_folder = os.path.join(year_folder, creation_date)  # Ordner für das Datum innerhalb des Jahres
                if not os.path.exists(date_folder):
                    os.makedirs(date_folder)
                
                shutil.move(file_path, os.path.join(date_folder, file_name))
            except PermissionError:
                print(f"Zugriff verweigert: {file_path}")
            except Exception as e:
                print(f"Fehler beim Verschieben von {file_path}: {e}")
    
    print("Bilder und Videos wurden erfolgreich nach Jahr und Aufnahmedatum sortiert!")

def main():
    source_folder = input("Geben Sie den Pfad des zu sortierenden Ordners ein: ")
    sort_files_by_date(source_folder)

if __name__ == "__main__":
    main()
