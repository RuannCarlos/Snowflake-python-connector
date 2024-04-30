import snowflake.connector, logging
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
logger = logging.getLogger(__name__)

def load_keys(key_path, key_pass) -> bytes:
    logger.info("Loading private key")
    with open(f"/home/ruann/.keys/{key_path}", "rb") as key:
        p_key = serialization.load_pem_private_key(
            key.read(),
            password=key_pass.encode(),
            backend=default_backend()
    )
        
    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())
    return pkb

def create_connection(environment):
    logger.info("Creating connection")
    return snowflake.connector.connect(
        user=environment.user,
        account=environment.account,
        private_key=load_keys(environment.private_key_path, environment.private_key_password),
        role=environment.role,
        region=environment.region
    )

