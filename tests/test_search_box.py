from playwright.sync_api import Page, expect
import re

def test_searchbox(page: Page):
    #Scenario:Happy path searching for 'cloud' on NTT DATA Spain page
    print("Given the user is on the NTT DATA Spain page")
    page.goto("https://es.nttdata.com/")
    
    #Accept cookies if the button is visible
    btn_cookies = page.get_by_role("button", name=re.compile(r"Aceptar", re.I))
    if btn_cookies.is_visible():
        btn_cookies.click()
    
    print("When the user searches for 'cloud' in the search box")
    page.get_by_role("button", name="Search").click()
    page.get_by_role("searchbox", name="aria-label").clear()
    page.get_by_role("searchbox", name="aria-label").click()
    page.get_by_role("searchbox", name="aria-label").fill("cloud")
    page.locator("#collapseSearch").get_by_role("button", name="Search").click()

    #Assertion
    print("Then the search results should be displayed for 'cloud'")
    expect(page).to_have_url("https://es.nttdata.com/search?keyword=cloud")

