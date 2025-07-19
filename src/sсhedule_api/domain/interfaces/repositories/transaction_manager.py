from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession


class TransactionManager(Protocol):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def flush(self) -> None: ...

    async def rollback(self) -> None: ...

    async def commit(self) -> None: ...
