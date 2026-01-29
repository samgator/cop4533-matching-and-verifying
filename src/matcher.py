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

#function for gale_shapely algorithm based on the lecture slide psuedocode
def gale_shapely(n, hospital_preferences, student_preferences):
    # Initialize and track student index
    hospital_match = [-1]*n
    student_match = [-1]*n
    proposals_sent = [0]*n

    #some hospital is free and hasn't been matched/assigned to every applicant
    while -1 in hospital_match:
        h = hospital_match.index(-1)
        # The hospital has tried proposing to everyone so break
        if proposals_sent[h] >= n:
            break

        #1st applicant (a) on h's list to whom h has not been matched
        ideal_student = hospital_preferences[h][proposals_sent[h]]-1
        proposals_sent[h] += 1

        #if a is free assign h and a 
        if student_match[ideal_student] == -1:
            student_match[ideal_student] = h
            hospital_match[h] = ideal_student
        else:
            h_prime = student_match[ideal_student]
            s_pref_list = student_preferences[ideal_student]
            #a prefers h to their current h'
            if s_pref_list.index(h+1) < s_pref_list.index(h_prime + 1):
                student_match[ideal_student] = h
                hospital_match[h] = ideal_student
                hospital_match[h_prime] = -1
            #a rejects h
            else:
                hospital_match[h] = -1
    return hospital_match

def main():
    # Get filepath from command line arguments and read input
    input_filepath = sys.argv[1]
    n, hospital_prefs, student_prefs = get_input(input_filepath)

    # Prints for debugging (to be removed)
    print("n =", n)
    print("Hospital preferences:", hospital_prefs)
    print("Student preferences:", student_prefs)

    if n == 0:
        return
    
    match_final = gale_shapely(n, hospital_prefs, student_prefs)

    for i in range(n):
        if match_final[i] != -1:
            print(i + 1, match_final[i] + 1)

if __name__ == "__main__":
    main()