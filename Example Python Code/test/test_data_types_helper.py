import unittest

from app.data_types_helper import DataTypesHelper


class TestDataTypesHelper(unittest.TestCase):
    def setUp(self):

        self.tested_float_16 = -12384.0
        self.tested_unsigned_integer_16 = 61964
        self.tested_signed_integer_16 = -3572

        self.A_16 = 0xF2
        self.B_16 = 0x0C

        self.tested_float_32 = -9.854026891228019e29
        self.tested_unsigned_integer_32 = 4047962144
        self.tested_signed_integer_32 = -247005152

        self.A_32 = 0xF1
        self.B_32 = 0x47
        self.C_32 = 0x00
        self.D_32 = 0x20

        self.tested_float_64 = -1.916676736030763e234
        self.tested_unsigned_integer_64 = 17335281018422417162
        self.tested_signed_integer_64 = -1111463055287134454

        self.A_64 = 0xF0
        self.B_64 = 0x93
        self.C_64 = 0x4A
        self.D_64 = 0x3D

        self.E_64 = 0x70
        self.F_64 = 0xA3
        self.G_64 = 0xD7
        self.H_64 = 0x0A

        self.data_types_helper_obj = DataTypesHelper

    def tearDown(self):
        pass

    def test_convert_i16_to_float_16_N_A_mode_small_values(self):
        data_type = self.data_types_helper_obj.data_types.float_16

        r = self.data_types_helper_obj.append_two_hex(0, 2, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, 1.1920928955078125e-07)

    def test_convert_i16_to_float_16_N_A_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_16

        r = self.data_types_helper_obj.append_two_hex(self.A_16, self.B_16, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, self.tested_float_16)

    def test_convert_i16_to_float_16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_16

        r = self.data_types_helper_obj.append_two_hex(self.B_16, self.A_16, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r], data_type, self.data_types_helper_obj.swap_modes.byte_and_word_swipe
        )
        self.assertEqual(result, self.tested_float_16)

    def test_convert_i16_to_uint_16_N_A_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_16

        r = self.data_types_helper_obj.append_two_hex(self.A_16, self.B_16, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, self.tested_unsigned_integer_16)

    def test_convert_i16_to_uint_16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_16

        r = self.data_types_helper_obj.append_two_hex(self.B_16, self.A_16, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r], data_type, self.data_types_helper_obj.swap_modes.byte_and_word_swipe
        )
        self.assertEqual(result, self.tested_unsigned_integer_16)

    def test_convert_i16_to_int_16_N_A_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_16

        r = self.data_types_helper_obj.append_two_hex(self.A_16, self.B_16, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, self.tested_signed_integer_16)

    def test_convert_i16_to_int_16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_16

        r = self.data_types_helper_obj.append_two_hex(self.B_16, self.A_16, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r], data_type, self.data_types_helper_obj.swap_modes.byte_and_word_swipe
        )
        self.assertEqual(result, self.tested_signed_integer_16)

    def test_convert_float_32_to_16_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_16

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_float_16,
            data_type,
            self.data_types_helper_obj.swap_modes.no_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["f20c"])

    def test_convert_float_32_to_16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_16

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_float_16,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["0cf2"])

    def test_convert_uint_16_to_16_N_A_swap_mode_small_value(self):
        data_type = self.data_types_helper_obj.data_types.uint_16

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            3, data_type, self.data_types_helper_obj.swap_modes.no_swap
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["0003"])

    def test_convert_uint_16_to_16_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_16

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_unsigned_integer_16,
            data_type,
            self.data_types_helper_obj.swap_modes.no_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["f20c"])

    def test_convert_uint_16_to_16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_16

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_unsigned_integer_16,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["0cf2"])

    def test_convert_int_16_to_16_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_16

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_signed_integer_16,
            data_type,
            self.data_types_helper_obj.swap_modes.no_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["f20c"])

    def test_convert_int_16_to_16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_16

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_signed_integer_16,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["0cf2"])

    def test_convert_2i16_to_float_32_N_A_mode_small_values(self):
        data_type = self.data_types_helper_obj.data_types.float_32

        r1 = self.data_types_helper_obj.append_two_hex(0, 3, 2)
        r2 = self.data_types_helper_obj.append_two_hex(0, 2, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, 2.755092910709023e-40)

    def test_convert_2i16_to_float_32_N_A_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_32

        r1 = self.data_types_helper_obj.append_two_hex(self.A_32, self.B_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.C_32, self.D_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, self.tested_float_32)

    def test_convert_2i16_to_float_32_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_32

        r1 = self.data_types_helper_obj.append_two_hex(self.D_32, self.C_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.B_32, self.A_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2],
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )
        self.assertEqual(result, self.tested_float_32)

    def test_convert_2i16_to_float_32_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_32
        r1 = self.data_types_helper_obj.append_two_hex(self.B_32, self.A_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.D_32, self.C_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2], data_type, self.data_types_helper_obj.swap_modes.byte_swap
        )
        self.assertEqual(result, self.tested_float_32)

    def test_convert_2i16_to_float_32_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_32
        r1 = self.data_types_helper_obj.append_two_hex(self.C_32, self.D_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.A_32, self.B_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2], data_type, self.data_types_helper_obj.swap_modes.word_swap
        )
        self.assertEqual(result, self.tested_float_32)

    def test_convert_2i16_to_uint_32_N_A_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_32

        r1 = self.data_types_helper_obj.append_two_hex(self.A_32, self.B_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.C_32, self.D_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, self.tested_unsigned_integer_32)

    def test_convert_2i16_to_uint_32_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_32

        r1 = self.data_types_helper_obj.append_two_hex(self.D_32, self.C_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.B_32, self.A_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2],
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )
        self.assertEqual(result, self.tested_unsigned_integer_32)

    def test_convert_2i16_to_uint_32_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_32

        r1 = self.data_types_helper_obj.append_two_hex(self.B_32, self.A_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.D_32, self.C_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2], data_type, self.data_types_helper_obj.swap_modes.byte_swap
        )
        self.assertEqual(result, self.tested_unsigned_integer_32)

    def test_convert_2i16_to_uint_32_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_32
        r1 = self.data_types_helper_obj.append_two_hex(self.C_32, self.D_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.A_32, self.B_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2], data_type, self.data_types_helper_obj.swap_modes.word_swap
        )
        self.assertEqual(result, self.tested_unsigned_integer_32)

    def test_convert_2i16_to_int_32_N_A_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_32

        r1 = self.data_types_helper_obj.append_two_hex(self.A_32, self.B_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.C_32, self.D_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, self.tested_signed_integer_32)

    def test_convert_2i16_to_int_32_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_32

        r1 = self.data_types_helper_obj.append_two_hex(self.D_32, self.C_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.B_32, self.A_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2],
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )
        self.assertEqual(result, self.tested_signed_integer_32)

    def test_convert_2i16_to_int_32_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_32
        r1 = self.data_types_helper_obj.append_two_hex(self.B_32, self.A_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.D_32, self.C_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2], data_type, self.data_types_helper_obj.swap_modes.byte_swap
        )
        self.assertEqual(result, self.tested_signed_integer_32)

    def test_convert_2i16_to_int_32_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_32
        r1 = self.data_types_helper_obj.append_two_hex(self.C_32, self.D_32, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.A_32, self.B_32, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2], data_type, self.data_types_helper_obj.swap_modes.word_swap
        )
        self.assertEqual(result, self.tested_signed_integer_32)

    def test_convert_float_32_to_2i16_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_float_32,
            data_type,
            self.data_types_helper_obj.swap_modes.no_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["f147", "0020"])

    def test_convert_float_32_to_2i16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_float_32,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["2000", "47f1"])

    def test_convert_float_32_to_2i16_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_float_32,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["47f1", "2000"])

    def test_convert_float_32_to_2i16_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_float_32,
            data_type,
            self.data_types_helper_obj.swap_modes.word_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["0020", "f147"])

    def test_convert_uint_32_to_2i16_N_A_swap_mode_small_value(self):
        data_type = self.data_types_helper_obj.data_types.uint_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            2, data_type, self.data_types_helper_obj.swap_modes.no_swap
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["0000", "0002"])

    def test_convert_uint_32_to_2i16_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_unsigned_integer_32,
            data_type,
            self.data_types_helper_obj.swap_modes.no_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["f147", "0020"])

    def test_convert_uint_32_to_2i16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_unsigned_integer_32,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["2000", "47f1"])

    def test_convert_uint_32_to_2i16_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_unsigned_integer_32,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["47f1", "2000"])

    def test_convert_uint_32_to_2i16_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_unsigned_integer_32,
            data_type,
            self.data_types_helper_obj.swap_modes.word_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["0020", "f147"])

    def test_convert_int_32_to_2i16_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_32
        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_signed_integer_32,
            data_type,
            self.data_types_helper_obj.swap_modes.no_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["f147", "0020"])

    def test_convert_int_32_to_2i16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_signed_integer_32,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["2000", "47f1"])

    def test_convert_int_32_to_2i16_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_signed_integer_32,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["47f1", "2000"])

    def test_convert_int_32_to_2i16_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_32

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_signed_integer_32,
            data_type,
            self.data_types_helper_obj.swap_modes.word_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["0020", "f147"])

    def test_convert_4i16_to_float_64_N_A_swap_mode_small_values(self):
        data_type = self.data_types_helper_obj.data_types.float_64

        r1 = self.data_types_helper_obj.append_two_hex(0, 2, 2)
        r2 = self.data_types_helper_obj.append_two_hex(0, 1, 2)
        r3 = self.data_types_helper_obj.append_two_hex(0, 3, 2)
        r4 = self.data_types_helper_obj.append_two_hex(0, 2, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, 2.781363544063294e-309)

    def test_convert_4i16_to_float_64_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_64

        r1 = self.data_types_helper_obj.append_two_hex(self.A_64, self.B_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.C_64, self.D_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.E_64, self.F_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.G_64, self.H_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, self.tested_float_64)

    def test_convert_4i16_to_float_64_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_64

        r1 = self.data_types_helper_obj.append_two_hex(self.D_64, self.C_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.B_64, self.A_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.H_64, self.G_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.F_64, self.E_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4],
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )
        self.assertEqual(result, self.tested_float_64)

    def test_convert_4i16_to_float_64_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_64

        r1 = self.data_types_helper_obj.append_two_hex(self.B_64, self.A_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.D_64, self.C_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.F_64, self.E_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.H_64, self.G_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4], data_type, self.data_types_helper_obj.swap_modes.byte_swap
        )
        self.assertEqual(result, self.tested_float_64)

    def test_convert_4i16_to_float_64_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_64

        r1 = self.data_types_helper_obj.append_two_hex(self.C_64, self.D_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.A_64, self.B_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.G_64, self.H_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.E_64, self.F_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4], data_type, self.data_types_helper_obj.swap_modes.word_swap
        )
        self.assertEqual(result, self.tested_float_64)

    def test_convert_4i16_to_uint_64_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_64

        r1 = self.data_types_helper_obj.append_two_hex(self.A_64, self.B_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.C_64, self.D_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.E_64, self.F_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.G_64, self.H_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, self.tested_unsigned_integer_64)

    def test_convert_4i16_to_uint_64_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_64

        r1 = self.data_types_helper_obj.append_two_hex(self.D_64, self.C_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.B_64, self.A_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.H_64, self.G_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.F_64, self.E_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4],
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )
        self.assertEqual(result, self.tested_unsigned_integer_64)

    def test_convert_4i16_to_uint_64_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_64

        r1 = self.data_types_helper_obj.append_two_hex(self.B_64, self.A_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.D_64, self.C_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.F_64, self.E_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.H_64, self.G_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4], data_type, self.data_types_helper_obj.swap_modes.byte_swap
        )
        self.assertEqual(result, self.tested_unsigned_integer_64)

    def test_convert_4i16_to_uint_64_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_64

        r1 = self.data_types_helper_obj.append_two_hex(self.C_64, self.D_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.A_64, self.B_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.G_64, self.H_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.E_64, self.F_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4], data_type, self.data_types_helper_obj.swap_modes.word_swap
        )
        self.assertEqual(result, self.tested_unsigned_integer_64)

    def test_convert_4i16_to_int_64_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_64

        r1 = self.data_types_helper_obj.append_two_hex(self.A_64, self.B_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.C_64, self.D_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.E_64, self.F_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.G_64, self.H_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4], data_type, self.data_types_helper_obj.swap_modes.no_swap
        )
        self.assertEqual(result, self.tested_signed_integer_64)

    def test_convert_4i16_to_int_64_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_64

        r1 = self.data_types_helper_obj.append_two_hex(self.D_64, self.C_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.B_64, self.A_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.H_64, self.G_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.F_64, self.E_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4],
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )
        self.assertEqual(result, self.tested_signed_integer_64)

    def test_convert_4i16_to_int_64_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_64

        r1 = self.data_types_helper_obj.append_two_hex(self.B_64, self.A_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.D_64, self.C_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.F_64, self.E_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.H_64, self.G_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4], data_type, self.data_types_helper_obj.swap_modes.byte_swap
        )
        self.assertEqual(result, self.tested_signed_integer_64)

    def test_convert_4i16_to_int_64_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_64

        r1 = self.data_types_helper_obj.append_two_hex(self.C_64, self.D_64, 2)
        r2 = self.data_types_helper_obj.append_two_hex(self.A_64, self.B_64, 2)
        r3 = self.data_types_helper_obj.append_two_hex(self.G_64, self.H_64, 2)
        r4 = self.data_types_helper_obj.append_two_hex(self.E_64, self.F_64, 2)

        result = self.data_types_helper_obj.convert_registers_to_data_type(
            [r1, r2, r3, r4], data_type, self.data_types_helper_obj.swap_modes.word_swap
        )
        self.assertEqual(result, self.tested_signed_integer_64)

    def test_convert_float_64_to_4i16_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_float_64,
            data_type,
            self.data_types_helper_obj.swap_modes.no_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["f093", "4a3d", "70a3", "d70a"])

    def test_convert_float_64_to_4i16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_float_64,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["3d4a", "93f0", "0ad7", "a370"])

    def test_convert_float_64_to_4i16_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_float_64,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["93f0", "3d4a", "a370", "0ad7"])

    def test_convert_float_64_to_4i16_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.float_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_float_64,
            data_type,
            self.data_types_helper_obj.swap_modes.word_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["4a3d", "f093", "d70a", "70a3"])

    def test_convert_uint_64_to_4i16_N_A_swap_mode_small_value(self):
        data_type = self.data_types_helper_obj.data_types.uint_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            2, data_type, self.data_types_helper_obj.swap_modes.no_swap
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["0000", "0000", "0000", "0002"])

    def test_convert_uint_64_to_4i16_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_unsigned_integer_64,
            data_type,
            self.data_types_helper_obj.swap_modes.no_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["f093", "4a3d", "70a3", "d70a"])

    def test_convert_uint_64_to_4i16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_unsigned_integer_64,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["3d4a", "93f0", "0ad7", "a370"])

    def test_convert_uint_64_to_4i16_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_unsigned_integer_64,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["93f0", "3d4a", "a370", "0ad7"])

    def test_convert_uint_64_to_4i16_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.uint_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_unsigned_integer_64,
            data_type,
            self.data_types_helper_obj.swap_modes.word_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["4a3d", "f093", "d70a", "70a3"])

    def test_convert_int_64_to_4i16_N_A_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_signed_integer_64,
            data_type,
            self.data_types_helper_obj.swap_modes.no_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["f093", "4a3d", "70a3", "d70a"])

    def test_convert_int_64_to_4i16_byte_and_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_signed_integer_64,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_and_word_swipe,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["3d4a", "93f0", "0ad7", "a370"])

    def test_convert_int_64_to_4i16_byte_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_signed_integer_64,
            data_type,
            self.data_types_helper_obj.swap_modes.byte_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["93f0", "3d4a", "a370", "0ad7"])

    def test_convert_int_64_to_4i16_word_swap_mode(self):
        data_type = self.data_types_helper_obj.data_types.int_64

        result = self.data_types_helper_obj.convert_data_type_to_registers(
            self.tested_signed_integer_64,
            data_type,
            self.data_types_helper_obj.swap_modes.word_swap,
        )

        hex_result = self.data_types_helper_obj.convert_to_readeable_characters(
            result, data_type
        )

        self.assertEqual(hex_result, ["4a3d", "f093", "d70a", "70a3"])


if __name__ == "__main__":
    unittest.main()
