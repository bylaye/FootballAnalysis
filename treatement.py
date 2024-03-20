import csv
import params
import os
import mysql.connector


dataset_path = os.path.join(params.DIRECTORY, params.NAME_DIR_DATASET)
print(dataset_path)


def extract_fields(csv_file,season):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        dataset = []
        for row in reader:
            row  = row[:23]
            row.insert(0, season)
            dataset.append(tuple(row))
    dataset.pop(0)
    return dataset


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
                `Time` CHAR(10),
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
                `AR` INT(5),
                PRIMARY KEY (`SEASON`, `LEAGUE`, `HomeTeam`, `AwayTeam`)
            ) ENGINE=InnoDB
        """

def insert_data(cursor, tb_name, val):
    req = f"""
            INSERT INTO {tb_name} 
                (`SEASON`, `LEAGUE`, `Date`, `Time`, `HomeTeam`, `AwayTeam`, `FTHG`, `FTAG`, `FTR`, `HTHG`,
                  `HTAG`, `HTR`, `HS`, `AS`, `HST`, `AST`, `HF`, `AF`, `HC`, `AC`, `HY`, `AY`, `HR`, `AR` )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
                dataset = extract_fields(file, season)
                insert_data(cursor, TB_NAME, dataset)
            cnx.commit()
    cnx.close()
        