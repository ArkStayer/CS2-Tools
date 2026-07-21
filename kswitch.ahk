toggle := false
z::
    toggle := !toggle
return
~$LButton::
    if (toggle) {
        ; Try -1000, -2000, or even -5000
	Sleep, 100
        DllCall("mouse_event", "UInt", 0x01, "UInt", 4000, "UInt", 5000, "UInt", 0, "UInt", 0)
	Sleep, 100
	DllCall("mouse_event", "UInt", 0x01, "UInt", -4000, "UInt", 2000, "UInt", 4000, "UInt", 5000)
    }
return