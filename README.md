# FootballAnalysis
Top European League Analysis

Resultat et clssement des 8 grands champonnats europeen: \
Angleterre, Italie, Espagne, France, Allemand, Portugal, Hollande et Belgique.

Pour telecharger les resultats score, on lance le script download_season_data\
L'historique des saison est limite a la saison 2006\
comme suit : python download_season_data.py 'nombre de saison'
```
python3 download_season_data.py 2
```
Resultat de la requete
```
Season 2324
Done for League England,  0.726942 seconds
Done for League Italy,  0.693359 seconds
Done for League Germany,  0.659689 seconds
Done for League Spain,  0.685452 seconds
Done for League France,  0.67284 seconds
Done for League Portugal,  0.687579 seconds
Done for League Netherlands,  0.677568 seconds
Done for League Belgium,  0.660663 seconds
Season 2223
Done for League England,  0.696271 seconds
Done for League Italy,  0.735687 seconds
Done for League Germany,  0.705515 seconds
Done for League Spain,  0.72994 seconds
Done for League France,  0.722887 seconds
Done for League Portugal,  0.699869 seconds
Done for League Netherlands,  0.713196 seconds
Done for League Belgium,  0.704222 seconds
```

## Description des champs de colonnes

* 'Div' => Division League
* 'Date'  =>  Date Match
* 'Time' : TIme match programmed
* 'HomeTeam' : Home play at Home
* 'AwayTeam' : Home Away
* 'FTHG' : Full Time Home Goal
* 'FTAG' : Full Time Away Goal
* 'FTR' : Full Time Result
* 'HTHG' : Half Time Home Goal
* 'HTAG': Half Time Away Goal
* 'HTR' : Half Time Result
* 'HS': Home Shoot
* 'AS' : Away Shoot
* 'HST': Home Shoot Target
* 'AST' : Away Shoot Target
* 'HF': Home Total Fault 
* 'AF': Away Total Fault
* 'HC': Home Total Corner
* 'AC' : Away Total Corner
* 'HY' : Home Total Yellow card
* 'AY' : Away Total Yellow card
* 'HR' : Home Total Red Card
* 'AR' : Away Total Red Card
