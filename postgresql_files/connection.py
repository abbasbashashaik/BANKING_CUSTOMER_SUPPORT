from sqlalchemy import create_engine,select,text
import psycopg2
from sqlalchemy.orm import Session
database_url="postgresql+psycopg2://postgres:system@localhost:5432/Sample_database"

engine=create_engine(
    database_url,echo=True
)
# with engine.connect() as con:
#     res=con.execute(text("select * from emp"))
#     print(res.fetchone())
