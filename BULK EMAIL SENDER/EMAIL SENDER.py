import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"  # Gmail SMTP Server
SMTP_PORT = 587  # TLS Port
SENDER_EMAIL = "YOUR EMAIL HERE"  # Your Email
SENDER_PASSWORD = "APP PASSWORD HERE"  # Use an App Password if using Gmail

# List of recipients
to_emails = [
    "RECIPIENT1@EXAMPLE.COM",
    "RECIPIENT2@EXAMPLE.COM"
]

cc_emails = [
    "CC1@EXAMPLE.COM",
    "CC2@EXAMPLE.COM"
]

bcc_emails = [
    "BCC1@EXAMPLE.COM",
    "BCC2@EXAMPLE.COM"
]

# Email content
subject = "SUBJECT HERE"
body = """\
USE HTML FOR BETTER EMAIL VISIBILITY
"""

# Create Email
msg = MIMEMultipart()
msg["From"] = SENDER_EMAIL
msg["To"] = ", ".join(to_emails)  # Visible To recipients
msg["Cc"] = ", ".join(cc_emails)  # Visible CC recipients
msg["Subject"] = subject
msg.attach(MIMEText(body, "html"))  # Attach body as HTML

# Attachment: Add your file here (e.g., flyer, event details, etc.)
filename = "YOUR_FILENAME.EXT"  # Replace with your actual file name
attachment_path = r"PATH_TO_YOUR_FILE"  # Replace with the actual file path

try:
    attachment = open(attachment_path, "rb")  # Open the file in binary mode

    # Create attachment MIME object
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

    # Encode the payload to base64
    encoders.encode_base64(part)

    # Add header with the filename
    part.add_header("Content-Disposition", f"attachment; filename={filename}")

    # Attach the file to the email
    msg.attach(part)

except FileNotFoundError:
    print("⚠️ Attachment not found. Email will be sent without it.")

# Combine all recipients for sending (To + CC + BCC)
all_recipients = to_emails + cc_emails + bcc_emails

# Send Email
try:
    # Connect to SMTP Server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Secure connection
    server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Login

    # Send Email
    server.sendmail(SENDER_EMAIL, all_recipients, msg.as_string())
    print("✅ Email sent successfully with attachment!")

    # Close connection
    server.quit()
except Exception as e:
    print(f"❌ Error: {e}")
