SERVICE_NAME=app
SERVICE_PORT=18000
pwd=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))

gen:
	docker run --rm -v $(pwd):/src -w /src sqlc/sqlc generate