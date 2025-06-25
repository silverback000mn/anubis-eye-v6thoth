CREATE TABLE divine_accounts (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT ENCRYPTED,
    creation_date TEXT DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('active', 'shadowban', 'banned')),
    quality_score INTEGER DEFAULT 0
);

CREATE TABLE proxy_rotation (
    proxy_id INTEGER PRIMARY KEY,
    address TEXT NOT NULL,
    last_used TEXT,
    success_rate REAL
);
