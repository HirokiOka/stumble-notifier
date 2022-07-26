import sqlalchemy as sa


def get_all_data():
    conn = sa.create_engine('postgresql://postgres:hiroki0827@localhost:5432')
    query = 'SELECT * FROM exelog'
    rows = conn.execute(query)
    return rows


def get_users():
    conn = sa.create_engine('postgresql://postgres:hiroki0827@localhost:5432')
    query = 'SELECT userid FROM exelog'
    row_data = conn.execute(query)
    ids = [x[0] for x in row_data]
    return ids


def get_code_params(user_id):
    conn = sa.create_engine('postgresql://postgres:hiroki0827@localhost:5432')
    query = f'SELECT executedAt, sloc, ted FROM exelog WHERE userid={user_id}'
    code_params = conn.execute(query)
    return code_params


def get_source_code(user_id, executed_time):
    conn = sa.create_engine('postgresql://postgres:hiroki0827@localhost:5432')
    query = f"SELECT sourceCode FROM exelog WHERE userid={user_id} and executedAt='{executed_time}'"
    row_data = conn.execute(query)
    source_code = [x[0] for x in row_data][0]
    return source_code
