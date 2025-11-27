import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

import os
import datetime

# Crear carpeta si no existe
os.makedirs("reports/screenshots", exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura automática de pantalla cuando un test falla."""
    outcome = yield
    report = outcome.get_result()

    # Solo actuar cuando el test falla en la fase principal
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = os.path.join("reports", "screenshots", filename)

            driver.save_screenshot(filepath)

            # Adjuntar al HTML
            if hasattr(report, "extra"):
                pytest_html = item.config.pluginmanager.getplugin("html")
                report.extra.append(pytest_html.extras.png(filepath))
