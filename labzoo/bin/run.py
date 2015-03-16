# -*- coding: utf-8 -*-

import argparse

from labzoo import (
    Database,
    SessionConfig,
    SessionModel,
    TemplateModel,
)


class Run(object):
    """ I manage the completion of a session on a host.
    """

    def __init__(self, mksess, host, conf):
        self.host = host
        self.mksess = mksess
        self.conf = conf
        self.template = TemplateModel.get_or_create(mksess, self.conf.name,
                                                    self.conf.description)
        sess = self.mksess()
        self.model = SessionModel(template=self.template)
        sess.add(self.model)
        sess.commit()

    def prepare(self):
        """ I prepare the environment for the session.
        """

    def collect_environment(self):
        """ I collect various environment data on the remote host.
        """

    def execute(self):
        """ I execute the serie of checks on the remote host.
        """

    def cleanup(self):
        """ I cleanup everything I've created on the remote host
        """


def main():
    parser = argparse.ArgumentParser(
        description='run LabZoo checks on remote targets'
    )
    parser.add_argument('config', help='path to the YAML file describing the'
                        'check to run')
    parser.add_argument('database', help='path to the database file of the '
                        'session')
    parser.add_argument('hosts', help='servers to run the session on',
                        nargs='+')
    args = parser.parse_args()

    conf = SessionConfig.load_from_file(args.config)
    db_session = Database.load_db(args.database)
    for host in args.hosts:
        run = Run(db_session, host, conf)
        try:
            run.set_state(SessionModel.STATE_IN_PROGRESS)
            run.prepare()
            run.collect_environment()
            run.execute()
            run.set_state(SessionModel.STATE_COMPLETED)
        except:
            run.set_state(SessionModel.STATE_FAILED)
        run.cleanup()
        db_session.commit()
