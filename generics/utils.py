from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.utils.html import strip_tags


def send_message(email, user_id):
    subject = "Активация аккаунта"

    activation_link = f"{settings.SITE_URL}/users/activate/{user_id}/"
    print("DEBUG activation_link:", activation_link)

    html_content = f"""
        <html>
          <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
              <h2 style="color: #333;">Добро пожаловать!</h2>
              <p style="font-size: 16px; color: #555;">
                Спасибо, что присоединились к нам. Нажмите на кнопку ниже, чтобы активировать аккаунт:
              </p>
              <a href="{activation_link}" target="_blank" 
                 style="display: inline-block; padding: 15px 25px; font-size: 16px; color: white; background-color: #007BFF; text-decoration: none; border-radius: 5px;">
                Активировать
              </a>
              <p style="font-size: 14px; color: #999; margin-top: 20px;">
                Если кнопка не работает, скопируйте и вставьте ссылку в браузер: <br>
                <a href="{activation_link}" target="_blank" style="color: #007BFF;">{activation_link}</a>
              </p>
            </div>
          </body>
        </html>
    """

    plain_message = strip_tags(html_content)

    try:
        send_mail(
            subject=subject,
            message=plain_message,
            html_message=html_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
    except BadHeaderError:
        print("Invalid header found.")
