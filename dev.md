
# Collect Sample data

Add debug section under uart to surface the raw data

```yaml
uart:
  - id: remote_bus
    baud_rate: 4800
    rx_pin: GPIO2
    debug:
      direction: RX
      dummy_receiver: true
      after:
        delimiter: "\n"
      sequence:
        - lambda: UARTDebug::log_hex(direction, bytes, ' ');
```

# Sample data
```text
PRESS:      5A 02 02 01 00 00 00 5F 5A 02 02 01 00 00 00 5F 5A 02 02 01 00 00 00 5F 5A 02 02 01 00 00 00 5F 5A 02 02 01 00 00 00 5F 5A 02 02 01 00 00 00 5F 5A 02 02 01 00 00 00 5F 5A 02 02 01 00 00 00 5F 5A 02 02 01 00 00 00 5F 5A 02 02 01 00 00 00 5F
LONG_PRESS: 5A 03 02 06 00 00 00 65 5A 03 02 06 00 00 00 65 5A 03 02 06 00 00 00 65 5A 03 02 06 00 00 00 65 5A 03 02 06 00 00 00 65 5A 03 02 06 00 00 00 65 5A 03 02 06 00 00 00 65 5A 03 02 06 00 00 00 65 5A 03 02 06 00 00 00 65 5A 03 02 06 00 00 00 65
LEFT:       5A 04 02 05 FF 00 00 64 5A 04 02 05 FF 00 00 64 5A 04 02 05 FF 00 00 64 5A 04 02 05 FF 00 00 64 5A 04 02 05 FF 00 00 64 5A 04 02 05 FF 00 00 64 5A 04 02 05 FF 00 00 64 5A 04 02 05 FF 00 00 64 5A 04 02 05 FF 00 00 64 5A 04 02 05 FF 00 00 64
RIGHT:      5A 05 02 04 02 00 00 67 5A 05 02 04 02 00 00 67 5A 05 02 04 02 00 00 67 5A 05 02 04 02 00 00 67 5A 05 02 04 02 00 00 67 5A 05 02 04 02 00 00 67 5A 05 02 04 02 00 00 67 5A 05 02 04 02 00 00 67 5A 05 02 04 02 00 00 67 5A 05 02 04 02 00 00 67
PRESS_LEFT: 5A 16 02 03 FF 00 00 74 5A 16 02 03 FF 00 00 74 5A 16 02 03 FF 00 00 74 5A 16 02 03 FF 00 00 74 5A 16 02 03 FF 00 00 74 5A 16 02 03 FF 00 00 74 5A 16 02 03 FF 00 00 74 5A 16 02 03 FF 00 00 74 5A 16 02 03 FF 00 00 74 5A 16 02 03 FF 00 00 74
PRESS_RIGHT:5A 18 02 02 01 00 00 77 5A 18 02 02 01 00 00 77 5A 18 02 02 01 00 00 77 5A 18 02 02 01 00 00 77 5A 18 02 02 01 00 00 77 5A 18 02 02 01 00 00 77 5A 18 02 02 01 00 00 77 5A 18 02 02 01 00 00 77 5A 18 02 02 01 00 00 77 5A 18 02 02 01 00 00 77
```

# Protocol

- byte 0: always 5A
- byte 1: sequence ID, increasing
- byte 2: always 02
- byte 3-4: command - 0x0100: PRESS, 0x0201: PRESS_RIGHT, 0x03FF PRESS_LEFT, 0x0402: RIGHT, 0x05FF: LEFT, 0x0600: LONG_PRESS
  - commnand can be determined by the first byte
- byte 5-6: always 0x00 (seems to be unused)
- byte 7: parity, should equal to sum(byte 0 to 6) % 256
  - following bytes can repeat byte 0 to 7 several times, which can be ignored, if parity match.

following bytes can repeat byte 0 to 7 several times, which can be ignored, if parity match.
