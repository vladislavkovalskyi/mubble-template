from mubble import ABCMiddleware, CallbackQuery, Dispatch, Message
from mubble.bot.dispatch.context import Context


dp = Dispatch()


@dp.message.register_middleware()
class MessageContextMiddleware(ABCMiddleware[Message]):
    async def pre(self, event: Message, ctx: Context) -> bool:
        return True


@dp.callback_query.register_middleware()
class CallbackContextMiddleware(ABCMiddleware[CallbackQuery]):
    async def pre(self, event: CallbackQuery, ctx: Context) -> bool:
        return True
