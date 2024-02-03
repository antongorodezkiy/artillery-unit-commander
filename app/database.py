from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from .config import config

path = config.get("database", "path")

engine = create_engine(f"sqlite:///{path}", echo = True, future = True)

declarative_base = declarative_base()

# we have ímport here, when we already have declarative_base
import app.models.Goal 
