def open_schema(device, schema):
    s = device.session('com.ky.template.test')
    device(className='XCUIElementTypeTextView').click()
    s.send_keys(schema)
    device(name="scheme跳转").click()
    device(name='打开').click_exists()