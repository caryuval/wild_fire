# coding: utf-8

from bernard.engine import triggers

from bernard.engine.transition import Transition

from bernard.i18n import intents

from .states import *

transitions = [
    Transition(
        dest=Welcome,
        factory=triggers.Text.builder(intents.WELCOME),
    ),
    Transition(
        dest=LetsNotPlay,
        origin=Welcome,
        factory=triggers.Choice.builder('no'),
    ),
    Transition(
        dest=LetsPlay,
        origin=Welcome,
        factory=triggers.Choice.builder('yes'),
    ),
]
