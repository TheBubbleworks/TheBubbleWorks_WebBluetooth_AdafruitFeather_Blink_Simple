# Pre-requisites

- Adafruit Feather BLE: https://www.adafruit.com/product/2829
- Arduino Setup:        https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le/setup
- Feather BLE Library:  https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le/installing-ble-library
- BlueFruit Firmata:    https://learn.adafruit.com/getting-started-with-the-nrf8001-bluefruit-le-breakout/software-bluefruit-firmata
- Arduino 1.6.x on your computer
- Web Bluetooth enabled browser  (see Running)
 

Once all the above is sorted then in the Arduino IDE open the example :  
`Examples -> Adafruit BLEFirmata -> BluefruitLE_nrf51822`

Modify the sketch:

Change:
`#define WAITFORSERIAL   true`

to: 
`#define WAITFORSERIAL   false`

Once the sketch is uploaded to the Feather open this web page in a browser to connect and start blinking, go crazy! :)

Note: On some browser versions and platform you may get a message "GATT operation failed for unknown reason" this is often a warning that can be ignored, mostly...


# Running

To run this demo you will need to use a compatible browser ona supported OS, please see the browser
compatibility matrix here: https://github.com/WebBluetoothCG/web-bluetooth/blob/gh-pages/implementation-status.md


 The demo can be 'browsed to' in multiple ways;

* A 'Live and editable' version [on Plunker](https://embed.plnkr.co/nd5uBt/):		

* Here, hosted via [GitHub pages](https://www.thebubbleworks.com/TheBubbleWorks_WebBluetooth_AdafruitFeather_Blink_Simple/) (gh-pages branch).

* On your local computer, after checking out this repository and running a simple Python HTTPS Server:
```
git clone https://github.com/TheBubbleWorks/TheBubbleWorks_WebBluetooth_AdafruitFeather_Blink_Simple
```

To run the server:

```
python main.py 
```

Open a browser at [https://localhost:9443/](https://localhost:9443/)

You will need to accept the self-signed certificate.


