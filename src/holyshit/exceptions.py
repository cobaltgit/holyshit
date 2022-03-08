class ContentUnavailable(Exception):
    """Raises when fetching content fails or type is invalid."""


class ClosedSessionError(Exception):
    """Raises when attempting to interact with a closed client instance."""
