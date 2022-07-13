from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base
import uuid
class Todo(Base):
        __tablename__ = "todo"
        #id=db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
        id = Column(String, primary_key=True, index=True,default=str (uuid.uuid4()))
        message= Column(String)
