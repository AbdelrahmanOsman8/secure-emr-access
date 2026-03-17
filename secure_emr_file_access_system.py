# --------------------------------------------------------
# secure_emr_file_access_system.py
# Secure Electronic Medical Record (EMR) Access Simulation
# --------------------------------------------------------

emr_file = None
max_attempts = 5

while max_attempts > 0:
    try:
        print("\n=== Secure EMR Access System ===")
        print(f"Access Attempts Remaining: {max_attempts}")
        print("Enter the full path of the patient's medical record file.")
        print("Example: D:\\HospitalSystem\\Records\\patient123.txt")

        file_path = input("Medical Record Path => ").strip()

        emr_file = open(file_path, "r")

        print("\n--- Patient Medical Record ---")
        print(emr_file.read())

        print("\nAccess Granted Successfully.")
        break

    except FileNotFoundError:
        print("Medical Record Not Found. Please verify the file path.")
        max_attempts -= 1

    except PermissionError:
        print("Access Denied. You do not have permission to view this record.")
        max_attempts -= 1

    except Exception as e:
        print("System Error Occurred:", e)
        max_attempts -= 1

    finally:
        if emr_file is not None:
            emr_file.close()
            print("Medical Record File Closed Securely.")

else:
    print("\nMaximum access attempts reached. Account temporarily locked.")
