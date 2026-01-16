from playwright.sync_api import Page, expect
import re

def test_images(page: Page):
    #Images of home page are visible
    print("Given the user is on the Home page")
    page.goto("https://es.nttdata.com/")
    print("When the user visit the page")
    print("Then the image should be visible")
    expect(page.get_by_role("img", name="NTT-DATA-servizi-e-consulenza-imprese")).to_be_visible()
    