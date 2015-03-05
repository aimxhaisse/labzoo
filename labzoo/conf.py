# -*- coding: utf-8 -*-

""" I'm the representation of a LabZoo YAML configuration file.
"""

import yaml


class SessionConfig(object):
    """ I'm LabZoo's configuration file, pleased to meet you.
    """

    @staticmethod
    def load_from_file(path):
        """ I create a SessionConfig from a YAML file pointed by path.
        """
        with open(path, 'r') as stream:
            return SessionConfig.load_from_dict(yaml.load(stream))

    @staticmethod
    def load_from_dict(raw):
        """ I create a SessionConfig from a Python dictionary.
        """
        session = SessionConfig()
        session.name = raw['name']
        session.description = raw['description']
        for check in raw['checks']:
            session.checks.append(SessionCheckConfig.load_from_dict(check))
        return session

    def __init__(self):
        """ I build an empty SessionConfig.
        """
        self.name = None
        self.description = None
        self.checks = []
        self.report = None


class SessionCheckConfig(object):
    """ I'm the configuration of a check.
    """

    @staticmethod
    def load_from_dict(raw):
        """ I create a SessionCheckConfig from a Python dictionary.
        """
        check = SessionCheckConfig()
        check.name = raw['name']
        check.description = raw['description']
        check.type = raw['type']
        for param in raw.get('params', []):
            check.params.append(SessionCheckParamsConfig.load_from_dict(param))
        return check

    def __init__(self):
        """ I build an empty SessionCheckConfig.
        """
        self.name = None
        self.description = None
        self.type = None
        self.params = []


class SessionCheckParamsConfig(object):
    """ I'm a combination of parameters for a check.
    """

    @staticmethod
    def load_from_dict(raw):
        """ I create a SessionCheckParamsConfig from a Python dictionary.
        """
        param = SessionCheckParamsConfig()
        for name, value in raw.iteritems():
            param.values[name] = value
        return param

    def __init__(self):
        """ I build an empty SessionCheckParamsConfig.
        """
        self.values = {}
