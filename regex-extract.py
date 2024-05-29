import re

text = """
Inhalte

Das Modul umfasst die für die Studierenden grundlegende Haupteinführungsveranstaltung "System Erde" sowie 5 Tage Geländeübung.
In "System Erde" werden grundlegende geowissenschaftliche Konzepte einführend vorgestellt und die Verbindungen zwischen den Einzeldisziplinen betont. Die Studierenden lernen den Planeten Erde, seine Entwicklungsgeschichte, aber auch notwendige geowissenschaftliche Konzepte und Begriffe kennen. Durch einfache Übungen im Selbststudium können Studierende die Lerninhalte aktiv festigen, während ein Tutorium weitere Hilfestellung bietet.
In den 5 Geländetagen aus dem Angebot an geologischen Anfänger*innen-Geländeübungen lernen die Studierenden die Grundprinzipien der geowissenschaftlichen Geländearbeit kennen. Im Gelände werden so Prinzipien der Stratigraphie, der Gesteinserkennung und von 3D-Strukturen verknüpfend eingeführt.
Lernergebnisse / Kompetenzziele

In diesem Modul erlernen die Studierenden die Grundprinzipien der Geowissenschaften und praktizieren diese im Rahmen von ersten Geländeübungen. Dadurch werden die Grundlagen für alle weiteren geowissenschaftlichen Lehrveranstaltungen - sowohl theoretisch als auch praktisch - sichergestellt.
Die Inhalte umfassen unter anderem die Entstehung von Sonnensystem und Erde, Zusammensetzung, Schalenbau und Bausteine der Erde, Plattentektonik als übergreifendes Konzept, geologische Zeit und ihre Bestimmung, Entwicklung des Lebens und Evolution, Erosion und Sedimentation. Die Wechselwirkungen und Rückkopplungsmechanismen zwischen den diversen Sphären sowie die zeitliche Entwicklung des Planeten Erde sollen die Neugier auf weiterführende Lehrveranstaltungen wecken.
Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls

-
Empfohlene Voraussetzungen
"""

pattern = re.compile(r'(?<=Inhalte)(.*?)(?=Empfohlene Voraussetzungen)', re.DOTALL)
match = pattern.search(text)

if match:
    extracted_text = match.group(1).strip()
    print(extracted_text)
else:
    print("No match found")
