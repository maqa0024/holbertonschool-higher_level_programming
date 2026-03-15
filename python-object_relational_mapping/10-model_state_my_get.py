#!/usr/bin/python3
"""
Prints the State object with the name passed as argument 
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # 1. Connect to the database using arguments provided
    # Syntax: mysql+mysqldb://user:password@host/db
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # 2. Create a configured "Session" class and instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. Query the State object
    # We use .filter() with the fourth command line argument
    # SQLAlchemy handles the parameterization to prevent SQL injection
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # 4. Display results
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # 5. Close the session
    session.close()
