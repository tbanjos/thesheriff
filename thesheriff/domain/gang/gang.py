from typing import NoReturn, Optional


class Gang:
    """Class Gang, the Gang domain entity class.

    :param owner_id: Outlaw's Id, owner of the new Gang.
    :type owner_id: Integer
    :param name: Given name of the Gang.
    :type name: String
    :param gang_id: Optional, Gang Id.
    :type gang_id: Integer
    """

    def __init__(
        self, owner_id: int, name: str, gang_id: Optional[int] = None
    ):
        # FIXME: Verify owner_id is of an existing outlaw
        self.name = name
        self.members = list()
        self.created_raids = 0
        self.owner_id = owner_id
        self.id = gang_id

    def members(self) -> list:
        """Method members.

        :return: The list of Outlaws, members of the Gang.
        :rtype: list
        """
        return self.members

    def add_members(self, members: list) -> NoReturn:
        """Method add_members.

        :param members: List of Outlaws on the Gang.
        :type members: List
        :return: No value returned.
        :rtype: NoReturn
        """
        self.members = members

    def score(self):
        score_gang = 0.0
        for outlaw in self.members:
            score_gang += outlaw.score
        return score_gang
