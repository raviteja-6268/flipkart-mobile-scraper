from appium.options.android import UiAutomator2Options


def get_capabilities():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "53121FDCQ0001M"
    options.automation_name = "UiAutomator2"

    options.app_package = "com.flipkart.android"
    options.app_activity = "com.flipkart.android.activity.HomeFragmentHolderActivity"

    options.no_reset = True

    return options