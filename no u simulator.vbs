Dim message, sapi
set sapi=CreateObject("sapi.spvoice")

do
msgbox("say no, u?")
sapi.Speak "no u"
loop