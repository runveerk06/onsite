# Contributing to OnSite

Read this before starting an issue.

## What the project is

A web application for small field service businesses. The office enters its
workers, equipment, sites and jobs. OnSite builds next week's crew and
equipment assignments, repairs the day when someone calls out, collects hours
through a link the foreman opens with no account, flags records entered twice,
and shows cost per job while the job is still running.

## Stack

| Layer | What we use |
| --- | --- |
| Backend | Python 3.12, FastAPI |
| Frontend | React 18, TypeScript, Vite |
| Database | PostgreSQL 16, run in our own container |
| Local dev | Docker Compose |
| CI | GitHub Actions |

Do not add a hosted service, an authentication provider, or an ORM without
raising it first. Our course grades us on the parts we build, and three of
those categories are not permitted at all.

## Layout

```
backend/app/main.py     endpoints
backend/app/db.py       database connection
backend/tests/          tests
frontend/src/           React screens
db/migrations/          hand written SQL, applied in order
.github/workflows/      CI
```

## Running it

```
docker compose up
```

Web on 5173, API on 8000, database on 5432. The database applies everything in
`db/migrations` the first time it starts.

Tests:

```
cd backend && pytest
```

## Working an issue

1. Pull main first: `git checkout main && git pull`
2. Branch: `git checkout -b feature/5-argon2-hashing` (type, issue number, short name)
3. Build only what the issue asks for. Extra work belongs in its own issue.
4. Commit as you go, not all at the end. A message finishes the sentence
   "this commit will", for example "Hash passwords with argon2 on account creation".
5. Push and open a pull request. Put "Closes #5" in the description so the
   issue closes itself on merge.
6. Someone else reviews and approves. Nobody merges their own work.

## Who owns what

Splitting by area keeps us out of each other's files.

| Area | Owner |
| --- | --- |
| Infrastructure, compose, CI, worker API | Runveer |
| Auth, migrations, backend endpoints | Anoop |
| React screens | Joseph |

If your issue needs a change in someone else's area, ask them rather than
editing it yourself.

## Order of work in sprint one

Some issues block others.

1. #1 compose stack, everything depends on it
2. #4 users table migration, before any auth work
3. #5 password hashing, then #6 sign in endpoint, then #7 redirect, then #8 screen
4. #10 workers migration, before #11 the worker API, before #12 the screen
5. #2 README and #3 CI can happen any time

## Conventions

- Raw SQL for queries. No ORM.
- Migrations are numbered and never edited once merged. Add a new one instead.
- Every endpoint validates its input.
- Secrets never go in the repository. Use environment variables.
- New behavior gets at least one test.

## Definition of Done

An item is done when all of these are true.

- Merged into main through a pull request
- Approved by another member
- Test workflow passed
- New behavior has at least one test
- Every acceptance criterion on the issue is met
- Anything a teammate needs to run it is in the README
- The issue closed itself through the merge
