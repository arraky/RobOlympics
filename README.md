# RobOlympics Line Follower
## Organisation und Prozess
### Ziel
Ziel des Linienfolgers ist es, einer schwarzen Linie zu folgen, bis er zum Ziel kommt. Die Strecke wird am Morgen des Wettkampfs festgelegt und besteht aus folgenden Elementen:
![Streckenelemente](/Images/Streckenelemente.png)  
Die Strecke am Wettkampf sah dann so aus:
![Strecke](/Images/strecke.jpg)  
Wie man sieht, gibt es auch eine Rampe, welche als Abkürzung dient.
### Regeln
1. Der Roboter darf die maximale Grösse von 20 cm x 25 cm x 25 cm (B x L x H) nie überschreiten.
2. Greift ein Teilnehmer vor dem Erreichen der Zielposition in das Spiel ein, wird der Wertungslauf abgebrochen.
3. Sieger ist, wer den Parcours in der kürzesten Zeit durchfahren ist.
4. Ein Abkürzen oder direktes Anfahren des Ziels ist nicht erlaubt. Der Roboter muss der Linie folgen.

## Entwurf
Für den Roboter brauchen wir zwei mittlere Sensoren, die prüfen, ob der Roboter immer noch auf der Linie ist und auf jeder Seite einen äusseren Sensor, um engere Kurven frühzeitig zu entdecken.  
Der restliche Aufbau haben wir je nach Sensorplatzierung verändert, um den Grössenanforderungen gerecht zu werden.  
  
Im Code müssen wir das Verhalten für jede mögliche Sensorkombination einprogrammieren. Eine 1 steht für das Erkennen einer schwarzen Linie, eine 0 steht für das Nichterkennen einer schwarzen Linie, also weiss:  
- 0000 -> nichts
- 1000 -> langsamer, Rotation links
- 0100 -> gleichschnell, leicht links lenken
- 1100 -> stehenbleiben, 90° links (für über Rampe)
- 0010 -> gleichschnell, leicht rechts lenken
- 1010 -> nichts
- 0110 -> gerade aus
- 1110 -> stehenbleiben, 90° links (für über Rampe)
- 0001 -> langsamer, Rotation rechts
- 1001 -> nichts
- 0101 -> nichts
- 1101 -> nichts
- 0011 -> nichts
- 1011 -> nichts
- 0111 -> nichts
- 1111 -> stehenbleiben, 90° rechts (T-Kreuzung von unten, nicht über Rampe)  

Wird bei einem Sensorzustand ein Verhalten festgelegt, wird es so lange fortgeführt, bis es durch einen anderen Sensorzustand geändert wird.  
![Zustandsdiagramm](/Images/Zustandsdiagramm.png)  
  
