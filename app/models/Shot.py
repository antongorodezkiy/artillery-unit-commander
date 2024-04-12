from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

import app.database as database

class Shot(database.declarative_base):
	__tablename__ = "shots"
	id = Column(Integer, primary_key = True)
	created_at = Column(DateTime)
	correction_id = Column(Integer, ForeignKey("corrections.id"), nullable = False)
	correction = relationship("Correction", back_populates = "shots")
	def __repr__(self):
		return f"Shot(id={self.id!r}, sight={self.created_at!r})"
