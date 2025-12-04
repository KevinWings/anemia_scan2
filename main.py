import diagnostics
import sys
from termcolor import colored

def main():
    print("Anemia Scan and Diagnostic Tool")

    try:
        #input handling
        sex_input = input("Enter patients's sex")
        hb_input = float(input("Enter hemoglobin level"))
        
        #logic handling
        result_text, status_color = diagnostics.assess_patient(sex_input, hb_input)

        print("\n" + colored(result_text, status_color, attrs=["bold"]))

        #Output
        print(f"RESULT: {result_text}")
    except ValueError as e:
        print(colored(f"Error: {e}"))
    except KeyboardInterrupt:
        print("Exiting program.")
        sys.exit()

if __name__ == "__main__":
    main()