from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

import app.database as database

class Goal(database.declarative_base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    created_at = Column(DateTime)
    corrections = relationship(
    	"Correction", back_populates = "goal", cascade = "all, delete-orphan"
    )
    def __repr__(self):
        return f"Goal(id={self.id!r}, name={self.name!r})"
