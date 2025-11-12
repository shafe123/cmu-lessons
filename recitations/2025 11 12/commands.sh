# Work only inside the reviews folder (keeps output clean; avoids venv and other parent dirs)
cd reviews

# Hint: Use . to represent the current directory in your commands
############################################################
# TODO 1 — List the names of all .txt files that contain the word "great" (case-insensitive)
# Hint: Use grep with appropriate flags
############################################################
grep -l -I -r great .

############################################################
# TODO 2 — Count how many .txt files mention the word "programming" (case-insensitive)
# Hint-1: You can use pipes to combine commands
# Hint-2: We are counting files, not occurrences
############################################################
grep -l -I -r programming . | wc -l

############################################################
# TODO 3 — Replace all email addresses in .txt files with <EMAIL_REMOVED> in place and create a backup with .bak extension
# Hint: Use sed with regex for a single file first
############################################################
# sed -s -E -i.bak 's/[[:alnum:].]+@[[:alnum:]]+\.com/<EMAIL_REMOVED>/gI' reviews1.txt
find *.txt | xargs sed -s -E -i.bak 's/[[:alnum:].]+@[[:alnum:]]+\.com/<EMAIL_REMOVED>/gI'

############################################################
# TODO 4 — From books_metadata.csv, print only the Title and Price columns (space-separated)
# Hint: Use awk to select specific columns (skip header row)
# Challenge: Do it by dynamically finding the column numbers based on the header row
############################################################


############################################################
# TODO 5 — Count how many books are free (is_free == True)
# Hint: Use awk to filter and count
# Challenge: Do it by dynamically finding the column number based on the header row
############################################################

cd ..