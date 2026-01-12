from playwright.sync_api import Page, expect
import re

def test_contact_form(page: Page):
    #Scenario: Fill the contact form with an empty mandatory field
    print("Given the user is on the Contact page")
    page.goto("https://es.nttdata.com/contact-us")
    print("When the user leaves the 'Name' field empty")
    #Clear the placeholder text
    page.get_by_role("textbox", name="Nombre*").clear()
    #Leave the field empty
    page.get_by_role("textbox", name="Nombre*").fill("")
    print("Then error message should appear")
    expect(page.get_by_text("Campo requerido")).to_be_visible()

    #Scenario: Fill the Telephone field with invalid data
    print("Given the user is on the Contact page")
    page.goto("https://es.nttdata.com/contact-us")
    #Clear the placeholder text
    page.get_by_role("textbox", name="Teléfono*").clear()
    print("When te user fills the 'Telephone' field with invalid data")
    page.get_by_role("textbox", name="Teléfono*").fill("invalid_phone")
    print("Then eror message should appear indicating invalid phone number")
    expect(page.get_by_text("Formato de número de teléfono incorrecto. Por favor, sigue el formato de ejemplo: +34 12 345 6789")).to_be_visible()



    
