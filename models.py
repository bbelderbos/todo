from sqlalchemy import Column, Sequence, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    description = Column(String(250))
    done = Column(Boolean, default=False)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.id}', "
            f"'{self.description}', '{self.done}')"
        )
