from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

import app.database as database

class Correction(database.declarative_base):
    __tablename__ = "corrections"
    id = Column(Integer, primary_key = True)
    sight = Column(String, nullable = False)
    angle = Column(String, nullable = False)
    created_at = Column(DateTime)
    goal_id = Column(Integer, ForeignKey("goals.id"), nullable = True)
    goal = relationship("Goal", back_populates = "corrections")
    shots = relationship(
    	"Shot", back_populates = "correction", cascade = "all, delete-orphan"
    )
    def __repr__(self):
        return f"Correction(id={self.id!r}, sight={self.sight!r}, angle={self.angle!r})"
