import pytest

from selenium.webdriver.common.by import By
from Utilties.utils import AutomationLogger
from pages.Xpertbotlogin import Xpert6






@pytest.mark.usefixtures("LaunchDriver")
class TestXpertbotLogin:
    log=AutomationLogger.automation()
    test_data= AutomationLogger.get_newest_excel_file("C:\\Users\\KarimBouGhannam\\Documents\\Xpert6\\testdata","Sheet1")
    @pytest.mark.parametrize("test_data", test_data)
    # This test will run for each row in the test data
    def test_login(self,test_data):

        try:
            self.log.info("Test started: test_login")
            Xpert=Xpert6(self.driver)
            Xpert.XpertbotLogin(**test_data)
            self.log.info("Login successful")
        except Exception as e:
            self.log.error(f"An error occurred during login: {e}")
            pytest.fail(f"Test failed due to an exception: {e}")


