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
    expect(page.get_by_text("Formato de número de teléfono incorrecto. Por favor, " \
    "sigue el formato de ejemplo: +34 12 345 6789")).to_be_visible()

    #Scenario: Not accept the privacy policy
    print("Given the user is on the Contact page")
    page.goto("https://es.nttdata.com/contact-us")
    print("When the user does not accept the Conditions checkbox")
    page.get_by_role("checkbox", name="Declaro haber leído y entendido estas condiciones " \
    "y acepto la gestión de mis datos personales bajo nuestra Política de privacidad y cookies para ser contactado " \
    "desde NTT DATA Spain y las compañías del grupo NTT DATA, Inc.*").uncheck()
    print("And clicks on 'Enviar' button")
    page.get_by_role("button", name="Enviar").click()
    print("Then an error message should appear")
    expect(page.get_by_text("Por favor, lee y acepta la política de privacidad.", exact=True)).to_be_visible()
    
    #Scenario: Fill the email field with invalid data
    print("Given the user is on the Contact page")
    page.goto("https://es.nttdata.com/contact-us")
    print("When the user fills the email field with invalid format")
    page.get_by_role("textbox", name="Correo electrónico*").clear()
    page.get_by_role("textbox", name="Correo electrónico*").fill("invalid_email")
    print("Then 'El formato no coincide' message should appear.")
    expect(page.get_by_text("El formato no coincide")).to_be_visible()
    


    
