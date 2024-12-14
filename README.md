## Pioreactor Vernier FPH-BTA Plugin

The plugin allows you to read temperature into the pioreactor app using the Vernier TMP-BTA sensor.

This plugin assumes that a JSON is being received by the RPI via serial, and that the JSON has keys A0-A5 representing voltages read by Arduino pins. Alternatively one might use some kind of ADC that can use 5V power to supply the sensor but still transmit over I2C at 3.3V etc., but in my case the arduino was the simplest option.

For wiring the sensor you can either use something like the vernier arduino shield or BTA breakout (which have been discontinued as of writing) or in my case I bought some BTA extenders [from amazon](https://www.amazon.co.uk/dp/B08CTWK13F?ref=ppx_yo2ov_dt_b_fed_asin_title), cut the BTA end off and soldered to header pins for breadboarding.
The pinouts for the BTA are [here](https://learn.sparkfun.com/tutorials/vernier-shield-hookup-guide/vernier-shield-pin-out-and-configuration).
I only bother to use vin, gnd, and the signal from the sensor, as I'm not using sensors that need the other pins and haven't figured out how to get the identification working properly.

Then you need arduino code to write the json to serial etc.

## Installation

Install from the Pioreactor plugins web interface or the command line:

```
pio install-plugin vernier-TMP-BTA # to install directly on the Pioreactor

# OR, on the leader's command line:

pios install-plugin vernier-TMP-BTA # to install on all Pioreactors in a cluster
```

Or install through the web interface (_Plugins_ tab). This will install the plugin on all Pioreactors within the cluster.

## Usage

#### Through the command line:
```
pio run vernier_tmp_bta
```

#### Through the UI:

Under _Manage_, there will be a new _Activities_ option called _vernier_tmp_bta_. Editable settings include the pin that's being read and the slope and intercept for calibration. 

## Plugin documentation

Documentation for plugins can be found on the [Pioreactor docs](https://docs.pioreactor.com/developer-guide/intro-plugins).
