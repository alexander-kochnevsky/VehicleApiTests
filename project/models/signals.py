from typing import List

from project.models.signal import Signal


class Signals:
    def __init__(self, signals: List[Signal]):
        self.signals = signals

    def __eq__(self, other):
        return self.signals == other.signals

    def __repr__(self):
        return f'{self.signals}'

    def __getitem__(self, item: int):
        return next(x for x in self.signals if x.sig_id == item)
