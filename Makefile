code_checker = pupenkinvas/code-checker:0.1.0

typing:
	docker run --platform linux/amd64 --rm --mount type=bind,src=$(PWD),dst=/app/ $(code_checker) ./run_checks.sh
