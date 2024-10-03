# Dymles Ganz
# Nuclei output format remover

import os
import time

def roast_the_targets(filename, option):
    output_filename = "nuclei.txt"

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        print("\n🔥 Running your targets... Hold tight!\n")
        time.sleep(1)

        with open(output_filename, 'w') as output_file:
            for idx, line in enumerate(lines):
                parts = line.split()
                if len(parts) > 0:
                    full_url = parts[-1]

                    if option == "1":
                        protocol, rest = full_url.split("//", 1)
                        domain = rest.split("/", 1)[0]
                        print(f"Processed URL-{idx + 1}: {protocol}//{domain}")
                        output_file.write(f"{protocol}//{domain}\n")
                    elif option == "2":
                        print(f"Processed FULL-{idx + 1}: {full_url}")
                        output_file.write(f"{full_url}\n")

        print(f"\n✅ Done man! Saved in {output_filename}..")

    except FileNotFoundError:
        print(f"❌ Ugh... File {filename} not found.")
    except Exception as e:
        print(f"❌ Whoops... Something went wrong. Try again!")


def roast_controller():
    os.system('figlet rm nuclei')
    
    filename = input("📂 Filename List of Nuclei: ")

    print("1 - URL TARGET only (domain-level)")
    print("2 - FULL URL with path")
    option = input("⚡ Choose 1 or 2: ")

    if option not in ["1", "2"]:
        print("❌ Invalid option, please pick 1 or 2.")
        return

    roast_the_targets(filename, option)

if __name__ == "__main__":
    roast_controller()
