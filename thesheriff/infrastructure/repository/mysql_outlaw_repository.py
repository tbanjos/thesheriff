"""
thesheriff.infrastructure.repository.mysql_outlaw_respository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements Outlaw MySQL Repository.
"""
from thesheriff.domain.outlaw.repository.outlaw_repository import \
    OutlawRepository
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.outlaw_factory import OutlawFactory
from sqlalchemy import create_engine, MetaData, Table
from typing import NoReturn, List


class MySQLOutlawRepository(OutlawRepository):
    """MySQLOutlawRepository implements persistence for Outlaw on MySQL.

    :param database_uri: URI for connecting to MySQL
    :type database_uri: String
    :param meta: MetaData object shared across all MySQL repositories.
    :type meta: sqlalchemy.MetaData
    :param outlaw_table: Table object, represents the Outlaw table in MySQL.
    :type outlaw_table: sqlalchemy.Table
    """

    def __init__(self, database_uri: str, meta: MetaData, outlaw_table: Table):
        engine = create_engine(database_uri, pool_pre_ping=True)
        self.__connection = engine.connect()
        self.__outlaw_table = outlaw_table
        meta.create_all(self.__connection)

    def of_id(self, outlaw_id: int) -> Outlaw:
        """of_id searches for a Outlaw matching outlaw_id.

        :param outlaw_id: ID of the Outlaw to be returned.
        :type outlaw_id: Integer
        :return: Outlaw object.
        :rtype: Outlaw
        """
        query = self.__outlaw_table.select().where(
            self.__outlaw_table.c.id == outlaw_id)
        result = self.__connection.execute(query)
        row = result.fetchone()
        return OutlawFactory.create(
            row.name,
            row.email,
            row.id
        )

    def add(self, new_outlaw: Outlaw) -> Outlaw:
        """Method add persists a new Outlaw to MySQL.

        :param new_outlaw: Object with the new Outlaw details
        :type new_outlaw: Outlaw
        :return: The persisted Outlaw.
        :rtype: Outlaw
        """
        query = self.__outlaw_table.insert().values(
            name=new_outlaw.name, email=new_outlaw.email
        )
        result = self.__connection.execute(query)
        new_outlaw.id = result.lastrowid
        return new_outlaw

    def update(self, mod_outlaw: Outlaw) -> NoReturn:
        """Method update modifies existing Outlaw.

        :param mod_outlaw: Object with Outlaw details to be updated.
        :type mod_outlaw: Outlaw
        :return: No returned value.
        :rtype: NoReturn.
        """
        query = self.__outlaw_table.update().where(
            self.__outlaw_table.c.id == mod_outlaw.id).values(**mod_outlaw)
        self.__connection.execute(query)

    def remove(self, outlaw_id: int) -> NoReturn:
        """Method remove deletes existing Outlaw.

        :param outlaw_id: Id of the Outlaw to be removed.
        :type outlaw_id: Integer
        :return: No returned value.
        :rtype: NoReturn
        """
        query = self.__outlaw_table.delete().where(
            self.__outlaw_table.c.id == outlaw_id)
        self.__connection.execute(query)

    def get_friends(self, outlaw_id: int) -> List[Outlaw]:
        """Method get_Friends lists outlaw's friends.

        :param outlaw_id: Id of the Outlaw to list his friends
        :type outlaw_id: Integer
        :return: List of outlaw friends.
        :rtype: List[Outlaw]
        """
        query = self.__outlaw_table.select().where(
            self.__outlaw_table.c.id == outlaw_id)
        return self.__connection.execute(query)

    def all(self) -> List[Outlaw]:
        """all returns all Outlaws stored on MySQL.

        :return: List Outlaw objects.
        :rtype: List[Outlaw]
        """
        # TODO(all): return OutlawCollection (TBI)
        query = self.__outlaw_table.select()
        rows = self.__connection.execute(query)
        outlaws = list()
        for row in rows:
            outlaw = OutlawFactory.create(row.name, row.email, row.id)
            outlaws.append(outlaw)
        return outlaws
