"""
儲存user的資料
"""

userdb = []
# userdb


class User:
    """
    user的資料
    """
    uid = ''
    state = 0

    edit_pic_filepath = ''
    edit_pic_editions = []

    def __init__(self, userid):
        super().__init__()
        self.uid = userid
        self.state = 0
        


def getuser(userid):
    """
    由userid取得user資料，沒有就建立一個
    """
    for u in userdb:
        if u.uid == userid:
            return u
    print("使用者",userid,"尚未建立資料，現在建立。")
    newuser = User(userid)
    userdb.append(newuser)
    return newuser