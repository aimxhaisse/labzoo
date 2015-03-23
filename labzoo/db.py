# -*- coding: utf-8 -*-

""" I'm the representation of LabZoo's object in the db.
"""

from datetime import (
    datetime,
)
from sqlalchemy import (
    create_engine,
    Column,
    DateTime,
    Integer,
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    backref,
    sessionmaker,
    relationship,
)
from sqlalchemy.orm.exc import (
    NoResultFound,
)
from sqlalchemy.ext.declarative import (
    declarative_base,
)

Base = declarative_base()


class Database:
    """ Helpers to initialize the database.
    """

    @staticmethod
    def load_db(path):
        """ I load an existing database or create a new one.
        """
        url = 'sqlite:///{0}'.format(path)
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        return sessionmaker(bind=engine)


class SessionTemplateModel(Base):
    """ I'm the main class which holds sessions.
    """

    __tablename__ = 'session_template'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    sessions = relationship('SessionModel', backref='template')
    reports = relationship('SessionReportModel', backref='template')

    @staticmethod
    def get_or_create(sess, name, description):
        """ I get the Template pointed by `name` or create a new template.

        If there is a matching Template in the database with a
        different description, its description gets updated by
        `description`.
        """
        try:
            template = sess.query(SessionTemplateModel) \
                .filter(SessionTemplateModel.name == name).one()
            if template.description != description:
                template.description = description
                sess.commit()
            return template
        except NoResultFound, e:
            template = SessionTemplateModel(name=name, description=description)
            sess.add(template)
            sess.commit()
            return template

    def __repr__(self):
        return '<SessionTemplate({0})>'.format(name)


class SessionModel(Base):
    """ I'm an instance of a Template which ties checks and reports.
    """

    __tablename__ = 'session'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now())
    template_id = Column(Integer, ForeignKey('session_template.id'))
    state = Column(String)
    reports = relationship('SessionCheckModel', backref='session')

    # Available states.
    STATE_IN_PROGRESS = 'in_progress'
    STATE_COMPLETED = 'completed'
    STATE_FAILED = 'failed'

    def __repr__(self):
        return '<Session(#{0} - {1})>'.format(self.id, self.template.name)


class SessionCheckModel(Base):
    """ I'm a check of a session.
    """

    __tablename__ = 'session_check'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    description = Column(String)
    session_id = Column(Integer, ForeignKey('session.id'))
    params = relationship('SessionCheckParamModel', backref='check')

    def __repr__(self):
        return '<SessionCheck({0})>'.format(self.name)


class SessionCheckParamModel(Base):
    """ I'm a parameter of a check.
    """

    __tablename__ = 'session_check_param'

    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=True)
    check_id = Column(Integer, ForeignKey('session_check.id'))
    values = relationship('SessionCheckParamValueModel', backref='param')

    def __repr__(self):
        return '<SessionCheckParam({0})>'.format(self.name)


class SessionCheckParamValueModel(Base):
    """ I'm a value of a parameter.
    """

    __tablename__ = 'session_check_param_value'

    id = Column(Integer, primary_key=True)
    value = Column(String, primary_key=True)
    param_id = Column(Integer, ForeignKey('session_check_param.id'))

    def __repr__(self):
        return '<SessionCheckParamValue({0})>'.format(self.value)


class SessionReportModel(Base):
    """ I'm a report of a session.
    """

    __tablename__ = 'session_report'

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey('session_template.id'))
