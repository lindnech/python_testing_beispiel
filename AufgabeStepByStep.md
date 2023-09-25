Setup: (Wie im Unterricht Schritt 1-4)
Schritt 1

1 Docker Container mit python3, python3-pip, pipx, pytest:

docker run -p 8080:8080 -p 50000:50000 -d -v jenkins-data:/var/jenkins_home jenkins/jenkins:latest
docker exec -it -u 0 ContainerID /bin/bash
apt-get update
apt-get install python3
apt-get install python3-pip
apt-get install pipx
pipx install pytest
exit

Falls die Befehle einen Permission Denied Fehler werfen hast du im Unterricht 2 mal nicht aufgepasst ;D

Schritt 2
Falls ihr euren alten Docker Container verwendet, bitte nur Master Knoten verwenden:
Dashboard -> Jenkins Verwalten -> Master -> Konfigurieren -> "Anzahl der Build-Prozessoren" auf mehr als 0 setzen.

Schritt 3
GitHub Repo mit Beispiel-Test Forken und Clonen:
https://github.com/16uhrpasing/python_testing_beispiel/tree/main

Schritt 4
Multibranch Pipeline mit GitHub Token einrichten. (Jede Minute Git Checken)

Schritt 5
Scan Repository Log von eurer Pipeline Screenshotten (man muss EURE repository im Screenshot erkennen können)

Schritt 6: Neues Python Script mit Tests:
Füge die neuen Python Scripte "programm.py" und "test_programm.py" hinzu. Diese sollen folgende Funktionen implementieren und für jede dieser Funktionen mindestens einen sinnvollen Test ausführen. Pushe diese auf deine Repo!

"plusmal(x,y)" : addiere x und y und multipliziere das Ergebnis mit 2
z.B. plusmal(2,3) = (2+3)*2

"unterschreiben(x) :" füge einem String dem wert "_unterschrieben" hinzu.
z.B. unterschreiben("test") : "test_unterschrieben"

"kubieren(x)": multipliziere x 3-mal mit sich selbst.
z.B. kubieren(2) = 8
kubieren(3) = 27

Neuen Screenshot von Scan Repository Log zur Abgabe hinzufügen.
Füge deinen GitHub-Repo-Fork-Link zur Abgabe hinzu, sonst nicht bewertbar.

Schritt 7: Selenium Recherche:
Füge deinem Git Repo eine "Selenium.txt" hinzu, in der kurz theoretisch erklärt wird, was Selenium ist und wie es sinnvoll in einer Jenkins Pipeline verwendet werden kann.