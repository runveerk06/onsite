from pathlib import Path

MIGRATIONS = Path(__file__).resolve().parents[2] / "db" / "migrations"


def test_migrations_are_numbered_in_order():
    names = sorted(p.name for p in MIGRATIONS.glob("*.sql"))
    numbers = [int(name.split("_")[0]) for name in names]
    assert numbers == list(range(1, len(numbers) + 1))


def test_users_migration_creates_users_table():
    sql = (MIGRATIONS / "002_create_users.sql").read_text().lower()
    assert "create table users" in sql
    assert "password_hash" in sql
