# OnSite

A web application for small field service businesses. OnSite builds next week's
crew and equipment assignments, repairs the day when workers call out, collects
hours through a link the foreman opens with no account, and flags records that
were entered twice.

## Running the stack locally

You need Docker Desktop installed. Nothing else.

```
docker compose up
```

That brings up three containers.

| Service | Address | What it is |
| --- | --- | --- |
| web | http://localhost:5173 | The React client |
| api | http://localhost:8000 | The FastAPI server |
| db | localhost:5432 | PostgreSQL with our migrations applied |

The database loads every file in `db/migrations` the first time it starts, so
the workers table exists with a few sample rows already in it. Open
http://localhost:5173 and you should see those workers listed.

To start over with an empty database:

```
docker compose down -v
docker compose up
```

## Running the tests

```
cd backend
pip install -r requirements.txt
pytest
```

The same tests run automatically on every pull request.

## How we work

All work lands on main through a pull request. Nobody pushes to main directly.
Every pull request needs one approving review from another member and a passing
test run before it can merge.

Branches are named by type and issue number, for example
`feature/12-signin-endpoint` or `fix/27-overtime-rounding`.

## Layout

```
backend/            FastAPI server
  app/main.py       Endpoints
  app/db.py         Database connection
  tests/            Tests
frontend/           React and TypeScript client
  src/App.tsx       Worker list screen
db/migrations/      Hand written SQL migrations, applied in order
.github/workflows/  CI that runs on every pull request
```
