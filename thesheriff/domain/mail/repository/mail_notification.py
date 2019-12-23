import abc
from thesheriff.domain.mail.mail import Mail


class MailNotification(abc.ABC):

    @abc.abstractmethod
    def send(self,  mail: Mail):
        pass
