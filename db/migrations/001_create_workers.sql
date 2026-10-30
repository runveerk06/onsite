CREATE TABLE workers (
    id          SERIAL PRIMARY KEY,
    full_name   TEXT NOT NULL,
    hourly_rate NUMERIC(8, 2) NOT NULL CHECK (hourly_rate >= 0),
    archived    BOOLEAN NOT NULL DEFAULT FALSE,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO workers (full_name, hourly_rate) VALUES
    ('Jose Martinez', 32.00),
    ('Mike Donnelly', 28.50),
    ('Ray Okafor', 35.75);
