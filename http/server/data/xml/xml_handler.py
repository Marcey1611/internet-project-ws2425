import os

file_path = "/data/xml/data.xml"

def get_data():
    try:
        # Datei öffnen und Inhalt lesen
        with open(os.getcwd() + file_path, "r", encoding="utf-8") as file:
            data = file.read()
        return data
    except Exception as e:
        raise e