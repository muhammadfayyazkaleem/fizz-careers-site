from sqlalchemy import create_engine , text
db_connect_string ="mysql+pymysql://b48p1gl118azhgzcs681:pscale_pw_FzoVwzsIJDUBBUd0OyYKeMwDjJJUrdkXfrkgyraMs4c@aws.connect.psdb.cloud/fizzcareerdb?charset=utf8mb4"
engine = create_engine(db_connect_string, connect_args= {
    'ssl': {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
}) 

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from job"))
        jobs = []
        for row in result.fetchall():
            jobs.append(dict(row))
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from job where id = :val"),
                              val=id)
        rows = result.fetchall()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])