import uuid

from slugify import slugify
from sqlalchemy import event
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Group(DeclarativeBase):
    __tablename__ = 'groups'

    group_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    group_name: Mapped[str] = mapped_column(unique=True)
    group_slug: Mapped[str] = mapped_column(index=True, default_factory=lambda: uuid.uuid4().hex)


@event.listens_for(Group, "before_insert")
@event.listens_for(Group, "before_update")
def generate_slug(mapper, connection, target):
    if target.group_name:
        target.group_slug = slugify(target.group_name)
