from enum import Enum


class IdentifyAs(Enum):
    female = "female"
    transgender = "transgender female"


class InteractionType(Enum):
    direct_message = "direct message"


class ReactionType(Enum):
    reported = "reported"


class ExperiencedFeeling(Enum):
    afraid = "afraid"


class Perpetrator(Enum):
    follower = "follower"
