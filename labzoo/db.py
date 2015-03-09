# -*- coding: utf-8 -*-

""" I'm the representation of LabZoo's object in the db.
"""

from sqlalchemy import (
    declarative_base,
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import (
    backref,
    relationship,
)


Base = declarative_base()


class LabZooDatabase:
    """ Helpers to initialize the database.
    """

    @staticmethod
    def load_db(path):
        """ I load an existing database or create a new one.
        """
        pass


class SessionModel(Base):
    """ I'm the main object which ties checks and reports.
    """

    __tablename__ = 'session'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __repr__(self):
        return '<Session({0})>'.format(self.name)


class SessionCheckModel(Base):
    """ I'm a check of a session.
    """

    __tablename__ = 'session_check'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    description = Column(String)
    session = relationship("SessionModel", backref=backref('checks',
                                                           order_by=id))

    def __repr__(self):
        return '<SessionCheck({0})>'.format(self.name)


class SessionCheckParamModel(Base):
    """ I'm a parameter of a check.
    """

    __tablename__ = 'session_check_param'

    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=True)
    check = relationship("SessionCheckModel", backref=backref('params',
                                                              order_by=id))

    def __repr__(self):
        return '<SessionCheckParam({0})>'.format(self.name)


class SessionCheckParamValueModel(Base):
    """ I'm a value of a parameter.
    """

    __tablename__ = 'session_check_param_value'

    id = Column(Integer, primary_key=True)
    value = Column(String, primary_key=True)
    param = relationship("SessionCheckParamModel", backref=backref('values',
                                                                   order_by=id))

    def __repr__(self):
        return '<SessionCheckParamValue({0})>'.format(self.value)


class SessionReport(Base):
    """ I'm a report of a session.
    """
    __tablename__ = 'session_report'
