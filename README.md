zkouska raspberry pi 3 s kamerou v2 nez se tema prace zmenilo

pripojeni pres SSH:
ssh pi@10.10.1.5
att4hack

1. updatovani zastaralych balicku
   sudo apt update
2. stahovani rpicam-apps
3. rpicam-hello --list-cameras
4. ve slozce kde jsou fotky python3 -m http.server 8080
5. fotka pomoci
   rpicam-still -t 2000 -q 100 --width 3280 --height 2464 -o fotka3.jpg (lepsi rozliseni - horsi na focus)
   rpicam-still -t 2000 -q 100  -o fotka3.jpg (lepsi pro focus)

fotka hostovana pres python server, na prohlizeci http://10.10.1.5:8080/fotka3.jpg
pytesseract nebylo moc presne pro mala pismena
