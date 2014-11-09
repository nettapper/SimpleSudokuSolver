CC := g++
Warning := -Wall -Wextra -Wconversion

out: Solve.cpp
	$(CC) $(Warning) $< -o $@

clean:
	rm *~ out
