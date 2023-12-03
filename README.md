# RobOlympics Line Follower
## Organisation und Prozess
### Ziel
Ziel des Linienfolgers ist es, einer schwarzen Linie zu folgen bis er zum Ziel kommt. Die Strecke wird am Morgen des Wettkampfs festgelegt und besteht aus folgenden Elementen:
![Streckenelemente](/Images/Streckenelemente.png)
Die Strecke am Wettkampf sah dann so aus:
![Strecke](/Images/strecke.jpg)
Wie man sieht gibt es auch eine Rampe, welche als Abkürzung dient.
### Regeln
1. Der Roboter darf die maximale Grösse von 20 cm x 25 cm x 25 cm (B x L x H) nie überschreiten.
2. Greift ein Teilnehmer vor dem Erreichen der Zielposition in das Spiel ein, wird der Wertungslauf abgebrochen.
3. Sieger ist, wer den Parcours in der kürzesten Zeit durchfahren ist.
4. Ein Abkürzen oder direktes Anfahren des Ziels ist nicht erlaubt. Der Roboter 
muss der Linie folgen.

## Entwurf
Für den Roboter brauchen wir zwei mittlere Sensoren, die prüfen, ob der Roboter immer noch auf der Linie ist und auf jeder Seite einen äusseren Sensor um engere Kurven frühzeitig zu entdecken.  
Der restliche aufbau haben wir je nach Sensorplatzierung verändert um den Grössenanforderungen gerecht zu werden.  
  
Im Code müssen wir das Verhalten für jede mögliche Sensorkombination einprogrammieren. Eine 1 steht für das Erkennen einer schwarzen Linie, eine 0 steht für das Nichterkennen einer schwarzen Linie, also weiss:  
- 0000 -> nichts
- 1000 -> langsamer, rotation links
- 0100 -> gleichschnell, leicht links lenken
- 1100 -> stehenbleiben, 90° links (für über Rampe)
- 0010 -> gleichschnell, leicht rechts lenken
- 1010 -> nichts
- 0110 -> gerade aus
- 1110 -> stehenbleiben, 90° links (für über Rampe)
- 0001 -> langsamer, rotation rechts
- 1001 -> nichts
- 0101 -> nichts
- 1101 -> nichts
- 0011 -> nichts
- 1011 -> nichts
- 0111 -> nichts
- 1111 -> stehenbleiben, 90° rechts (T-Kreuzung von unten, nicht über Rampe)  

Wird bei einem Sensorzustand ein Verhalten festgelegt, wird es so lange fortgeführt, bis es durch einen anderen Sensorzustand geändert wird.  
![Zustandsdiagramm](/Images/Zustandsdiagramm.png)

## Umsetzung
### Prototyp
![Prototyp Front](/Images/Prototyp-Front.jpg)
![Prototyp Seite](/Images/Prototyp-Seite.jpg)
Sehr simpel haben wir einen breiten Radstand, beide Räder werden mittels EV3 L Motoren angesteuert. Vorne rollt der Prototyp auf einer Metallkugel; dahinter befinden sich vier EV3 Lichtsensoren. Diese stellen fest, ob sich der Linienfolger noch auf der Linie befindet. Der Code ist dann dazu da, die Messungen richtig zu interpretieren und der Linie weiter zu folgen.

### Wettkampfversion
![Wettkampfversion](/Images/wettkampfversion.jpg)
Die Wettkampfversion ist kompakter als der Prototyp. Was sich am meisten verändert hat ist:
- Reifen: Wir haben während dem Wettkampf grössere Reifen montiert um eine bessere Zeit zu erreichen
- Sensorplatzierung: Beim Prototypen hatten wir zwei mittlere Sensoren und zwei äussere Sensoren. Bei der Wettkampfversion haben wir alle Sensoren so nahe aneinander wie nur möglich auf eine Reihe gebaut. 
- Dichte: Wie haben den Roboter kompakter gebaut, sodass er stabiler ist. Dafür haben wir auch kürzere Kabel verwendet, sodass diese die Reifen und die Fahrt allgemein nicht stören.  

Für den Code konnten wir die gleiche Struktur wie beim Prototypen verwenden, mussten aber ein paar Änderungen aufgrund der neuen Sensorplatzierung und der grösseren Räder vornehmen.
## Erfahrungen
### Roberterbau und Programmierung
Beim Bau des Roboters sollte man eine gute balance zwischen Schnelligkeit und Wendigkeit finden. Der Motor hat eine bestimmte Höchstgeschwindigkeit. Will man dennnoch schneller fahren, müssen grössere Räder her. Durch grössere Räder wird der Roboter aber sensibler für kleinste Kursabweichungen und wird dadurch instabiler. Um da entgegenzuwirken muss man dann im Code die Drehgschwindigkeit für allfällige Kurskorrekturen verringern, was dann aber die allgeimeine geschwindigkeit des Roboters verringert. Deshalb muss man die goldene Mitte finden.  
  
Beim Code sollte man einfach mal anfangen. Hat man das geschafft, sollte man schon einen ungefähren Aufbau und die nötigen Codeteile haben. Auf dieses Grundgerüst kann man dann aufbauen. Hat man dann einen Code der funktioniert, aber nicht so übersichtlich ist, kann man dann die besten Teile davon auf eine neue Datei übertragen und diese perfektionieren. Diesen Prozess haben wir etwa 4-5 mal gemacht, bis wir auf unser Endresultat gekommen sind.  
  
Ist man mit dem Resultat nicht zufrieden, wenn der Roboter beispielsweise zu langsam ist, oder aus den Kurven fällt, sollte man nicht nur änderungen an der Software, sondern auch an der Hardware vornehmen. Diese Veränderungen sollten jedoch immer schön ausbalanciert sein. Beide Komponenten sind voneinander abhängig um einen funktionstüchtigen Roboter zu machen.
### Wettkampf
Wenn man nicht gut genug war, soll man es trotzdem probieren. Man sollte neue Sachen probieren und man sollte das was man schon hat perfektionieren. Und wenn es dann immer noch nicht funktioniert hat kann man dann sagen, dass man es zumindest bis auf den letzten Drücker probiert hat.  
Wir können stolz sagen, dass wir es versucht und auch geschafft haben.  
Wir haben anfangs einen Lauf ohne Rampe gemacht um einen sicheren zu haben. Uns ist aber sofort aufgefallen, dass wir über die Rampe müssen um zu gewinnen. Nach langem tüfteln und ausprobieren haben wir dann eine Zeit von **15.94** geschafft. Damit haben wir die bisherige Rekordzeit um 2.22 Sekunden unterboten.  

### Vorgehensweise und Projekt insgesamt
Code for RobOlympics bot
![PodestFoto](/Images/podest.png)