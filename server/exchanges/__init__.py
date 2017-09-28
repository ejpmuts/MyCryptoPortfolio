import abc


class Exchange:
    __metaclass__ = abc.ABCMeta

    def get_pairs(self):
        """Returns the pairs as a dict."""
        raise NotImplementedError()
