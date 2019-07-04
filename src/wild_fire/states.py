# coding: utf-8
from bernard import layers

from bernard.analytics import (
    page_view,
)
from bernard.engine import (
    BaseState,
)
from bernard.i18n import translate, intents

from bernard.platforms.telegram import (
    layers as telegram_layers,
)

from bernard.platforms.facebook import (
    layers as fbl,
)

from HonestDistantJavadocs.main import LandsatBisector

class WildFireState(BaseState):
    """
    Root class for Wild Fire.

    Here you must implement "error" and "confused" to suit your needs. They
    are the default functions called when something goes wrong. The ERROR and
    CONFUSED texts are defined in `i18n/en/responses.csv`.
    """

    @page_view('/bot/error')
    async def error(self) -> None:
        """
        This happens when something goes wrong (it's the equivalent of the
        HTTP error 500).
        """

        self.send(layers.Text(translate.ERROR))

    @page_view('/bot/confused')
    async def confused(self) -> None:
        """
        This is called when the user sends a message that triggers no
        transitions.
        """

        self.send(layers.Text(translate.CONFUSED))

    async def handle(self) -> None:
        raise NotImplementedError

class Welcome(WildFireState):
    """
    Welcome the user
    """

    async def handle(self) -> None:
        name = await self.request.user.get_friendly_name()

        keyboardButtons = [
            telegram_layers.KeyboardButton(
            text=translate.YES, 
            choice='yes',
            intent=intents.LETS_PLAY
        ),
        telegram_layers.KeyboardButton(
            text=translate.NO,
            choice='no',
            intent=intents.LETS_NOT_PLAY
        )]

        self.send(
            layers.Text(translate('WELCOME', name=name)),
            telegram_layers.ReplyKeyboard(
                keyboard=[keyboardButtons],
                one_time_keyboard=True
            )
        )

class LetsNotPlay(WildFireState):
    """
    The user is not willing to play
    """

    async def handle(self) -> None:

        self.send(layers.Text(translate.LETS_NOT_PLAY))

class LetsPlay(WildFireState):
    """
    The user wants to play
    """

    async def handle(self) -> None:
        self.send(layers.Text(translate.LETS_PLAY))
