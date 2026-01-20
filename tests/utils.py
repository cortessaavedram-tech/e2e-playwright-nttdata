from playwright.sync_api import Page, expect
import re

def is_mobile(page: Page):
    escritorio = 1024
    is_mobile = False

    if(page.viewport_size["width"] < escritorio):
        is_mobile = True

    return is_mobile

def accept_cookies(page):
    if is_mobile(page):
        btn_cookies = page.get_by_role("button", name=re.compile(r"Okay", re.I))
        if btn_cookies.is_visible():
            btn_cookies.click()
    else:
        btn_cookies = page.get_by_role("button", name=re.compile(r"Aceptar", re.I))
        if btn_cookies.is_visible():
            btn_cookies.click()