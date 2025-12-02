# create constants to avoid any changes

CRITICAL_THRESHOLD_MALE = 7.0
LOW_THRESHOLD_MALE = 13.0

CRITICAL_THRESHOLD_FEMALE = 7.5
LOW_THRESHOLD_FEMALE = 12.0

def assess_patient(sex, hb_level):
    normalized_sex = sex.strip().lower()

    if normalized_sex == "male":
        return check_male(hb_level)
    elif normalized_sex == "female":
        return check_female(hb_level)
    else:
        raise ValueError (f"Unknown biological sex: {sex}.")

def check_male(hb_level):
    if hb_level < CRITICAL_THRESHOLD_MALE:
        return "Critical hemoglobin levels", "red"
    elif hb_level < LOW_THRESHOLD_MALE:
        return "Low hemoglobin levels", "yellow"
    return "Normal hemogloobin levels", "green" 

def check_female(hb_level):
    if hb_level < CRITICAL_THRESHOLD_FEMALE:
        return "Critical hemoglobin levels", "red"
    elif hb_level < LOW_THRESHOLD_FEMALE:
        return "Low hemoglobin levels", "yellow"
    return "Normal hemogloobin levels", "green" 