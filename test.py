from core.ios_server import IosServer
from core.driver import IosDriver

schema = 'kwaiying://main'
server = IosServer()
driver = IosDriver.get_driver()
s = driver.session('com.ky.template.test')
driver(className='XCUIElementTypeTextView').click()
s.send_keys(schema)
driver(name="scheme跳转").click()
driver(name='打开').click_exists()
server.stop()

