__all__ = ["InteractionListener"]


class InteractionListener(object):
    def childInteractionUpdated(self):
        # type: () -> None
        raise NotImplementedError
