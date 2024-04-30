import logging

logger = logging.getLogger(__name__)

class Environment:
    def __init__(self, user:str, warehouse, account, private_key_path, private_key_pass, role, region) -> None:
        self.user = user
        self.warehouse = warehouse
        self.account = account
        self.private_key_path = private_key_path
        self.private_key_password = private_key_pass
        self.role = role
        self.region = region