import inject
from typing import NoReturn
from thesheriff.domain.raid.repository.raid_repository import RaidRepository
from thesheriff.domain.outlaw.repository.outlaw_repository import OutlawRepository
from thesheriff.domain.outlaw.score import Score


class RateRaid:
    """Class RateRaid implements the Raid rating use case.
    :param outlaw_repository: Repository managing Outlaw domain entities.
    :type outlaw_repository: OutlawRepository.
    :param raid_repository: Repository managing Raid domain entities.
    :type raid_repository: RaidRepository.
    """

    @inject.autoparams()
    def __init__(
        self, outlaw_repository: OutlawRepository,
        raid_repository: RaidRepository
    ):
        self.__raid_repository = raid_repository
        self.__outlaw_repository = outlaw_repository

    def execute(
            self, raid_id: int, outlaw_id: int, score: Score
    ) -> NoReturn:
        """execute is the actual action of the Raid rating use case.
        :param raid_id: ID of the Raid to be rated
        :type raid_id: Integer.
        :param outlaw_id: ID of the Outlaw performing the action.
        :type outlaw_id: Integer.
        :param score: Raid's score.
        :type score: Score.
        :returns: NoReturn -- no value returned.
        """
        outlaw = self.__outlaw_repository.of_id(outlaw_id)
        raid = self.__raid_repository.of_id(raid_id)

        if outlaw:
            raid.add_rate(score.value())
            # TODO(all): do we really want to persist the score? I guess we do.
            # If so, we'd need to re-add the update method and arrive to
            # consensus on how to really make the update, e.g.: raid_id, dict({'score': value})
            # Something like the above example would make the update way easier to handle.
            self.__raid_repository.update(raid)