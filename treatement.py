import csv
import params
import os
import mysql.connector


dataset_path = os.path.join(params.DIRECTORY, params.NAME_DIR_DATASET)
print(dataset_path)

"""Check if the dataset directory exist"""
def dataset_directory_exits(dataset_path):
    return os.path.isdir(dataset_path)


def extract_fields(csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        dataset = []
        for row in reader:
            dataset.append(row[:23])
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
                `id` int(11)
            )ENGINE=InnoDB
        """

if __name__ == '__main__':
    cnx = engine_connection(params.MYSQL_USER, params.MYSQL_PASSWORD, params.MYSQL_HOST)
    DB_NAME = params.MYSQL_DB_NAME
    cursor = cnx.cursor()
    cnx.database = create_database(cursor)
    create_table(cursor,'test')

    cnx.close()

    extract_fields(os.path.join(dataset_path, '2324', '2324_I1.csv'))