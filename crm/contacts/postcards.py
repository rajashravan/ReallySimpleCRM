import lob

lob.api_key = "test_333b0d654ea19eaec8ab7074cf3de26b605"  # REMOVE LATER


def send_postcard(contact, postcard_text):
    if contact.address_line_1 is "":
        raise ValueError("Contact is missing the 'Address Line 1' field")

    if contact.city is "":
        raise ValueError("Contact is missing the 'City' field")

    if contact.state is "":
        raise ValueError("Contact is missing the 'State' field")

    to_address = lob.Address.create(
        name=contact.first_name + " " + contact.last_name,
        address_line1=contact.address_line_1,
        address_line2=contact.address_line_2,
        address_city=contact.city,
        address_state=contact.state,
        address_zip="00000",  # ignoring zip verification
        email=contact.email,
    )

    card = lob.Postcard.create(
        to_address=to_address,
        back='<html style="padding: 1in; font-size: 20;">{{postcard_text}}</html>',
        front='https://lob.com/postcardfront.pdf',
        merge_variables={
            'postcard_text': postcard_text
        },
    )
