import asyncio
from logging.config import fileConfig
import os
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context

from models import Base 

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 2. Укажите метаданные моделей
target_metadata = Base.metadata

# 3. Добавьте поддержку асинхронности в функцию run_migrations_online
async def run_migrations_online() -> None:
    # Берем URL из переменной окружения, как в приложении
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = os.getenv("DATABASE_URL")

    connectable = async_engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_offline() -> None:
    url = os.getenv("DATABASE_URL")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
