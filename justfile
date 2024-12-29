# list all recipes
default:
  @just --list

# install dependencies
setup:
  cd frontend && npm install
  ln -sf ../node_modules/flowbite/dist/flowbite.min.js frontend/assets/flowbite.min.js
  cd backend && uv sync --all-extras --dev

# watch tailwind
watch-tailwind:
  cd frontend && npx tailwindcss -i ./input.css -o ./assets/tailwind.css --watch

# watch dioxus
watch-dioxus:
  cd frontend && dx serve

# watch the backend
watch-backend:
  cd backend && uv run fastapi dev src/millie/_internal/scripts/main.py

# build docs
docs:
  rm -rf backend/docs/build backend/docs/source/_autosummary
  cd backend && uv run make -C docs html
  echo Docs are in $PWD/backend/docs/build/html/index.html

# run code checks
check:
  #!/usr/bin/env bash

  error=0
  trap error=1 ERR

  echo
  (set -x; cd backend && uv run ruff check src/ tests/ docs/source/ examples/ )
  test $? = 0

  echo
  ( set -x; cd backend && uv run ruff format --check src/ tests/ docs/source/ examples/ )
  test $? = 0

  echo
  ( set -x; cd backend && uv run mypy src/ tests/ docs/source/ examples/ )
  test $? = 0

  echo
  ( set -x; cd backend && uv run pytest )
  test $? = 0

  echo
  ( set -x; cd backend && rm -rf docs/build docs/source/_autosummary; uv run make -C docs doctest )
  test $? = 0

  test $error = 0

# auto-fix code issues
fix:
  cd backend && uv run ruff format src/ tests/ docs/source/ examples/
  cd backend && uv run ruff check --fix src/ tests/ docs/source/ examples/
