import diagnostics
import sys

def main():
    print("Anemia Scan and Diagnostic Tool")

    try:
        #input handling
        sex_input = input("Enter patients's sex")
        hb_input = float(input("Enter hemoglobin level"))
        
        #logic handling
        result_text, status_color = diagnostics.assess_patient(sex_input, hb_input)

        #Output
        print(f"RESULT: {result_text}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Exiting program.")
        sys.exit()

if __name__ == "__main__":
    main()