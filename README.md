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

* 'Div' : Division League
* 'Date' : Date Match
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

## Importer les donnees a la base MySql/Mariadb
* Les configurations du serveur de base de donnees sont dans le fichier config.ini.\
On Peut l'editer et le specifier en fonction de notre configuration serveur pour redefinir\
les parametres de connexion.

* Ensuite on peut lancer directement le script d'import (treatement.py)
```
python3 treatement.py
```

```
creation table
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1819/1819_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1819/1819_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1819/1819_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1819/1819_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1819/1819_D1.csv
Done Season 1819 - total rows 306
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1213/1213_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1213/1213_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1213/1213_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1213/1213_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1213/1213_SP1.csv
Done Season 1213 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0708/0708_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0708/0708_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0708/0708_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0708/0708_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0708/0708_F1.csv
Done Season 0708 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2324/2324_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2324/2324_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2324/2324_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2324/2324_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2324/2324_D1.csv
Done Season 2324 - total rows 234
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0809/0809_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0809/0809_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0809/0809_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0809/0809_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0809/0809_E0.csv
Done Season 0809 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1516/1516_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1516/1516_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1516/1516_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1516/1516_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1516/1516_I1.csv
Done Season 1516 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1617/1617_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1617/1617_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1617/1617_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1617/1617_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1617/1617_E0.csv
Done Season 1617 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1415/1415_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1415/1415_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1415/1415_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1415/1415_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1415/1415_I1.csv
Done Season 1415 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1718/1718_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1718/1718_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1718/1718_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1718/1718_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1718/1718_F1.csv
Done Season 1718 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2223/2223_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2223/2223_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2223/2223_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2223/2223_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2223/2223_F1.csv
Done Season 2223 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1011/1011_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1011/1011_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1011/1011_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1011/1011_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1011/1011_D1.csv
Done Season 1011 - total rows 306
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1112/1112_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1112/1112_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1112/1112_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1112/1112_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1112/1112_E0.csv
Done Season 1112 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1920/1920_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1920/1920_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1920/1920_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1920/1920_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1920/1920_D1.csv
Done Season 1920 - total rows 306
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2122/2122_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2122/2122_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2122/2122_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2122/2122_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2122/2122_I1.csv
Done Season 2122 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0910/0910_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0910/0910_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0910/0910_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0910/0910_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/0910/0910_I1.csv
Done Season 0910 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1314/1314_F1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1314/1314_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1314/1314_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1314/1314_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/1314/1314_SP1.csv
Done Season 1314 - total rows 380
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2021/2021_I1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2021/2021_SP1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2021/2021_D1.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2021/2021_E0.csv
/home/aniang/Labs/FootballAnalysis/SeasonDatasets/2021/2021_F1.csv
Done Season 2021 - total rows 380
```

* On peut taper sur la base (FootballAnalysis) et voir la description de la table(Matchs)
```
MariaDB [FootballAnalysis]> desc Matchs;
+----------+----------+------+-----+---------+-------+
| Field    | Type     | Null | Key | Default | Extra |
+----------+----------+------+-----+---------+-------+
| SEASON   | char(4)  | NO   | PRI | NULL    |       |
| LEAGUE   | char(5)  | NO   | PRI | NULL    |       |
| Date     | char(20) | YES  |     | NULL    |       |
| HomeTeam | char(50) | NO   | PRI | NULL    |       |
| AwayTeam | char(50) | NO   | PRI | NULL    |       |
| FTHG     | char(5)  | YES  |     | NULL    |       |
| FTAG     | char(5)  | YES  |     | NULL    |       |
| FTR      | char(2)  | YES  |     | NULL    |       |
| HTHG     | char(5)  | YES  |     | NULL    |       |
| HTAG     | char(5)  | YES  |     | NULL    |       |
| HTR      | char(2)  | YES  |     | NULL    |       |
| HS       | char(5)  | YES  |     | NULL    |       |
| AS       | char(5)  | YES  |     | NULL    |       |
| HST      | char(5)  | YES  |     | NULL    |       |
| AST      | char(5)  | YES  |     | NULL    |       |
| HF       | char(5)  | YES  |     | NULL    |       |
| AF       | char(5)  | YES  |     | NULL    |       |
| HC       | char(5)  | YES  |     | NULL    |       |
| AC       | char(5)  | YES  |     | NULL    |       |
| HY       | char(5)  | YES  |     | NULL    |       |
| AY       | char(5)  | YES  |     | NULL    |       |
| HR       | char(5)  | YES  |     | NULL    |       |
| AR       | char(5)  | YES  |     | NULL    |       |
+----------+----------+------+-----+---------+-------+
23 rows in set (0,001 sec)

MariaDB [FootballAnalysis]> 
```