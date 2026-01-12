from playwright.sync_api import Page, expect
import re

def test_contact_form(page: Page):
    print("Given the user is on the Contact page")
    page.goto("https://es.nttdata.com/contact-us")
    print("When the user leaves the 'Name' field empty")
    #Clear the placeholder text
    page.get_by_role("textbox", name="Nombre*").clear()
    #Leave the field empty
    page.get_by_role("textbox", name="Nombre*").fill("")
    #print("Then Campo requerido message should appear")
    expect(page.get_by_text("Campo requerido")).to_be_visible()

    
