
### THIS CODE WAS GENERATED WITH CHATGPT ###

import pyotp
import qrcode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Generate a new secret key
secret_key = pyotp.random_base32()

# Generate the OTP URI
otp_uri = pyotp.totp.TOTP(secret_key).provisioning_uri('bryanfred03@gmail.com', issuer_name='CySER')

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(otp_uri)
qr.make(fit=True)

# Create an image from the QR Code instance
qr_img = qr.make_image(fill='black', back_color='white')

# Save the image
qr_img.save('2fa_qr_code.png')

# Send email with the QR code as attachment
from_email = 'bryanfred03@gmail.com'
to_email = 'bryanfred03@gmail.com'
password = 'ocam aecg lmoy dfli'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = '2FA QR Code'

# Attach the QR code image
with open('2fa_qr_code.png', 'rb') as f:
    img = MIMEImage(f.read())
    img.add_header('Content-Disposition', 'attachment', filename='2fa_qr_code.png')
    msg.attach(img)

# Send the email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)

# Verify the TOTP code
def verify_totp_code(secret_key, user_code):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(user_code)

# Example usage:
user_entered_code = input("Enter the TOTP code generated by Google Authenticator: ")
if verify_totp_code(secret_key, user_entered_code):
    print("Code is valid.")
else:
    print("Code is not valid.")


### THIS CODE WAS GENERATED WITH CHATGPT ###



