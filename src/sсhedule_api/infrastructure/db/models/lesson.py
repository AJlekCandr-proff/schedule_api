import uuid

from slugify import slugify
from sqlalchemy import event
from sqlalchemy.orm import Mapped, mapped_column

from sсhedule_api.infrastructure.db.base import Base


class Lesson(Base):
    __tablename__ = 'lessons'

    lesson_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lesson_name: Mapped[str] = mapped_column(unique=True)
    lesson_slug: Mapped[str] = mapped_column(index=True, default_factory=lambda: uuid.uuid4().hex)


@event.listens_for(Lesson, "before_insert")
@event.listens_for(Lesson, "before_update")
def generate_slug(mapper, connection, target):
    if target.lesson_name:
        target.lesson_slug = slugify(target.lesson_name)
