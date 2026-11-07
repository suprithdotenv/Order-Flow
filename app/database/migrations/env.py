
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool

from app.core.config import settings
from app.database.base import Base
from app.database.session import engine

from app.modules.restaurants.models import Restaurant



# Alembic configuration
config = context.config

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Register SQLAlchemy metadata for autogeneration
target_metadata = Base.metadata

# Load database URL from .env
config.set_main_option(
    "sqlalchemy.url",
    settings.DATABASE_URL.replace("%", "%%")
)


def run_migrations_offline() -> None:
    """Run migrations without a database connection."""

    url = settings.DATABASE_URL

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations using an active database connection."""

    with engine.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
