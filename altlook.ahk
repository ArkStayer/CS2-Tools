altPressed := false

$Alt::
    if !altPressed {
        altPressed := true
        DllCall("mouse_event", "UInt", 0x01, "UInt", 4000, "UInt", 0, "UInt", 0, "UInt", 0)
    }
return

$Alt up::
    altPressed := false
    DllCall("mouse_event", "UInt", 0x01, "UInt", 4000, "UInt", 0, "UInt", 0, "UInt", 0)
return