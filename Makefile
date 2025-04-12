.PHONY: typing_windows

code_checker_image = pupenkinvas/code-checker:0.1.0

typing_windows:
    docker run --rm --mount type=bind,src=%cd%,dst=/app/ $(code_checker_image) ./run_checks.sh