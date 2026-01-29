import sys
from matcher import get_input, gale_shapely

# UNUSED: Read test matches to debug the verifier
def read_test_matches(filename):
    matches = []
    with open(filename) as f:
        for line in f:
            h, s = map(int, line.split())
            matches.append(s - 1)
    return matches

def verifier(preferences, matches):
    n, hospital_prefs, student_prefs = preferences

    # Build inverse mapping
    student_to_hospital = [-1] * n
    for h in range(n):
        s = matches[h]
        if s == -1:
            print("INVALID: unmatched hospital", h + 1)
            return False
        if student_to_hospital[s] != -1:
            print("INVALID: student matched twice", s + 1)
            return False
        student_to_hospital[s] = h

    # Build ranking tables
    hospital_rank = [[0]*n for _ in range(n)]
    for h in range(n):
        for i, s in enumerate(hospital_prefs[h]):
            hospital_rank[h][s-1] = i

    student_rank = [[0]*n for _ in range(n)]
    for s in range(n):
        for i, h in enumerate(student_prefs[s]):
            student_rank[s][h-1] = i

    # Check stability
    for h in range(n):
        current_s = matches[h]
        for s in range(n):
            if s == current_s:
                continue

            current_h = student_to_hospital[s]

            if (hospital_rank[h][s] < hospital_rank[h][current_s] and
                student_rank[s][h] < student_rank[s][current_h]):
                print(f"INVALID: Blocking pair ({h+1}, {s+1})")
                return False

    print("VALID STABLE")
    return True

def main():
    # Read in preference list and generate matches for verification
    preferences_filepath = sys.argv[1]
    try:
        preferences = get_input(preferences_filepath)
        matches = gale_shapely(preferences[0], preferences[1], preferences[2])
    except Exception:
        print("Error: input not in expected format")
        return

    # Run verifier on generated matches
    try:
        verifier(preferences, matches)
    except Exception as e:
        print(f"Error during verification: {e}")

if __name__ == "__main__":
    main()