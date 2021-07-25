import os

from pymysql import Connection


def generate(mysql: dict, table_name: str, model_name: str, model_path: str):
    model_path = model_path % model_name
    connection = Connection(**mysql)
    try:
        cursor = connection.cursor()
        cursor.execute(
            query="SELECT TABLE_COMMENT FROM information_schema.TABLES "
                  "WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s",
            args=(mysql['database'], table_name)
        )
        TABLE_COMMENT, = cursor.fetchone()
        cursor.close()
        cursor = connection.cursor()
        cursor.execute(
            query="SELECT COLUMN_NAME, COLUMN_TYPE, COLUMN_COMMENT FROM information_schema.COLUMNS "
                  "WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s",
            args=(mysql['database'], table_name)
        )
        fields = cursor.fetchall()
        cursor.close()
        if os.path.exists(model_path):
            print(f"File {model_path}:1 was overwrite.")
        with open(model_path, 'w', encoding='utf8') as f:
            f.write("from ._BaseModel import BaseModel\n\n\n")
            f.write(f"class {model_name}(BaseModel):\n")
            TABLE_COMMENT = ' '.join(TABLE_COMMENT.split())
            if TABLE_COMMENT:
                f.write(f'    """{TABLE_COMMENT}"""\n\n')
            f.write("    def __init__(self, row: dict = None):\n")
            f.write("        row = dict() if row is None else row\n\n")
            for COLUMN_NAME, COLUMN_TYPE, COLUMN_COMMENT in fields:
                if COLUMN_TYPE == 'bit(1)':
                    f.write(
                        f"        self.{COLUMN_NAME} = (None"
                        f" if '{COLUMN_NAME}' not in row"
                        f" else bool(row['{COLUMN_NAME}'] == b'\\x01')"
                        f" if type(row['{COLUMN_NAME}']) is bytes and len(row['{COLUMN_NAME}']) == 1"
                        f" else row['{COLUMN_NAME}'])\n"
                    )
                else:
                    f.write(f"        self.{COLUMN_NAME} = row['{COLUMN_NAME}'] if '{COLUMN_NAME}' in row else None\n")
                COLUMN_COMMENT = ' '.join(COLUMN_COMMENT.split())
                if COLUMN_COMMENT:
                    f.write(f'        """{COLUMN_COMMENT}"""\n\n')
                else:
                    f.write('\n')

    except Exception as e:
        connection.rollback()
        print(type(e), e)
    finally:
        connection.close()
