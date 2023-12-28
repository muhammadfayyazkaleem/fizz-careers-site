from sqlalchemy import create_engine , text
db_connect_string ="mysql+pymysql://7fzrl8irnvel20dtctqg:pscale_pw_VI1tU4lnrpJCqo6dQhPAWvfeyDH4I7ufNeFLTGVZHg9@aws.connect.psdb.cloud/fizz-careers?charset=utf8mb4"
engine = create_engine(db_connect_string, connect_args= {
    'ssl': {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
}) 

def load_job_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from job"))
        jobs = []
        for row in result.fetchall():
            jobs.append(dict(row))
        return jobs