Organisiert haben wir uns über Planka:  
![plankaPrtSc](/Images/planka.png)  
Obwohl wir uns bis zum Ende darum bemüht haben, ist trotzdem nichts aus dem Raketenantrieb geworden :( .

## Umsetzung
### Prototyp
![Prototyp Front](/Images/Prototyp-Front.jpg)  
![Prototyp Seite](/Images/Prototyp-Seite.jpg)  
Sehr simpel haben wir einen breiten Radstand, beide Räder werden mittels EV3 L Motoren angesteuert. Vorne rollt der Prototyp auf einer Metallkugel; dahinter befinden sich vier EV3 Lichtsensoren. Diese stellen fest, ob sich der Linienfolger noch auf der Linie befindet. Der Code ist dann dazu da, die Messungen richtig zu interpretieren und der Linie weiter zu folgen.

### Wettkampfversion
![Wettkampfversion](/Images/wettkampfversion.jpg)  
Die Wettkampfversion ist kompakter als der Prototyp. Was sich am meisten verändert hat ist:
- Reifen: Wir haben während dem Wettkampf grössere Reifen montiert, um eine bessere Zeit zu erreichen
- Sensorplatzierung: Beim Prototypen hatten wir zwei mittlere Sensoren und zwei äussere Sensoren. Bei der Wettkampfversion haben wir alle Sensoren so nahe aneinander wie nur möglich auf eine Reihe gebaut. 
- Dichte: Wie haben den Roboter kompakter gebaut, sodass er stabiler ist. Dafür haben wir auch kürzere Kabel verwendet, sodass diese die Reifen und die Fahrt allgemein nicht stören.  

Für den Code konnten wir die gleiche Struktur wie beim Prototypen verwenden, mussten aber ein paar Änderungen aufgrund der neuen Sensorplatzierung und der grösseren Räder vornehmen. Dabei handelt es sich um Feintuning bei der Fahr- und Kurvengeschwindigkeit.  

LightTest.py ist ein Programm zum Ermitteln der `ambient()` und `reflection()` Werte, die die Sensoren erfassen, damit sie für die korrekten Werte eingestellt werden können. Am Wettkampf haben wir uns aber nur die `reflection()` Werte angeschaut, da diese am aussagekräftigsten für das Messen der Linie waren.  

LineStraight.py ist das Programm für unseren ersten Wertungslauf. Hier ist der Roboter nicht über die Rampe gefahren. Wir haben uns anfangs dafür entschieden, da wir mal eine sichere Zeit haben wollten. In diesem Code soll der Roboter bei keiner Kreuzung abbiegen, aber er sollte bei einer T-Kreuzung (wenn er von unten kommt und daher 1111 erfasst) sich nach rechts drehen.  

LineRampe.py ist das Programm für die beiden anderen Wertungsläufe. Der Roboter sollte die erste Möglichkeit links abzubiegen nehmen. Das heisst, dass er anhalten und sich um 90° nach links drehen sollte, sobald die Sensoren 1110 oder 1100 (also eine Linkskurve) erfassen. Weil er das aber schon bei einer Kurve erfassen kann, soll er sich erst dann drehen, wenn er bei der korrekten Kreuzung angekommen ist. Diese erreicht er nach ungefähr sechs Sekunden, daher haben wir einprogrammiert, dass er sich erst nach sechs Sekunden nach Start bei einer korrekten Erkennung drehen sollte.
## Erfahrungen
### Roboterbau und Programmierung
Beim Bau des Roboters sollte man eine gute Balance zwischen Schnelligkeit und Wendigkeit finden. Der Motor hat eine bestimmte Höchstgeschwindigkeit. Will man dennoch schneller fahren, müssen grössere Räder her. Durch grössere Räder wird der Roboter aber sensibler für kleinste Kursabweichungen und wird dadurch instabiler. Um da entgegenzuwirken, muss man dann im Code die Drehgeschwindigkeit für allfällige Kurskorrekturen verringern, was dann aber die allgemeine Geschwindigkeit des Roboters verringert. Deshalb muss man die goldene Mitte finden.  
  
Beim Code sollte man einfach mal anfangen. Hat man das geschafft, sollte man schon einen ungefähren Aufbau und die nötigen Codeteile haben. Auf dieses Grundgerüst kann man dann aufbauen. Hat man dann einen Code, der funktioniert, aber nicht so übersichtlich ist, kann man dann die besten Teile davon auf eine neue Datei übertragen und diese perfektionieren. Diesen Prozess haben wir etwa 4-5-mal gemacht, bis wir auf unser Endresultat gekommen sind.  
  
Ist man mit dem Resultat nicht zufrieden, wenn der Roboter beispielsweise zu langsam ist, oder aus den Kurven fällt, sollte man nicht nur Änderungen an der Software, sondern auch an der Hardware vornehmen. Diese Veränderungen sollten jedoch immer schön ausbalanciert sein. Beide Komponenten sind voneinander abhängig, um einen funktionstüchtigen Roboter zu machen.
### Wettkampf
Wenn man nicht gut genug war, soll man es trotzdem probieren. Man sollte neue Sachen probieren und man sollte das, was man schon hat, perfektionieren. Und wenn es dann immer noch nicht funktioniert hat, kann man dann sagen, dass man es zumindest bis auf den letzten Drücker probiert hat.  
Wir können stolz sagen, dass wir es versucht und auch geschafft haben.  
Wir haben anfangs einen Lauf ohne Rampe gemacht, um einen sicheren zu haben. Uns ist aber sofort aufgefallen, dass wir über die Rampe müssen, um zu gewinnen. Nach langem tüfteln und ausprobieren haben wir dann eine Zeit von **15.94** geschafft. Damit haben wir die bisherige Rekordzeit um 2.22 Sekunden unterboten.  

https://github.com/arraky/RobOlympics/assets/76037364/3dd83696-8b8a-4f17-aed5-f8b1f5d29c0b  

Das Video wird in VSCode nur als Link angezeigt. Falls das Video nicht korrekt angezeigt wird, klicken Sie [hier](https://github.com/arraky/RobOlympics/blob/main/README.md) um die Onlineversion anzusehen.

### Vorgehensweise und Projekt insgesamt
Zusammengefasst war es eine tolle Erfahrung. Verständlicherweise ist es toll erster zu werden. Danke an Herr Hofer und Herr Scheidegger, die uns begleitet und uns das ermöglicht haben. Für weitere Informationen klicken Sie [hier](https://www.youtube.com/watch?v=dQw4w9WgXcQ).  

![PodestFoto](/Images/podest.png)  
### Team GBSL-ꓶSꓭꓨ#1  