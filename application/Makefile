PWD=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))

gen:
	docker run --rm -v ${PWD}:/src -w /src kjconroy/sqlc generate