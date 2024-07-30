from envparse import env
from mubble import API, Dispatch, LoopWrapper, Mubble, Token, logger

from src import middlewares, commands

logger.set_level("INFO")

env.read_envfile(".env")

DB_USERNAME = env.str("DB_USERNAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_ADDRESS = env.str("DB_ADDRESS")
DB_PORT = env.int("DB_PORT")


async def setup_database(): ...


def setup_app() -> Mubble:
    dispatch = Dispatch()
    dps = [*middlewares.dps, *commands.dps]
    for dp in dps:
        dispatch.load(dp)

    loop_wrapper = LoopWrapper(tasks=[setup_database()])

    bot = Mubble(
        api=API(Token.from_env(path_to_envfile=".env")),
        dispatch=dispatch,
        loop_wrapper=loop_wrapper,
    )

    return bot
