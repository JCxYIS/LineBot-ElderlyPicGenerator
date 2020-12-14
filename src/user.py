"""
儲存user的資料
"""

__userdb = []
# userdb


class User:
    """
    user的資料
    """
    id = ''
    state = 0

    def __init__(self, id):
        super().__init__()
        self.id = id
        


def getuser(userid):
    for u in __userdb:
        if u.id == userid:
            return u

    print("使用者",userid,"尚未建立資料，現在建立。")
    return User(id)