from __future__ import annotations
from enum import Enum
from sqlalchemy import ForeignKey, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .message import Message
    from .user import User

class ChatType(str, Enum):
    DIRECT = "direct"
    GROUP = "group"

class Chat(Base, TimestampMixin):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[ChatType] = mapped_column(default=ChatType.DIRECT)
    name: Mapped[str | None] = mapped_column(String(100)) # Только для групп

    members: Mapped[list["Membership"]] = relationship(back_populates="chat")
    messages: Mapped[list["Message"]] = relationship(back_populates="chat")

class Membership(Base):
    __tablename__ = "memberships"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"), primary_key=True)
    
    is_pinned: Mapped[bool] = mapped_column(Boolean, default=False)
    notifications_enabled: Mapped[bool] = mapped_column(Boolean, default=True)

    user: Mapped["User"] = relationship(back_populates="memberships")
    chat: Mapped["Chat"] = relationship(back_populates="members")
