import os
import shutil
from datetime import datetime

# Configuración de carpetas por tipo de archivo
FOLDERS_BY_TYPE = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Vídeos": [".mp4", ".avi", ".mov", ".mkv"],
    "Audios": [".mp3", ".wav", ".aac"],
    "Archivos comprimidos": [".zip", ".rar", ".7z", ".tar.gz"],
    "Otros": [],
}

def select_folder():
    """Solicita al usuario ingresar la ruta de la carpeta a analizar."""
    folder_path = input("Ingrese la ruta de la carpeta que desea analizar: ").strip()
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"La carpeta '{folder_path}' no existe. Verifica la ruta.")
    return folder_path

def select_categories():
    """Permite al usuario seleccionar las categorías de archivos a organizar."""
    print("Seleccione las categorías que desea organizar (separelas por comas):")
    for index, category in enumerate(FOLDERS_BY_TYPE.keys(), start=1):
        print(f"{index}. {category}")
    
    selected_indices = input("Ingrese los números de las categorías: ").strip().split(",")
    selected_categories = []
    
    for index in selected_indices:
        try:
            category = list(FOLDERS_BY_TYPE.keys())[int(index) - 1]
            selected_categories.append(category)
        except (IndexError, ValueError):
            print(f"'{index}' no es una opción válida. Ignorando.")
    
    if not selected_categories:
        raise ValueError("Debe seleccionar al menos una categoría.")
    
    return selected_categories

def select_target_folder(selected_categories):
    """Permite al usuario seleccionar el nombre de la carpeta de destino para cada categoría de archivos."""
    print("\nPara cada tipo de archivo seleccionado, se pedirá un nombre de carpeta de destino.")
    target_folders = {}
    
    for category in selected_categories:
        folder_name = input(f"Ingrese el nombre de la carpeta para '{category}' (deje en blanco para usar el nombre predeterminado): ").strip()
        if not folder_name:
            folder_name = category
        target_folders[category] = folder_name
    
    return target_folders

def organize_files(folder_path, selected_categories, organize_by_month, filter_words, backup_folder, target_folders):
    """Organiza los archivos en la carpeta según las categorías seleccionadas."""
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            # Filtrar por palabras clave
            if filter_words and not any(word.lower() in item.lower() for word in filter_words):
                continue
            
            _, ext = os.path.splitext(item)
            for category in selected_categories:
                if ext.lower() in FOLDERS_BY_TYPE[category]:
                    # Obtener la carpeta de destino seleccionada
                    target_folder_name = target_folders.get(category, category)
                    target_folder = os.path.join(folder_path, target_folder_name)

                    # Ordenar por mes si está habilitado
                    if organize_by_month:
                        creation_time = os.path.getctime(item_path)
                        month = datetime.fromtimestamp(creation_time).strftime("%B-%Y")
                        target_folder = os.path.join(target_folder, month)
                    
                    # Crear respaldo antes de mover
                    if backup_folder:
                        backup_path = os.path.join(backup_folder, item)
                        shutil.copy2(item_path, backup_path)
                    
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(item_path, os.path.join(target_folder, os.path.basename(item_path)))
                    print(f"Moviendo '{item}' a '{target_folder}'")
                    break
            else:
                if "Otros" in selected_categories:
                    other_folder = os.path.join(folder_path, "Otros")
                    os.makedirs(other_folder, exist_ok=True)
                    shutil.move(item_path, os.path.join(other_folder, os.path.basename(item_path)))
                    print(f"Moviendo '{item}' a '{other_folder}'")

def main():
    try:
        print("=== Organizador de Archivos ===")
        folder_path = select_folder()
        selected_categories = select_categories()

        # Opciones adicionales
        organize_by_month = input("¿Desea organizar los archivos por meses? (s/n): ").strip().lower() == "s"
        filter_words = input("Ingrese palabras clave para filtrar archivos (separadas por comas) o presione Enter para omitir: ").strip()
        filter_words = [word.strip() for word in filter_words.split(",")] if filter_words else None
        backup_folder = input("Ingrese una carpeta para respaldo o presione Enter para omitir: ").strip()
        
        if backup_folder:
            os.makedirs(backup_folder, exist_ok=True)
        
        # Selección de carpetas de destino
        target_folders = select_target_folder(selected_categories)
        
        organize_files(folder_path, selected_categories, organize_by_month, filter_words, backup_folder, target_folders)
        print("Organización completada.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
