failed_logins = 0

with open("sample.log", "r") as file:
    for line in file:
        if "4625" in line:
            failed_logins += 1
            print("FAILED LOGIN:", line.strip())

print("\nTotal failed login attempts:", failed_logins)

if failed_logins >= 3:
    print("ALERT: Possible brute force activity detected!")
