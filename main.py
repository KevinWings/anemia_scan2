import diagnostics
import sys
from termcolor import colored
import datetime

def save_report(result):
    with open("patient_history.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m%d %H:%M")
        f.write(f"[{timestamp}]{result}\n")
        print("Report saved successfully")

def main():
    print("Anemia Scan and Diagnostic Tool")

    try:
        #input handling
        sex_input = input("Enter patients's sex")
        hb_input = float(input("Enter hemoglobin level"))
        
        #logic handling
        result_text, status_color = diagnostics.assess_patient(sex_input, hb_input)

        print("\n" + colored(result_text, status_color, attrs=["bold"]))

        save_report(result_text)

        #Output
        print(f"RESULT: {result_text}")
    except ValueError as e:
        print(colored(f"Error: {e}"))
    except KeyboardInterrupt:
        print("Exiting program.")
        sys.exit()

if __name__ == "__main__":
    main()