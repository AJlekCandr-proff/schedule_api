from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from sсhedule_api.infrastructure.db.base import Base


class Schedule(Base):
    __tablename__ = 'schedule'
    __table_args__ = (
        CheckConstraint(
            "number_of_lesson > 0",
            name="chk_positive_number_of_lesson"
        ),
    )

    schedule_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number_of_lesson: Mapped[int]
    audience: Mapped[str]
    week_type: Mapped[bool | None]  # Числитель - True, Знаменатель - False, постоянное - None
    is_active: Mapped[bool]
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey(
            "lessons.lesson_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        )
    )
    group_id: Mapped[int] = mapped_column(
        ForeignKey(
            "groups.group_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        )
    )
