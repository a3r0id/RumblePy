from requests import post
from rumble_bot.Static import Static

def reply(self, postId, commentId, text):
    return post(
        Static.URI.service + "?name=comment.add",
        data={"video": postId, "reply_id": commentId, "comment": text, "target": f"comments-reply-{commentId}"}, 
        cookies={"u_s": self.session}, 
        headers={"User-Agent": Static.Request.user_agent}
    ).json()
    