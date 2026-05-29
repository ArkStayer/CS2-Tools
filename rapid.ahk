*~$LButton::
Sleep 5
Loop
{
GetKeyState, LButtonState, LButton, P
If LButtonState = U
break
Sleep 1
Send, {Blind}{LButton}
}
Return