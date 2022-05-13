DROP TABLE IF EXISTS budgets;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS master_categories;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS transactions;

CREATE TABLE budgets (
    uuid TEXT PRIMARY KEY,
    label TEXT UNIQUE NOT NULL
);

CREATE TABLE accounts (
    uuid TEXT PRIMARY KEY,
    label TEXT UNIQUE NOT NULL,
    account_type TEXT NOT NULL,
    budget_type TEXT NOT NULL,
    budget TEXT,
    FOREIGN KEY(budget) REFERENCES budgets(uuid)
);

CREATE TABLE master_categories (
    uuid TEXT PRIMARY KEY,
    label TEXT UNIQUE NOT NULL,
    budget TEXT,
    FOREIGN KEY(budget) REFERENCES budgets(uuid)
);

CREATE TABLE categories (
    uuid TEXT PRIMARY KEY,
    label TEXT UNIQUE NOT NULL,
    amount REAL NOT NULL,
    master_catergory TEXT,
    FOREIGN KEY(master_catergory) REFERENCES master_categories(uuid)
);

CREATE TABLE transactions (
    uuid TEXT PRIMARY KEY,
    ts TEXT NOT NULL,
    payee TEXT NOT NULL,
    memo TEXT,
    outflow REAL,
    inflow REAL,
    cleared INTEGER DEFAULT 0,
    account TEXT,
    category TEXT,
    FOREIGN KEY(account) REFERENCES accounts(uuid),
    FOREIGN KEY(category) REFERENCES categories(uuid)
);