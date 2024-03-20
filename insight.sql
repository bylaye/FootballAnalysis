-- Basic : Level Easy

-- Le nombre total de matchs par league/ season
SELECT Season, League, count(*) as total_match 
    FROM Matchs
    GROUP BY Season, League;

-- Le nombre total de matchs saison en cours (2023-2024)
SELECT Season, League, count(*) as total_match 
    FROM Matchs 
    WHERE Season='2324'
    GROUP BY Season, League;


-- Le nombre total de matchs de la ligue / saison
SELECT Season, League, count(*) as total_match 
    FROM Matchs 
    WHERE League='F1'
    GROUP BY Season;


-- Le nombre de but marque par saison en ligue 1 par equipe domicile et exterieur
SELECT Season, League, SUM(FTHG) as HomeGoal, SUM(FTAG) as AwayGoal, SUM(FTHG)+SUM(FTAG) as TotalGoal
    FROM Matchs
    WHERE League='E0'
    GROUP BY Season, League;


-- level Medium

-- Le nombre de buts marque par saison en Premier League 
-- a domicile/exterieur et total buts trier par saison 
SELECT Season, League, SUM(FTHG) as HomeGoal, SUM(FTAG) as AwayGoal, SUM(FTHG)+SUM(FTAG) as TotalGoal
    FROM Matchs
    WHERE League='E0'
    GROUP BY Season
    ORDER BY TotalGoal desc;


-- Nombre de carton distribue par saison / ligue
SELECT Season, League, SUM(HY)+SUM(AY) as YellowCard, SUM(HR)+SUM(AR) as RedCard
FROM Matchs
GROUP BY Season, League;


-- Nombre de Faute commise par saison /League
SELECT Season, League, SUM(HF)+SUM(AF) as Faults
FROM Matchs
GROUP BY Season, League;


-- Corner par saison /League
SELECT Season, League, SUM(HC)+SUM(AC) as Corners
FROM Matchs
GROUP BY Season, League;


-- Top Matchs avec les plus de but marques 
SELECT Season, League, HomeTeam, AwayTeam, FTHG, FTAG, FTHG+FTAG as totalGoal 
FROM Matchs 
GROUP BY Season, Hometeam, awayteam 
ORDER BY totalGoal DESC 
LIMIT 20;


-- Top Matchs avec les plus larges score par saison/league
-- Il y a une difference entre score plus large et total Buts 
SELECT Season, League, HomeTeam, AwayTeam, FTHG, FTAG, abs(FTHG-FTAG) as diffGoal 
FROM Matchs 
GROUP BY Season, Hometeam, awayteam 
ORDER BY diffGoal DESC 
LIMIT 20;


-- Top matchs des equipes qui ont pris une raclee a domicile
-- Humiliation score fleuve devant leur supporters
SELECT Season, League, HomeTeam, AwayTeam, FTHG, FTAG 
FROM Matchs 
WHERE (FTAG-FTHG) >= 5
GROUP BY Season, Hometeam, awayteam 
ORDER BY FTAG-FTHG DESC 
LIMIT 20;


-- Top Match avec le plus de sanctions
-- On considere un poids plus important pour les red cards
SELECT Season, League, HomeTeam, AwayTeam, HY, AY, HY+AY as YellowCards, HR, AR, HR+AR as RedCards
FROM Matchs
GROUP BY Season, League, HomeTeam, AwayTeam
ORDER BY RedCards*1.5+YellowCards DESC 
LIMIT 10;


-- Niveau Avance
-- Tout les statistiques matchs de Milan Saison 2021-2022. Annee du sacre
-- But marque, encaisse, tirs, corner, faute, carton jaune rouge
SELECT Season, League, Date, Team, Game, Scored, Conceded, Result, Shoot, Target, 
    Corner, Fault, Yellow as YC, Red as RC, Opponent
FROM
(SELECT Season, League, Date, HomeTeam as Team, 'H' as Game, FTHG as Scored, FTAG as Conceded, 
    HS as Shoot, HST as Target, HY as Yellow, HC as Corner, HF as Fault, HR as Red,
    CASE 
        WHEN FTR = 'H' then 'W'
        WHEN FTR = 'A' then 'L'
        ELSE 'D'
    END as Result, AwayTeam as Opponent
FROM Matchs
UNION ALL
SELECT Season, League, Date, AwayTeam as Team, 'A' as Game, FTAG as Scored, FTHG as Conceded, 
    `AS` as Shoot, AST as Target, AY as Yellow, AC as Corner, AF as Fault, AR as Red,
    CASE 
        WHEN FTR = 'H' then 'L'
        WHEN FTR = 'A' then 'W'
        ELSE 'D'
    END as Result, HomeTeam as Opponent
FROM Matchs) as t 
WHERE season='2122' AND team='Milan' 
ORDER BY STR_TO_DATE(`Date`, '%d/%m/%Y') ;

-- Classement general complet Premier league Saison 2122
SELECT Season, RANK() OVER (ORDER BY SUM(RESULT) DESC, SUM(Scored-Conceded) desc) as Pos, 
    Team, COUNT(Team) as Games, SUM(Result) as Pts, 
    SUM(scored) as scored, SUM(Conceded) as Conceded,
    SUM(CASE WHEN Result=3 then 1 else 0 end) as W, 
    SUM(CASE WHEN Result=0 then 1 else 0 end) as L,
    SUM(CASE WHEN Result=1 then 1 else 0 end) as D,
    SUM(Yellow) as YC, SUM(Red) as RC,
    SUM(Fault) as Faults,
    SUM(Shoot) as Shoots, SUM(`Target`) as `Targets`
FROM
(SELECT Season, League, Date, HomeTeam as Team, 'H' as Game, FTHG as Scored, FTAG as Conceded, 
    HS as Shoot, HST as Target, HY as Yellow, HC as Corner, HF as Fault, HR as Red,
    CASE 
        WHEN FTR = 'H' then 3
        WHEN FTR = 'A' then 0
        ELSE 1
    END as Result, AwayTeam as Opponent
FROM Matchs
UNION ALL
SELECT Season, League, Date, AwayTeam as Team, 'A' as Game, FTAG as Scored, FTHG as Conceded, 
    `AS` as Shoot, AST as Target, AY as Yellow, AC as Corner, AF as Fault, AR as Red,
    CASE 
        WHEN FTR = 'H' then 0
        WHEN FTR = 'A' then 3
        ELSE 1
    END as Result, HomeTeam as Opponent
FROM Matchs) as t 
WHERE season='2122' AND League='E0'
GROUP BY Team
ORDER BY Pos;