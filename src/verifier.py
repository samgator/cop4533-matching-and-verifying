import sys
from matcher import get_input, gale_shapely

def verifier(preferences, matches):
    print("To be completed")

def main():
    # Read in preference list and generate matches for verification
    preferences_filepath = sys.argv[1]
    preferences = get_input(preferences_filepath)
    matches = gale_shapely(preferences[0], preferences[1], preferences[2])

    # Print matches for debugging (remove later)
    for i in range(len(matches)):
        if matches[i] != -1:
            print(i + 1, matches[i] + 1)

if __name__ == "__main__":
    main()