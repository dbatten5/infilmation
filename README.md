# infilmation

infilmation.co

A React + FastAPI web app to aggregate data from various sources for a given
film.

*information* + *film* = ***infilmation***

## Local deployment

```bash
docker compose -f docker-compose up -d
docker compose exec backend -T alembic upgrade head
```

Now you can navigate to the following URLs:

- Frontend: http://localhost
- Backend OpenAPI docs: http://localhost/api/v1/docs/
