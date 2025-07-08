import os
import shutil

# Liste der Bild- und Videoformate, die nicht extrahiert werden sollen
excluded_extensions = ['.png', '.jpeg', '.jpg', '.gif', '.bmp', '.tiff', '.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv', '.wmv']

def get_files_to_extract(folder_path):
    files_to_extract = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            # Wenn die Datei keine der ausgeschlossenen Erweiterungen hat, füge sie zur Liste hinzu
            if file_extension not in excluded_extensions:
                files_to_extract.append(os.path.join(root, file))
    return files_to_extract

def extract_files(source_folder):
    # Erstelle den Zielordner "extracted", wenn er nicht existiert
    extracted_folder = os.path.join(source_folder, 'extracted')
    if not os.path.exists(extracted_folder):
        os.makedirs(extracted_folder)
    
    # Alle zu extrahierenden Dateien finden
    files_to_extract = get_files_to_extract(source_folder)

    # Dateien verschieben
    for file_path in files_to_extract:
        # Zielpfad für die Datei
        target_path = os.path.join(extracted_folder, os.path.basename(file_path))
        
        # Verschiebe die Datei
        shutil.move(file_path, target_path)
        print(f"Verschoben: {file_path} -> {target_path}")

def main():
    # Benutzer nach dem Ordner fragen
    source_folder = input("Bitte gib den Pfad des Ordners an, der durchsucht werden soll: ")
    
    # Überprüfen, ob der angegebene Ordner existiert
    if not os.path.exists(source_folder):
        print(f"Der angegebene Ordner {source_folder} existiert nicht.")
        return
    
    # Extrahiere die Dateien
    extract_files(source_folder)
    print("Alle Dateien wurden extrahiert.")

if __name__ == "__main__":
    main()
