import os

from playwright.sync_api import Page, expect


def test_home_page_loads(page: Page, live_server):
    page.goto(live_server.url)

    expect(page).to_have_title("Todo")
    expect(page.get_by_role("heading", name="Get this done")).to_be_visible()
