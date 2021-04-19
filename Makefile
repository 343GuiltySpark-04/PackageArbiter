
package-arbiter:
		python3 ./setup_scripts.py

make doxygen:
		doxygen ./docs/Doxyfile

make test:
		python3 -m unittests ./tests/unit_tests.py

