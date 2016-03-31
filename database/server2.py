from walnut_street import routes

from sqlalchemy import create_engine
engine = create_engine('postgresql://localhost/walnut_dev', convert_unicode=True)

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

db_session = scoped_session(sessionmaker(autocommit=False,
				      autoflush=False,
				      bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
	import finalmodels
	Base.metadata.create_all(bind=engine)

init_db()
