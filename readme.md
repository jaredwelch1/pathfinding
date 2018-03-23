# Pathfinding

- This repo contains simple classes for graph implementation in python. Once the graph classes are in a working state, pathfinding algorithms will be written using the graph class.

## TO DO

- Unit testing for graph, node, and edge classes

	- make tests for:
		- proper edge list return from interables (i. e. , edge value when expected vs tuple vs object)

- Pathfinding algorithms implemented, with possible test cases?
- Make file and import other paths using os.dir so that graph library can be imported
- pip stuff?
- visualizations that show the algorithms as they iterate over the graph

## Running tests

- Navigate to the tests directory and run `python -m unittest discover` which will find all files matching test*.py and run them.

- To run specific group of tests, you can do `python -m unittest filename.py`

- Finally, to run a specific test within a test module you can do `python -m unittest filename.test_method`
