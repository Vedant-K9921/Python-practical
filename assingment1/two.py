with open("sample.txt", "r") as file:
    lines = file.readlines()

print(f"Total number of lines: {len(lines)}")

if len(lines) >= 2:
    print(f"2nd line: {lines[1].strip()}")
else:
    print("The file has fewer than 2 lines.")

if len(lines) >= 4:
    print(f"4th line: {lines[3].strip()}")
else:
    print("The file has fewer than 4 lines.")