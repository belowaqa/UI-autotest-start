from playwright.sync_api import expect, Page
import pytest

@pytest.mark.ui
def test_successful_registration(page: Page, user_data: dict[str, str]):
        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )

        page.locator("[data-testid='registration-form-email-input'] input").fill(user_data['email'])
        page.locator("[data-testid='registration-form-username-input'] input").fill(user_data['username'])
        page.locator("[data-testid='registration-form-password-input'] input").fill(user_data['password'])
        page.locator("[data-testid='registration-page-registration-button']").click()
        expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_title = page.locator("[data-testid='dashboard-toolbar-title-text']")
        expect(dashboard_title).to_be_visible()
        expect(dashboard_title).to_have_text("Dashboard")
        # input("Нажмите Enter для завершения...")
