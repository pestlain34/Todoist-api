

from api.api import router
from fastapi import FastAPI
from data_access import models
from data_access.database import engine
from data_access.models import Base


models.Base.metadata.create_all(bind=engine)
app = FastAPI(debug = True)
app.include_router(router, prefix="/api")
Base.metadata.create_all(bind=engine)
# session_maker = sessionmaker(bind = create_engine("postgresql+psycopg2://postgres:dfdfdfdjk34@localhost/apifirst"))