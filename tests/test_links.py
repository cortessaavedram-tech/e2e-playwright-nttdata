from playwright.sync_api import Page, expect
import re

def test_links_linkedin(page: Page):
    #Scenario: Verify LinkedIn link
    print("Given the user is on the NTT DATA Spain page")
    page.goto("https://es.nttdata.com/")
    #Accept cookies if the button is visible
    btn_cookies = page.get_by_role("button", name=re.compile(r"Aceptar", re.I))
    if btn_cookies.is_visible():
        btn_cookies.click()

    print("When the user clicks on the LinkedIn link in the footer")
    with page.context.expect_page() as new_page_info:
        page.get_by_role("link", name="LinkedIn").click()

    linkedin_page = new_page_info.value
    linkedin_page.wait_for_load_state()

    print("Then the LinkedIn page should open in a new tab")
    expect(linkedin_page).to_have_url(re.compile(r"linkedin\.com/company/ntt-data", re.I))


def test_links_x(page: Page):
    #Scenario: Verify X link
    print("Given the user is on the NTT DATA Spain page")
    page.goto("https://es.nttdata.com/")
    #Accept cookies if the button is visible
    btn_cookies = page.get_by_role("button", name=re.compile(r"Aceptar", re.I))
    if btn_cookies.is_visible():
        btn_cookies.click()

    print("When the user clicks on the X link in the footer")
    with page.context.expect_page() as new_page_info:
        page.get_by_role("link", name="twitter").click()

    x_page = new_page_info.value
    x_page.wait_for_load_state()

    #Accept cookies if the button is visible
    btn_cookies = page.get_by_role("button", name=re.compile(r"Aceptar", re.I))
    if btn_cookies.is_visible():
        btn_cookies.click()

    print("Then the X page should open in a new tab")
    expect(x_page).to_have_url(re.compile(r"x\.com/nttdata", re.I))