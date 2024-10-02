from util import get_connection

def build_insert_query(table_name, column_name):
    column_values = tuple(map(lambda column: column.replace(column, '%s')))
    query = f(f'''
    insert into {table_name} {column_name} values {column_values}
    ''')
    return query


def insert_data(connection, cursor, query, data, batch_size=100):
