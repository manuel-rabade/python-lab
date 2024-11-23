# LoRa Sat Decoder

## Kaitai

https://kaitai.io/

```
kaitai-struct-compiler -t python tianqi.ksy
kaitai-struct-compiler -t python norby.ksy
```

## Norby

```
$ python lora_sat_decoder.py norby.ksy --hex 8effffffff0a0601c93f5600000000f10f0000a6b49223d22e42524b204d57205645523a3035615f303100000000000e0100c50b0000000716000cd00a8bf32103000000000000000000000000000000000000000000000027000001dfff6d010000000000000e04040f0f0f0f0f0f00fafb3ffc30000009330200000c00024ef6000061070c0b090020002d20f3e8
header:
	length: 142
	receiver_address: 4294967295
	transmitter_address: 3372287498
	transaction_number: 22079
	reserved: b'\x00\x00'
	msg_type_id: 0
payload:
	frame_start_mark: b'\xf1\x0f'
	frame_definition: 0
	frame_number: 46246
	frame_generation_time: 785523602
	brk_title: BRK MW VER:05a_01
	brk_number_active: 0
	brk_restarts_count_active: 3013
	brk_current_mode_id: 0
	brk_transmitter_power_active: 7
	brk_temp_active: 22
	brk_module_state_active: b'\x00\x0c'
	brk_voltage_offset_amplifier_active: 2768
	brk_last_received_packet_rssi_active: -117
	brk_last_received_packet_snr_active: -13
	brk_archive_record_pointer: 801
	brk_last_received_packet_snr_inactive: 0
	ms_module_state: b'\x00\x00'
	ms_payload_state: b'\x00\x00'
	ms_temp: 0
	ms_pn_supply_state: 0
	sop_altitude_glonass: 0
	sop_latitude_glonass: 0
	sop_longitude_glonass: 0
	sop_date_time_glonass: 0
	sop_magnetic_induction_module: 39
	sop_angular_velocity_vector: b'\x00\x01\xdf\xffm\x01'
	sop_angle_priority1: 0
	sop_angle_priority2: 0
	sop_mk_temp_dsg1: 0
	sop_mk_temp_dsg6: 0
	sop_board_temp: 14
	sop_state: b'\x04\x04'
	sop_state_dsg: b'\x0f\x0f\x0f\x0f\x0f\x0f'
	sop_orientation_number: 0
	ses_median_panel_x_temp_positive: -6
	ses_median_panel_x_temp_negative: -5
	ses_solar_panels_state: b'?\xfc0\x00\x00'
	ses_charge_level_m_ah: 13065
	ses_battery_state: b'\x02\x00\x00'
	ses_charging_keys_state: b'\x0c\x00'
	ses_power_line_state: 2
	ses_total_charging_power: -2482
	ses_total_generated_power: 0
	ses_total_power_load: 1889
	ses_median_pmm_temp: 12
	ses_median_pam_temp: 11
	ses_median_pdm_temp: 9
	ses_module_state: b'\x00 \x00'
	ses_voltage: 8237
	crc16: 59635
```

https://tinygs.com/packet/a5910fb2-47a4-4bcb-b9ac-975835fd9dc0

```
$ python lora_sat_decoder.py norby.ksy --bin norby.bin
header:
	length: 142
	receiver_address: 4294967295
	transmitter_address: 3372287498
	transaction_number: 22591
	reserved: b'\x00\x00'
	msg_type_id: 0
payload:
	frame_start_mark: b'\xf1\x0f'
	frame_definition: 0
	frame_number: 46252
	frame_generation_time: 785523724
	brk_title: BRK MW VER:05a_01
	brk_number_active: 0
	brk_restarts_count_active: 3013
	brk_current_mode_id: 0
	brk_transmitter_power_active: 7
	brk_temp_active: 22
	brk_module_state_active: b'\x00\x0c'
	brk_voltage_offset_amplifier_active: 2766
	brk_last_received_packet_rssi_active: -117
	brk_last_received_packet_snr_active: -13
	brk_archive_record_pointer: 805
	brk_last_received_packet_snr_inactive: 0
	ms_module_state: b'\x00\x00'
	ms_payload_state: b'\x00\x00'
	ms_temp: 0
	ms_pn_supply_state: 0
	sop_altitude_glonass: 0
	sop_latitude_glonass: 0
	sop_longitude_glonass: 0
	sop_date_time_glonass: 0
	sop_magnetic_induction_module: 32
	sop_angular_velocity_vector: b'\x1e\x00T\x01\xd0\x00'
	sop_angle_priority1: 0
	sop_angle_priority2: 0
	sop_mk_temp_dsg1: 0
	sop_mk_temp_dsg6: 0
	sop_board_temp: 13
	sop_state: b'\x04\x04'
	sop_state_dsg: b'\x0f\x0f\x0f\x0f\x0f\x0f'
	sop_orientation_number: 0
	ses_median_panel_x_temp_positive: -7
	ses_median_panel_x_temp_negative: -6
	ses_solar_panels_state: b'?\xfc0\x00\x00'
	ses_charge_level_m_ah: 13055
	ses_battery_state: b'\x02\x00\x00'
	ses_charging_keys_state: b'\x0c\x00'
	ses_power_line_state: 2
	ses_total_charging_power: -2480
	ses_total_generated_power: 0
	ses_total_power_load: 1887
	ses_median_pmm_temp: 11
	ses_median_pam_temp: 10
	ses_median_pdm_temp: 8
	ses_module_state: b'\x00 \x00'
	ses_voltage: 8233
	crc16: 43928
```

## Tianqi

https://tinygs.com/packet/fbec960f-8d1e-4013-9206-eb5b09402944

```
$ python lora_sat_decoder.py tianqi.ksy --bin tianqi.bin
header:
	net_id: 235
	message_type_id: 245
	head_unknown: 64
	sat_timestamp: 217551210
	sat_id: 28
unknown_blocks:
	block1:
		unknown3: 248
		unknown4: 4
		unknown5: 12
		unknown6: 247
		unknown7: 145
		unknown8: 104
		unknown9: 0
	block2:
		unknown10_1: 0
		unknown10_2: 74
		unknown10_3: 222
	block3:
		unknown11_1: 41
		unknown11_2: 219
		unknown11_3: 59
		unknown11_4: 18
		unknown11_5: 252
		unknown11_6: 165
		unknown12_1: 66
		unknown12_2: 51
		unknown12_3: 101
		unknown12_4: 93
timestamp:
	last_rx_time: 1133344719
	unknown13: 66
	unknown14: 131
orbital_data:
	set1:
		semi_major_axis: 1.428009821502485e-09
		eccentricity: -2.2270361573475653e+28
		inclination: 2.0312576293945312
		ascending_node: 5.657901293948109e+16
		angle_x: 4009.318359375
		angle_y: 2.850230556393607e-32
	set2:
		semi_major_axis: 2392684.75
		eccentricity: 1.2491895814241907e-34
		inclination: 6.707956894187398e-39
		ascending_node: 4.412377775899769e-39
		angle_x: 1.2123577490038947e-38
		angle_y: 5.971814431061023e-36
```
