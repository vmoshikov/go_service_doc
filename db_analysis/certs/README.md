# mTLS сертификаты для PostgreSQL

Подключение: **mTLS (сертификаты)** + **логин/пароль** (PostgreSQL auth).

Положите сюда сертификаты для mTLS:

| Файл | Описание |
|------|----------|
| `client.pem` | Клиентский сертификат |
| `client-key.pem` | Приватный ключ клиента |
| `ca.pem` | Сертификат CA (корневой) |

**Использование:**

Логин и пароль — в URL или отдельно:

```bash
# В URL
export DATABASE_URL="postgresql://user:password@host:5432/dbname"

# Или через переменные (пароль не в process list)
export DATABASE_URL="postgresql://host:5432/dbname"
export DB_USER=user
export DB_PASSWORD=password

python db_analyzer.py
```

Сертификаты из `certs/` подхватываются автоматически. Явные пути:

```bash
python db_analyzer.py --db-url "postgresql://user:password@host:5432/dbname" \
  --ssl-cert certs/client.pem --ssl-key certs/client-key.pem --ssl-rootcert certs/ca.pem
```

**Важно:** Файлы `*.pem` не коммитятся в git (см. `.gitignore`).
