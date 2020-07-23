import dataclasses


@dataclasses.dataclass
class UserDTO:
    user_id: int
    name: str
    profile_pic_url: str
