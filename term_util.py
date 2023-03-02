"""
term_util.py is a utility for auto generating definition links to specific terms in the documentation.

To utilize, words like "Admin" and such will be converted to links with tooltips.

Ways to achieve this in Github's Markdown:
<abbr title="Tooltip">Text</abbr>
[Text](https://stackoverflow.com/a/71729464/11465149 "Tooltip here!")
"""

import sys
import time
import os
import re

FAILURE = 1
SUCCESS = 0

terms = {
    "CTX ": "CTX ",
    "Trainer ": "[Trainer](terms.md 'A cadet who instructs, trains, and leads the Participant(s).') ",
    "Admin ": "[Admin](terms.md 'The primary trainer and onsite mastermind.') ",
    "Participant ": "[Participant](terms.md 'A cadet who is participating as an end user in the CTX.') ",
    "Leader ": "[Leader](terms.md 'A Participant who is selected as the team leader for all the Participant(s).') ",
    "Designer ": "[Designer](terms.md 'The creator and 'owner'' of a specific CTX. They are responsible for all code and documentation for their specific CTX.') ",
    "Developer ": "[Developer](terms.md \"Someone who contributes to the CTX Project's code or documentation.\") "
    #"TODO ": "[TODO](terms.md 'TODO') ",
}

def update_terms(filename: str) -> int:
    """
    Updates a file to include links and tooltips on all terms
    Returns the number of line changes
    """
    temp_ending = ".temp.md"
    file = open(filename, "r")
    file_w = open(filename + temp_ending, "w")
    changes_count = 0
    for line in file:
        for term in terms.keys():
            if term in line:
                # add term
                line = line.replace(term, terms[term])
                changes_count += 1
                print(term, "-", line)
            #if re.findall(r".*\[" + term + "\]\(terms.md '" + terms[term] + "'\)")
        file_w.write(line)
    file.close()
    file_w.close()
    os.rename(filename + temp_ending, filename)
    return changes_count

def print_usage():
    print("USAGE: python3 term_util.py file_to_update [file_to_update_2]...[file_to_update_n]")
    return FAILURE

def check_file_exists(filename: str):
    """
    Return FAILURE if file does not exist
    Return SUCCESS if file does exist
    """
    if not os.path.isfile(filename):
        print("ERROR: filename '", filename, "' does not exist!")
        return print_usage()
    return SUCCESS

def main():
    if len(sys.argv) < 2:
        return print_usage()
    update_line_count = 0
    start_seconds = time.time()
    for filename in sys.argv[1:]:
        if check_file_exists(filename) == 1:
            return print_usage()
        update_line_count += update_terms(filename)
    total_seconds = str(round(time.time() - start_seconds, 2))
    print("Updated", update_line_count, "lines in", total_seconds, "seconds")

if __name__ == "__main__":
    main()