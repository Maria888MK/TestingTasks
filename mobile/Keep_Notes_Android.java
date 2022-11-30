package mobile;

import io.appium.java_client.android.AndroidDriver;
import java.net.URL;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.remote.DesiredCapabilities;


public class Keep_Notes_Android {

    private static final String APPIUM = "http://localhost:4723/wd/hub";
    private AndroidDriver driver;


    @Before
    public void setUp() throws Exception {
        DesiredCapabilities caps = new DesiredCapabilities();
        caps.setCapability("platformName", "Android");
        caps.setCapability("platformVersion", "13");
        caps.setCapability("deviceName", "Android Emulator");
        caps.setCapability("automationName", "UiAutomator2");
        this.driver = new AndroidDriver(new URL("http://localhost:4723/wd/hub"), caps);
    }

    @After
    public void tearDown() {
        if (this.driver != null) {
            this.driver.quit();
        }

    }

    @Test
    public void test() {
        System.out.println("test!");
    }
}
