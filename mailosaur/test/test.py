from email.mime.text import MIMEText
import smtplib
import time
from unittest import TestCase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from mailosaur.mailosaur import Mailosaur


class MailosaurTest(TestCase):
    def setUp(self):
        with open('mailbox.settings') as f:
            config = f.readlines()

        mailbox_id = config[0].strip()
        api_key = config[1].strip()
        self.mailbox = Mailosaur(mailbox_id, api_key)

    def test_get_emails(self):
        # ensure mailbox is empty to prevent picking up previous test emails:
        self.mailbox.delete_all_email()

        # send three emails with different subjects:
        self.send_test_email('one')
        recipient = self.send_test_email('two')
        self.send_test_email('three')

        # wait for emails to be received fully:
        time.sleep(2)
        emails = self.mailbox.get_emails()
        self.assertEqual(3, len(emails))

        email = next(x for x in emails if x.to_address[0].address == recipient)
        self.assert_email(email, recipient, 'two')

    def test_get_emails_search(self):
        # ensure mailbox is empty to prevent picking up previous test emails:
        self.mailbox.delete_all_email()

        # send three emails with different subjects:
        self.send_test_email('one')
        recipient = self.send_test_email('two')
        self.send_test_email('three')

        # find the second one based on the subject:
        emails = self.mailbox.get_emails('two')

        # assert we have only one email with the right subject sent to the right recipient:
        self.assertTrue(1, len(emails))
        self.assert_email(emails[0], recipient, 'two')

    def test_get_emails_by_recipient(self):
        # send three emails to different recipients:
        self.send_test_email('one')
        recipient = self.send_test_email('two')
        self.send_test_email('three')

        # find the second one:
        emails = self.mailbox.get_emails_by_recipient(recipient)

        # assert recipient, subject and other email properties
        self.assert_email(emails[0], recipient, 'two')

    def test_empty_mailbox(self):
        self.send_test_email('one')
        self.send_test_email('two')

        # wait to ensure emails have been processed
        time.sleep(4)

        self.mailbox.delete_all_email()
        emails = self.mailbox.get_emails(None, 1)
        self.assertEqual(0, len(emails))

    def assert_email(self, email, to_address, subject='test subject'):
        # html links:
        self.assertEqual(3, len(email.html.links))
        self.assertEqual('https://mailosaur.com/', email.html.links[0].href)
        self.assertEqual('mailosaur', email.html.links[0].text)
        self.assertEqual('https://mailosaur.com/', email.html.links[1].href)
        self.assertEqual(None, email.html.links[1].text)
        self.assertEqual('http://invalid/', email.html.links[2].href)
        self.assertEqual('invalid', email.html.links[2].text)

        # html images:
        self.assertTrue(email.html.images[1].src.endswith('.png'))
        self.assertEqual('Inline image 1', email.html.images[1].alt)

        # html body:
        body = "<div dir=\"ltr\"><img src=\"https://mailosaur.com/favicon.ico\" /><div style=\"font-family:arial,sans-serif;font-size:13px;color:rgb(80,0,80)\">this is a test.</div><div style=\"font-family:arial,sans-serif;font-size:13px;color:rgb(80,0,80)\"><br>this is a link: <a href=\"https://mailosaur.com/\" target=\"_blank\">mailosaur</a><br>\n</div><div class=\"gmail_quote\" style=\"font-family:arial,sans-serif;font-size:13px;color:rgb(80,0,80)\"><div dir=\"ltr\"><div><br></div><div>this is an image:<a href=\"https://mailosaur.com/\" target=\"_blank\"><img src=\"cid:inline_cid\" alt=\"Inline image 1\"></a></div>\n<div><br></div><div>this is an invalid link: <a href=\"http://invalid/\" target=\"_blank\">invalid</a></div></div></div>\n</div>"
        self.assertEqual(body, email.html.body)

        # text links:
        self.assertEqual(2, len(email.text.links))
        self.assertTrue(email.text.links[0].href.startswith('https://mailosaur.com/'))
        self.assertTrue(email.text.links[0].text.startswith('https://mailosaur.com/'))
        self.assertTrue(email.text.links[1].href.startswith('https://mailosaur.com/'))
        self.assertTrue(email.text.links[1].text.startswith('https://mailosaur.com/'))

        # text body:
        text = "this is a test.\n\nthis is a link: mailosaur <https://mailosaur.com/>\n\nthis is an image:[image: Inline image 1] <https://mailosaur.com/>\n\nthis is an invalid link: invalid"
        self.assertEqual(text, email.text.body)

        # headers:
        self.assertTrue(email.headers['received'].startswith('from'))
        self.assertEqual('anyone<anyone@example.com>', email.headers['from'])
        self.assertEqual('python<' + to_address + '>', email.headers['to'])
        self.assertEqual(subject, email.headers['subject'])

        # properties:
        self.assertEqual(subject, email.subject)
        self.assertEqual('normal', email.priority)

        self.assertTrue(email.creation_date.year > 2013)
        self.assertIsNotNone(email.sender_host)
        self.assertIsNotNone(email.mailbox)

        # raw eml:
        self.assertIsNotNone(email.raw_id)
        eml = self.mailbox.get_raw_email(email.raw_id)
        self.assertIsNotNone(eml)
        self.assertTrue(len(eml) > 1)
        assert (eml.startswith('Received') or eml.startswith('Authentication'))

        #from:
        self.assertEqual('anyone@example.com', email.from_address[0].address)
        self.assertEqual('anyone', email.from_address[0].name)

        # to:
        self.assertEqual(to_address, email.to_address[0].address)
        self.assertEqual('python', email.to_address[0].name)

        # attachments:
        self.assertEqual(2, len(email.attachments), 'there should be 2 attachments')

        # attachment 1:
        attachment1 = email.attachments[0]
        self.assertIsNotNone(attachment1.id)
        self.assertTrue(attachment1.id.endswith('.png'))
        self.assertEqual(4819, attachment1.length)
        self.assertEqual('logo-m.png', attachment1.file_name)

        self.assertEqual("image/png", attachment1.content_type)

        data1 = self.mailbox.get_attachment(attachment1.id)
        self.assertIsNotNone(data1)

        # attachment 2:
        attachment2 = email.attachments[1]
        self.assertTrue(attachment2.id.endswith('logo-m-circle-sm.png'))
        self.assertEqual(5260, attachment2.length)
        self.assertEqual('logo-m-circle-sm.png', attachment2.file_name)
        self.assertEqual('image/png', attachment2.content_type)

        data2 = self.mailbox.get_attachment(attachment2.id)
        self.assertIsNotNone(data2)
        self.assertEqual(attachment2.length, len(data2))

    def send_test_email(self, subject='test subject'):
        msg = MIMEMultipart('related')
        msg['Subject'] = subject

        from_address = 'anyone<anyone@example.com>'
        to_address = self.mailbox.generate_email_address()
        to_address_long = 'python<' + to_address + '>'

        msg['From'] = from_address
        msg['To'] = to_address_long

        alt = MIMEMultipart('alternative')
        msg.attach(alt)

        text = "this is a test.\n\nthis is a link: mailosaur <https://mailosaur.com/>\n\nthis is an image:[image: Inline image 1] <https://mailosaur.com/>\r\n\nthis is an invalid link: invalid"
        html = "<div dir=\"ltr\"><img src=\"https://mailosaur.com/favicon.ico\" /><div style=\"font-family:arial,sans-serif;font-size:13px;color:rgb(80,0,80)\">this is a test.</div><div style=\"font-family:arial,sans-serif;font-size:13px;color:rgb(80,0,80)\"><br>this is a link: <a href=\"https://mailosaur.com/\" target=\"_blank\">mailosaur</a><br>\n</div><div class=\"gmail_quote\" style=\"font-family:arial,sans-serif;font-size:13px;color:rgb(80,0,80)\"><div dir=\"ltr\"><div><br></div><div>this is an image:<a href=\"https://mailosaur.com/\" target=\"_blank\"><img src=\"cid:inline_cid\" alt=\"Inline image 1\"></a></div>\n<div><br></div><div>this is an invalid link: <a href=\"http://invalid/\" target=\"_blank\">invalid</a></div></div></div>\n</div>"

        alt.attach(MIMEText(text))
        alt.attach(MIMEText(html, 'html'))

        fp = open('logo-m.png', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        img.add_header('Content-ID', 'inline_cid')
        img.add_header('Content-Disposition', 'inline', filename='logo-m.png')
        msg.attach(img)

        fp = open('logo-m-circle-sm.png', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        img.add_header('Content-Disposition', 'attachment', filename='logo-m-circle-sm.png')
        msg.attach(img)

        smtp = smtplib.SMTP()
        smtp.connect('mailosaur.com')
        smtp.sendmail(from_address, to_address, msg.as_string())
        smtp.quit()

        return to_address
