from requests import post
from rumble_bot.static import Static

def comment(self, postId, text):
    return post(
        Static.URI.service + "?name=comment.add",
        data={"video": postId, "reply_id": 0, "comment": text, "target": "comment-create-1"}, cookies={"u_s": self.session}).json()
    