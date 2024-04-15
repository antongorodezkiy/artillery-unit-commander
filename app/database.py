from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from .config import config
from .args import args

path = config.get("env", "DATABASE_PATH", fallback = "resources/artillery.db")
verbose = args.verbose or config.getboolean("env", "VERBOSE", fallback = False)
engine = create_engine(f"sqlite:///{path}", echo = verbose, future = True)

declarative_base = declarative_base()

# we have ímport here, when we already have declarative_base
import app.models.Goal
