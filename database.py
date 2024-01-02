from sqlalchemy import create_engine , text
db_connect_string ="mysql+pymysql://pddmygfs1a2ebc2v432e:pscale_pw_w1i6N0wARpvnPAE2YRcAlRl5tfM70BIgadZe3Qtb38W@aws.connect.psdb.cloud/fizzcareers?charset=utf8mb4"
engine = create_engine(db_connect_string, connect_args= {
    'ssl': {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
}) 

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.fetchall():
            jobs.append(dict(row))
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"),
                              val=id)
        rows = result.fetchall()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])
        

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, 
                 job_id=job_id, 
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])