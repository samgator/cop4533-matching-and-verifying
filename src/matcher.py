import sys

# Function to read input from a file and parse it into structured data
def get_input(filename):
    with open(filename) as f:
        n = int(f.readline().strip())
    
        # Read hospital and student preferences n times each
        hospital_preferences = []
        for _ in range(n):
            hospital_preferences.append(list(map(int, f.readline().strip().split())))
        student_preferences = []
        for _ in range(n):
            student_preferences.append(list(map(int, f.readline().strip().split())))

        return n, hospital_preferences, student_preferences

# Get filepath from command line arguments and read input
input_filepath = sys.argv[1]
n, hospital_prefs, student_prefs = get_input(input_filepath)

# Prints for debugging (to be removed)
print("n =", n)
print("Hospital preferences:", hospital_prefs)
print("Student preferences:", student_prefs)