from playwright.sync_api import Page, expect
import re
import utils

def test_languages(page: Page):
    #Scenario: Change website language to English
    print("Given the user is on the NTT DATA Spain page")
    page.goto("https://es.nttdata.com/")
   
    #Accept cookies if the button is visible
    utils.accept_cookies(page)

    print("When the user changes the website language to English")
     #If mobile, open the menu first
    if (utils.is_mobile(page)):
        page.get_by_role("button", name="Toggle navigation").click()
    
    page.get_by_role("button", name="Español").click()
    page.get_by_role("link", name="EnglishUnited KingdomEnglish").click()
    #Assertion by url
    print("Then the website should be displayed in English")
    expect(page).to_have_url(re.compile("https://uk.nttdata.com/"))
    #Assertion by an English heading
    expect(page.get_by_role("heading", name="Cyber Frontiers 2026")).to_be_visible()

    