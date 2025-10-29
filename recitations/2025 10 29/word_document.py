from docx import Document
#Generate an invitation like below and write it to a document
# John Doe,
# You are invited to the Annual Gala.
# Date: December 15, 2024
# Time: 6:00 PM
# Location: 1234 Event Hall, Main City
# Looking forward to seeing you!
# Best Regards,
# Event Organizer
# Read the invitation and print on console

document = Document()
document.add_paragraph("Hello, welcome to the Event!")
document.save("sample_invitation.docx")


def generate_invitation(name, event, date, time, location, output_dir):
    # TODO initialize document and add paragraphs
    file_name = f"{output_dir}/{name.replace(' ', '_')}_invitation.docx"
    # TODO save document to file_name
    print(f"Invitation created for {name}")

generate_invitation("John Doe", "Annual Gala", "December 15, 2024", "6:00 PM", "1234 Event Hall, Main City", "invitations")

def read_invitation(file_path):
    # TODO open document at file_path and print each paragraph
    pass

# File path to the generated invitation
file_path = "invitations/John_Doe_invitation.docx"

# Read and print the invitation content
read_invitation(file_path)
