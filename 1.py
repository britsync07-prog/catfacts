import os
import sys

def find_files(root_dir, keyword):
    found_files = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            filepath = os.path.join(root, file)

            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                    if keyword in content:
                        print(filepath)
                        found_files.append(filepath)

            except:
                pass

    return found_files


def replace_in_files(files, keyword, replacement):
    for filepath in files:
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            new_content = content.replace(keyword, replacement)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"Replaced in: {filepath}")

        except:
            print(f"Skipped: {filepath}")


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python3 search_replace.py <folder> <keyword>")
        sys.exit(1)

    folder = sys.argv[1]
    keyword = sys.argv[2]

    print("\nFiles containing the keyword:\n")

    files = find_files(folder, keyword)

    if not files:
        print("\nNo files found.")
        sys.exit()

    choice = input("\nDo you want to replace the keyword in these files? (y/n): ").lower()

    if choice == "y":
        replacement = input("Enter the replacement text: ")
        replace_in_files(files, keyword, replacement)
        print("\nReplacement completed.")
    else:
        print("\nNo changes made.")
