from playwright.sync_api import Page, expect
import re

def test_languages(page: Page):
    #Scenario: Change website language to English
    print("Given the user is on the NTT DATA Spain page")
    page.goto("https://es.nttdata.com/")
    #Accept cookies if the button is visible
    btn_cookies = page.get_by_role("button", name=re.compile(r"Aceptar", re.I))
    if btn_cookies.is_visible():
        btn_cookies.click()
    print("When the user changes the website language to English")
    page.get_by_role("button", name="Español").click()
    page.get_by_role("link", name="EnglishUnited KingdomEnglish").click()
    #Assertion by url
    print("Then the website should be displayed in English")
    expect(page).to_have_url(re.compile("https://uk.nttdata.com/"))
    #Assertion by an English heading
    expect(page.get_by_role("heading", name="Cyber Frontiers 2026")).to_be_visible()