from behave.model_core import Status
from utils.driver_manager import DriverManager
from utils.screenshot_utils import ScreenshotUtils
from utils.logger_utils import LoggerUtils
import allure
from utils.allure_utils import AllureUtils


logger = LoggerUtils.get_logger("Behave")

def before_all(context):
    AllureUtils.create_environment_file()
    logger.info("Allure environment file created")

def before_scenario(context,scenario):

    logger.info(f"START Scenario: {scenario.name}")
    context.driver_manager = DriverManager()
    context.driver = context.driver_manager.start_driver()

def after_scenario(context, scenario):

    if scenario.status != Status.passed:

        logger.error(
            f"Scenario {scenario.status.name.upper()}: {scenario.name}"
        )

        screenshot_path = ScreenshotUtils.take_screenshot(
            context.driver,
            scenario.name
        )

        logger.info(
            f"Screenshot saved: {screenshot_path}"
        )
        allure.attach.file(
            str(screenshot_path),
            name=f"Failure - {scenario.name}",
            attachment_type=allure.attachment_type.PNG
        )

    else:
        logger.info(
            f"Scenario PASSED: {scenario.name}"
        )

    context.driver_manager.quit_driver()
    


