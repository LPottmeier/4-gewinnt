# 4-gewinnt
4-gewinnt


Strategie:


variable spielernummer




relativ einfach bei vier gewinnt ... bewerte die anzahl der möglichkeiten die ein spielzug dem jeweiligen spieler bringt 4 in eine reihe zu bringen ...

sagen wir mal du hast ein leeres feld ... ganz links machst du nun deinen zug ... durch diesen zug hast du nun 3 möglichkeiten eine 4er reihe zu bilden ... nach oben ... nach oben rechts ... und nach rechts ...

diese metrik würde diesen zug mit 3 bewerten ... wirfst du den stein dagegen in die mitte, lautet das ergebnis 5 ... nach links ... nach links oben ... nach oben ... nach rechts oben ... und nach rechts ...

da 5>3 ist es gemäß dieser metrik sinnvoller den stein am anfang in die mitte zu werfen ... was ja auch den allgemeinen erfahrungen in diesem spiel entspricht ...

betrachtet man die folgezüge, wird klar, dass man die zugfolge wählen sollte bei der diese metrik für die eigene seite maximal werden kann, und gleichzeitig die gleiche metrik für den gegner minimal wird ...


vier gewinnt ist in dieser hinsicht erledigt ... es gibt genug beweisbare algorithmen die ein perfektes spiel liefern ...