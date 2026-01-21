
from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://<user>:<password>@<rds-endpoint>:3306/myflixdb"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM movies"))
    for row in result:
        print(row)
