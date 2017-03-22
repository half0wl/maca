# Maca

Autoclicker for macOS, written in Python.

(Work in progress)

Retrieving current cursor position and simulating a left click is working.

```python
>>> from maca import cur_pos, click
>>> cur_pos()
<NSPoint x=1140.57421875 y=401.890625>
>>> click()
Clicked x=1140.57421875 y=401.890625
```

## Todo

* Auto-clicking upon trigger (with `NSTimer` maybe?)
* Hotkey trigger (with `NSEvent` & `NSKeyDownMask`)
* GUI? With either PyQt or Tkinter. Or CLI? Or menubar app (similar to [simon](https://github.com/hcyrnd/simon/))?