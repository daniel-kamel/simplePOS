#!/ur/bin/python3
from models.basemodel import Base, engine
from models.models import *

Base.metadata.create_all(engine)
