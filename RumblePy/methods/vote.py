from requests import post
from RumblePy.Static import Static

def vote(self, postId, vote):
    # 1 for upvote, -1 for downvote
    return post(
        Static.URI.service + "?name=user.rumbles",
        data={"type": "1", "id": postId, "vote": vote},
        cookies={"u_s": self.session}, 
        headers={"User-Agent": Static.Request.user_agent}
        ).json()
