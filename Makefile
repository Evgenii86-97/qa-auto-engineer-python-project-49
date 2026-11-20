install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install: build
	uv tool install --force dist/*.whl

lint:
	uv run ruff check src
