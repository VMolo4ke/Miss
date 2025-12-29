from __future__ import annotations
from enum import Enum
from sqlalchemy import ForeignKey, Text, String, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, TimestampMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .chat import Chat

class MessageType(str, Enum):
    TEXT = "text"
    PHOTO = "photo"
    VIDEO = "video"
    VOICE = "voice"
    VIDEO_NOTE = "video_note" # "Кружочки"

class Message(Base, TimestampMixin):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"), index=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    type: Mapped[MessageType] = mapped_column(default=MessageType.TEXT)
    
    # Текст сообщения (для поиска используем индекс ниже)
    content: Mapped[str | None] = mapped_column(Text)
    
    # Путь к медиафайлу в хранилище (S3/сервер)
    file_url: Mapped[str | None] = mapped_column(String(255))
    file_size: Mapped[int | None] = mapped_column()
    duration: Mapped[int | None] = mapped_column() # Для голосовых/видео

    chat: Mapped["Chat"] = relationship(back_populates="messages")
    
    # Индекс для быстрого поиска по сообщениям
    __table_args__ = (
        Index("ix_message_content_fulltext", "content"),
    )
