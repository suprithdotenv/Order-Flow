from sqlalchemy.orm import Mapped,mapped_column
from app.database.base import Base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone

from sqlalchemy import String, Text, Boolean, DateTime

import uuid

"""

1. Mapped
- Tells SQLAlchemy that a Python attribute is part of ORM mapping.
- Specifies the expected Python data type.
- Helps with type checking and IDE support.

2. mapped_column()
- Defines the database column.
- Specifies its SQL data type and constraints.
- Defines properties like primary_key, nullable, default, etc.

"""



class Restaurant(Base):

    __tablename__ = "restaurants"



    id:Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,

    )


    name:Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )


    description:Mapped[str|None] = mapped_column(
        Text,
        nullable = True
    )


    address:Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    is_active:Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )



    created_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )