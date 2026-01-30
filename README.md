# cop4533-matching-and-verifying
Programming Assignment 1

Sam Morsics 85201061
Jayden Ollis 61598910

Instructions to compile/build your code (if applicable).
Not Applicable

Instructions to run the matcher and the verifier, including example commands.
To run the matcher on an input file and save the results to /data, use a command like so:
python src/matcher.py tests/example.in
To run the verifier and check for stability, use a command in the terminal like so:
python src/verifier.py tests/example.in

Any assumptions (input/output format, dependencies, etc.).
Input:
It is assumed that line one of input files contain n, where the next n lines is the preference list for hospitals where the 
ranks are seperated by a single space and different hospitals are seperated by a new line. The next n lines after that 
are a preferences list for students following the same formatting. Preference lists are assumed to be a complete permutation from 1 to n 
Output:
It is assumed that matcher has write permission to the /data folder, where it will output a file containing lines that represent
each pair like so: 
HospitalID StudentID
The verifier assumes that a stable match means there are no blocking pairs, where a blocking pair is any (H,S) who both prefer
eachother over their currently assigned partners.
The algorithm is hospital proposing, so in cases where multiple stable matchings are possible the hospital optimal result is produced

Your graph and solution to Task C.
The graphs are located in the data folder labeled matcher_runtime_plot.ong and verifier_runtime_plot.png.
The solution to part C was to generate tests of vastly varying sizes using scripts, then benchmark ran the tests and wrote out 
data regarding run time, and then finally plot used the results from benchmark to actually create the graphs 