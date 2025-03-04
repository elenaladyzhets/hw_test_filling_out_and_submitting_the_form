from selene import have, command
from selene.support.shared import browser

from model import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

