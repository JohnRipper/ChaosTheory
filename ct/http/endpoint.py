class Endpoint:
    BASE = "https://discordapp.com/api"
    VERSION = '6'

    # ENDPOINTS
    gateway = ''.join([BASE, "/gateway"])
    _users = ''.join([BASE, "/users/{user_id}"])

    def users(self, user_id):
        return self._users.format(user_id=user_id)
