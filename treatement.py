import csv
import params
import os
import mysql.connector


dataset_path = os.path.join(params.DIRECTORY, params.NAME_DIR_DATASET)

header_list = [
    'Season', 'Div', 'Date', 'HomeTeam', 'AwayTeam', 
    'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 
    'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR'
]

""""""
def headers(header_list, header_dataset):
    header_dict = {}
    for i, h in enumerate(header_dataset):
        if h in header_list:
            if h not in header_dict:
                header_dict[h] = i
            else:
                print(f'Duplicate header {h} {header_dict[h]}, {i}')
    return header_dict


def extract_fields(csv_file,season):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        dataset = []
        for row in reader:
            #row  = row[:25]
            # verifier les team name vide
            if len(row[2]) > 1 and len(row[3]) > 1:
                dataset.append(row)
    header_dataset = dataset.pop(0)
    result = []
    h = headers(header_list=header_list, header_dataset=header_dataset)
    for row in dataset:
        r = (
            season, row[h[header_list[1]]], row[h[header_list[2]]], 
            row[h[header_list[3]]], row[h[header_list[4]]], row[h[header_list[5]]],
            row[h[header_list[6]]], row[h[header_list[7]]], row[h[header_list[8]]], 
            row[h[header_list[9]]], row[h[header_list[10]]], row[h[header_list[11]]], 
            row[h[header_list[12]]], row[h[header_list[13]]], row[h[header_list[14]]], 
            row[h[header_list[15]]], row[h[header_list[16]]], row[h[header_list[17]]], 
            row[h[header_list[18]]], row[h[header_list[19]]], row[h[header_list[20]]], 
            row[h[header_list[21]]], row[h[header_list[22]]]
        )
        result.append(r)
    return result


"""Connection Server Database"""
def engine_connection(user, password, host, port=3306):
    cnx = mysql.connector.connect(
        user=user, password=password,
        host=host, port=port
    )
    return cnx


"""Creation Database"""
def create_database(cursor, db_name=params.MYSQL_DB_NAME):
    try:
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET 'utf8' "
        )
        cursor.execute(f'USE {db_name}')
        return db_name
    except mysql.connector.Error as err:
        print(f'Failed creating database {err}')
        exit(1)


def create_table(cursor, tb_name):
    try:
        print(f'creation table')
        tb_description = table_description(tb_name)
        cursor.execute(tb_description)
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)


def table_description(tb_name):
    return f"""
            CREATE TABLE IF NOT EXISTS {tb_name} 
            (
                `SEASON` CHAR(4),
                `LEAGUE` CHAR(5),
                `Date` CHAR(20),
                `HomeTeam` CHAR(50),
                `AwayTeam` CHAR(50),
                `FTHG` CHAR(5),
                `FTAG` CHAR(5),
                `FTR` CHAR(2),
                `HTHG` CHAR(5),
                `HTAG` CHAR(5),
                `HTR` CHAR(2),
                `HS` CHAR(5),
                `AS` CHAR(5),
                `HST` CHAR(5),
                `AST` CHAR(5),
                `HF` CHAR(5),
                `AF` CHAR(5),
                `HC` CHAR(5),
                `AC` CHAR(5),
                `HY` CHAR(5),
                `AY` CHAR(5),
                `HR` CHAR(5),
                `AR` CHAR(5),
                PRIMARY KEY (`SEASON`, `LEAGUE`, `HomeTeam`, `AwayTeam`)
            ) ENGINE=InnoDB
        """

def insert_data(cursor, tb_name, val):
    req = f"""
            INSERT INTO {tb_name} 
                (`SEASON`, `LEAGUE`, `Date`,  `HomeTeam`, `AwayTeam`, `FTHG`, `FTAG`, `FTR`, `HTHG`,
                  `HTAG`, `HTR`, `HS`, `AS`, `HST`, `AST`, `HF`, `AF`, `HC`, `AC`, `HY`, `AY`, `HR`, `AR` )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    cursor.executemany(req, val)
    


if __name__ == '__main__':
    cnx = engine_connection(params.MYSQL_USER, params.MYSQL_PASSWORD, params.MYSQL_HOST)
    DB_NAME = params.MYSQL_DB_NAME
    TB_NAME = 'Matchs'
    cursor = cnx.cursor()
    cnx.database = create_database(cursor)
    create_table(cursor,TB_NAME)
    
    for dirs,_, files in os.walk(dataset_path):
        if files:
            season = os.path.split(dirs)[-1]
            for f in files:
                file = os.path.join(dirs, f)
                print(file)
                dataset = extract_fields(file, season)
                insert_data(cursor, TB_NAME, dataset)
            cnx.commit()
            print(f'Done Season {season} - total rows {(len(dataset))}')
    cnx.close()
        