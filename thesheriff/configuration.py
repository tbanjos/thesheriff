import os

import inject
from flask import Flask

from thesheriff.infrastructure.asalto.asalto_mysql_repository import AsaltoMySQLRepository
from thesheriff.infrastructure.banda.banda_mysql_repository import BandaMySQLRepository
from thesheriff.infrastructure.bandido.bandido_mysql_repository import BandidoMySQLRepository
from thesheriff.domain.asalto.asalto_repository import AsaltoRepository
from thesheriff.domain.banda.banda_repository import BandaRepository
from thesheriff.domain.bandido.bandido_repository import BandidoRepository


def configure_application(application: Flask) -> None:
    application.config.update(
        DATABASE_URI=os.getenv('DATABASE_URI')
    )


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(AsaltoRepository, AsaltoMySQLRepository(
            application.config['DATABASE_URI']))
        binder.bind(BandaRepository, BandaMySQLRepository(
            application.config['DATABASE_URI']))
        binder.bind(BandidoRepository, BandidoMySQLRepository(
            application.config['DATABASE_URI']))
    inject.configure(config)
