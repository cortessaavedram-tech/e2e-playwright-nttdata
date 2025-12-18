from playwright.sync_api import Page, expect

def test_visit_menu_links(page: Page):
    print("Given the user is on the homepage")
    page.goto("https://es.nttdata.com/")

    print("And the user accepts the cookies")
    page.locator("iframe[title=\"Banner de cookies\"]").content_frame.get_by_role("button", name="Aceptar").click()
