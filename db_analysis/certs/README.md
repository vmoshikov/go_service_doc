# mTLS сертификаты для JDBC

Положите сюда сертификаты для подключения к PostgreSQL через mTLS:

| Файл | Описание |
|------|----------|
| `client.pem` | Клиентский сертификат |
| `client-key.pem` | Приватный ключ клиента |
| `ca.pem` | Сертификат CA (корневой) |

**JDBC URL с mTLS:**
```
jdbc:postgresql://host:5432/dbname?ssl=true&sslmode=verify-full&sslcert=certs/client.pem&sslkey=certs/client-key.pem&sslrootcert=certs/ca.pem
```

**Важно:** Файлы `*.pem` не коммитятся в git (см. `.gitignore`).
