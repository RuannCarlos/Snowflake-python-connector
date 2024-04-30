import os, logging
from helper.connector import create_connection
from dotenv import load_dotenv
from model.environment import Environment
from model.logger import ColoredFormatter

logger = logging.getLogger(__name__)

def main():
    env = load_environment()
    conn = create_connection(env)
    logger.info("Connection established")
    test_query(conn)


def load_environment():
    logger.info("Loading environment variables")
    load_dotenv()
    return Environment(
        user=os.getenv('USER'),
        warehouse=os.getenv('WAREHOUSE'),
        account=os.getenv('ACCOUNT'),
        private_key_path=os.getenv('PRIVATE_KEY_PATH'),
        private_key_pass=os.getenv('PRIVATE_KEY_PASSPHRASE'),
        role=os.getenv('ROLE'),
        region=os.getenv('REGION')
    )

def test_query(connection):
    result = connection.cursor().execute("DESC USER w513180")
    logger.info(f"Testing query result: {result}")


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColoredFormatter('%(message)s'))
    logger.addHandler(console_handler)
    main()