from requests import post
from RumblePy.Static import Static

def delete_comment(self, commentId, isRestore=False):
    return post(
        Static.URI.service + "?name=comment." + ("restore" if isRestore else "delete"),
        data={"comment_id": commentId}, 
        cookies={"u_s": self.session}, 
        headers={"User-Agent": Static.Request.user_agent}
    ).json()
    