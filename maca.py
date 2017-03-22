from Quartz.CoreGraphics import CGEventCreateMouseEvent, CGEventPost, \
    kCGHIDEventTap, kCGMouseButtonLeft, CGEventGetLocation, CGEventCreate, \
    kCGEventLeftMouseDown, kCGEventLeftMouseUp


def _mouse_event(type, x, y):
    event = CGEventCreateMouseEvent(None,
                                    type,
                                    (x, y),
                                    kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, event)


def cur_pos():
    return CGEventGetLocation(CGEventCreate(None))


def click():
    x = cur_pos().x
    y = cur_pos().y

    # simulate left mouse button down & up, making a full click
    _mouse_event(kCGEventLeftMouseDown, x, y)  # down
    _mouse_event(kCGEventLeftMouseUp, x, y)  # up

    print('Clicked x={0} y={1}'.format(x, y))
