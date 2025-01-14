#
# SPDX-License-Identifier: 0BSD
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
#

# This file is a simple test driver for testing the ws2812_pio module. It is
# meant to be run on the rp2 target board that already has the ws2812_pio
# module installed.
#
# It will instantiate the module and perform a couple of simple operations to
# verify the module works.

import array
import time
import ws2812_pio as wspio

# Verify test by inspection:
# the first 3 LEDs should light in sequence R, G, B with half second between
# each. The cycle should repeat 10 times.

def run():
    print("running ws2812 test")
    print("you should see 3 LEDs blinking in sequence for about 15 seconds")
    ws = wspio.WS2812(smid=0, pin=16)
    pixels = array.array("I", [0 for _ in range(3)])
    colors = [0x003f00, 0x3f0000, 0x00003f]
    for _ in range(10):
        print("*", end="")
        for pix in range(3):
            pixels[pix] = colors[pix]
            pixels[pix-1] = 0
            ws.show(pixels)
            time.sleep_ms(500)
    for pix in range(3):
        pixels[pix] = 0
    ws.show(pixels)
    time.sleep_ms(100)
    ws.shutdown()
    print("\nTest exiting")

run()

