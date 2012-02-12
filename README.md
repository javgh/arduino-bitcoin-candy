#### Description

This repository hosts the software bits of a candy dispenser build with
Arduino and utilizing Bitcoin as the payment mechanism. It uses code
from the this project: https://github.com/javgh/greenaddress-pos-tools/ .

#### Getting started

- install dependencies: python-qrencode, python-qt4
- add "server=1" (but not daemon=1) to bitcoin.conf and configure rpcuser & rpcpassword
- create the file $HOME/.arduino-bitcoin-candyrc with this contents:

````
{
    "arduino_port": "/dev/ttyUSB0", 
    "candy_currency": "USD", 
    "candy_price": 2.0, 
    "exchange_rate_ticker": {
        "field": "last", 
        "interval": 5, 
        "source": "MtGox.com", 
        "url": "https://mtgox.com/api/0/data/ticker.php"
    }, 
    "green_addresses": {
        "1CDysWzQ5Z4hMLhsj4AKAEFwrgXRC8DqRN": "Verified by Instawallet."
    }, 
    "rpc_url": "http://rpcuser:rpcpassword@127.0.0.1:8332"
}
````

- upload the sketch arduino/trigger_via_serial/trigger_via_serial.ino to your Arduino
- run: python pos-tool.py

You should see two windows popping up: The merchant back end and the
customer display. Clicking on "Init demo" will display a new Bitcoin
address and associated QR code. The tool then listens for transactions
to the Bitcoin address and as soon as it receives something, it changes
the display to read "Payment received" and sends a signal to the
Arduino.

#### Not yet implemented

- looping the demo
- checking for correct amount and dealing with cases where not enough or
  too much was payed
- any kind of double-spend detection/prevention mechanism (besides green
  addresses)
