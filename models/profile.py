from dataclasses import dataclass, field

@dataclass
class Resume:
    text: str

@dataclass
class Profile:
    resume: Resume = field(default_factory=Resume)
    legal_authorization: str= None
    preferences: str= None