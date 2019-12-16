from typing import NoReturn, List
from thesheriff.domain.gang.gang import Gang
from thesheriff.domain.gang.repository.gang_repository import GangRepository
from thesheriff.domain.outlaw.outlaw import Outlaw


class MockGangRepository(GangRepository):

    def of_id(self, gang_id: int) -> Gang:
        pass

    def add(self, new_gang: Gang) -> NoReturn:
        pass

    def update(self, mod_gang: Gang) -> NoReturn:
        pass

    def remove(self, gang_id: int) -> NoReturn:
        pass

    def all(self) -> List[Gang]:
        gang1 = Gang(1, "Gang1")
        gang2 = Gang(2, "Gang2")
        gang3 = Gang(3, "Gang3")

        outlaw1 = Outlaw("B1", "b1@yopmail.com")
        outlaw2 = Outlaw("B2", "b2@yopmail.com")
        outlaw3 = Outlaw("B3", "b3@yopmail.com")

        members_gang1 = [outlaw1, outlaw2]
        members_gang2 = [outlaw2, outlaw3]
        members_gang3 = [outlaw1, outlaw3]

        gang1.add_members(members_gang1)
        gang2.add_members(members_gang2)
        gang3.add_members(members_gang3)

        return [gang1, gang2, gang3]