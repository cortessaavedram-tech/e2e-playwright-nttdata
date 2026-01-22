from tabnanny import check
from playwright.sync_api import Page, expect
import re
import utils

def test_form_empty_field(page: Page):
    #Scenario: Send the contact form with an empty mandatory field
    print("Given the user is on the Contact page")
    page.goto("https://es.nttdata.com/")
    utils.accept_cookies(page)

    if (utils.is_mobile(page)):
        page.get_by_role("link", name="envelope Contact").click()

    if not utils.is_mobile(page):
        page.goto("https://es.nttdata.com/contact-us")
    
    print("When the user leaves the 'Name' field empty")
    #Clear the placeholder text
    page.get_by_label("Nombre*").clear()
    #Leave the field empty
    page.get_by_label("Nombre*").fill("")
    ("And clicks on 'Enviar' button")
    page.get_by_role("button", name="Enviar").click()
    
    print("Then error message should appear")
    utils.accept_cookies(page)
    expect(page.get_by_text("Campo requerido").nth(3)).to_be_visible()


def test_form_invalid_data(page: Page):
    #Scenario: Fill the Telephone field with invalid data
    print("Given the user is on the Contact page")
    page.goto("https://es.nttdata.com/")
    utils.accept_cookies(page)

    if (utils.is_mobile(page)):
        page.get_by_role("link", name="envelope Contact").click()

    if not utils.is_mobile(page):
        page.goto("https://es.nttdata.com/contact-us")
    #Clear the placeholder text
    page.get_by_label("Teléfono*").clear()
    print("When te user fills the 'Telephone' field with invalid data")
    page.get_by_label("Teléfono*").fill("invalid_phone")
    print("And clicks on 'Enviar' button")
    page.get_by_role("button", name="Enviar").click()
    print("Then error message should appear indicating invalid phone number")
    utils.accept_cookies(page)
    expect(page.get_by_text(re.compile(r"Formato de número de teléfono", re.I))).to_be_visible()


def test_form_privacy_policy(page: Page):
    #Scenario: Not accept the privacy policy
    print("Given the user is on the Contact page")
    page.goto("https://es.nttdata.com/")
    utils.accept_cookies(page)
    
        
    print("When the user does not accept the Conditions checkbox")
    utils.accept_cookies(page)
    print("And clicks on 'Enviar' button")
    page.get_by_role("button", name="Enviar").click()
    expect(page.get_by_text(re.compile(r"Por favor, lee y acepta la", re.I))).to_be_visible()


def test_form_invalid_email(page: Page):
    #Scenario: Fill the email field with invalid data
    print("Given the user is on the Contact page")
    page.goto("https://es.nttdata.com/")
    utils.accept_cookies(page)
    if (utils.is_mobile(page)):
        page.get_by_role("link", name="envelope Contact").click()

    if not utils.is_mobile(page):
        page.goto("https://es.nttdata.com/contact-us")

    print("When the user fills the email field with invalid format")
    page.get_by_label("Correo electrónico*").clear()
    page.get_by_label("Correo electrónico*").fill("invalid_email")
    print("And clicks on 'Enviar'button")
    page.get_by_role("button", name="Enviar").click()
    print("Then 'El formato no coincide' message should appear.")
    expect(page.get_by_text("El formato no coincide")).to_be_visible()

    
