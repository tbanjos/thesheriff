from tests.mock_raid_repository import MockRaidRepository
from tests.mock_outlaw_repository import MockOutlawRepository
from thesheriff.application.outlaw.rate_raid import RateRaid
from thesheriff.domain.raid.raid import Raid
from thesheriff.domain.outlaw.outlaw import Outlaw
from thesheriff.domain.outlaw.score import Score


def test_rate_raid():
    outlaw_repository = MockOutlawRepository()
    outlaw = Outlaw(1, None, None)
    outlaw_repository.add(outlaw)

    raid_repository = MockRaidRepository()
    raid = Raid("very nice restaurant", None, None, None, None)
    raid_repository.add(raid)

    rate_raid = RateRaid(outlaw_repository, raid_repository)
    rate_raid.execute(1, 0, Score(5, 6, 7, 5.5))
    rate_raid.execute(1, 0, Score(7, 8.5, 8, 9))

    assert 2 == len(raid.rates)
    assert 5.875 == raid.rates[0]
    assert 8.125 == raid.rates[1]
