import collections
import struct
from itertools import zip_longest


class DataTypesHelper:

    Data_type_tuple = collections.namedtuple(
        "Data_Type_Tuple", ["variable_type", "integer_type", "variable_bytes_number"]
    )

    data_types_dictionary = {
        "float_16": Data_type_tuple("e", "H", 2),
        "uint_16": Data_type_tuple("H", "H", 2),
        "int_16": Data_type_tuple("h", "H", 2),
        "float_32": Data_type_tuple("f", "L", 4),
        "uint_32": Data_type_tuple("L", "L", 4),
        "int_32": Data_type_tuple("l", "L", 4),
        "float_64": Data_type_tuple("d", "Q", 8),
        "uint_64": Data_type_tuple("Q", "Q", 8),
        "int_64": Data_type_tuple("q", "Q", 8),
    }

    data_types = collections.namedtuple(
        "Data_Types_Tuple", data_types_dictionary.keys()
    )(*data_types_dictionary.values())

    swap_modes_dictionary = {
        "no_swap": "N/A",
        "byte_and_word_swipe": "s",
        "byte_swap": "s-b",
        "word_swap": "s-w",
    }

    swap_modes = collections.namedtuple(
        "Swap_Modes_Tuple", swap_modes_dictionary.keys()
    )(*swap_modes_dictionary.values())

    def convert_registers_to_data_type(registers, data_type, swap_mode):
        if registers is None or not registers:
            return None

        for register in registers:
            if register is None:
                return None

        raw_integer_representation = 0

        if data_type.variable_bytes_number == 2:
            raw_integer_representation = registers[0]

        if data_type.variable_bytes_number == 4:
            r1 = registers[0]
            r2 = registers[1]

            if swap_mode in [
                DataTypesHelper.swap_modes.byte_swap,
                DataTypesHelper.swap_modes.word_swap,
            ]:
                r1, r2 = r2, r1

            raw_integer_representation = DataTypesHelper.append_two_hex(
                r1, r2, data_type.variable_bytes_number
            )

        first_part = 0
        second_part = 0

        if data_type.variable_bytes_number == 8:
            r1 = registers[0]
            r2 = registers[1]
            r3 = registers[2]
            r4 = registers[3]

            if swap_mode in [
                DataTypesHelper.swap_modes.byte_swap,
                DataTypesHelper.swap_modes.word_swap,
            ]:
                r1, r2, r3, r4 = r2, r1, r4, r3

            first_part = DataTypesHelper.append_two_hex(
                r1, r2, data_type.variable_bytes_number // 2
            )
            second_part = DataTypesHelper.append_two_hex(
                r3, r4, data_type.variable_bytes_number // 2
            )

            raw_integer_representation = DataTypesHelper.append_two_hex(
                first_part, second_part, data_type.variable_bytes_number
            )

        if swap_mode in [
            DataTypesHelper.swap_modes.byte_and_word_swipe,
            DataTypesHelper.swap_modes.byte_swap,
        ]:
            if data_type.variable_bytes_number == 8:
                intermediate_data_type = DataTypesHelper.data_types.uint_32
                first_part_swapped = (
                    DataTypesHelper.swap_integer_bytes_and_word_with_bytes_number(
                        first_part, intermediate_data_type
                    )
                )
                second_part_swapped = (
                    DataTypesHelper.swap_integer_bytes_and_word_with_bytes_number(
                        second_part, intermediate_data_type
                    )
                )

                (
                    variable_type_temp,
                    integer_type_temp,
                    variable_bytes_number_temp,
                ) = intermediate_data_type

                raw_integer_representation = DataTypesHelper.append_two_hex(
                    first_part_swapped,
                    second_part_swapped,
                    data_type.variable_bytes_number,
                )
            else:
                raw_integer_representation = (
                    DataTypesHelper.swap_integer_bytes_and_word_with_bytes_number(
                        raw_integer_representation, data_type
                    )
                )

        text_representation = DataTypesHelper.hex_string_from_integer(
            raw_integer_representation, data_type
        )

        converted_number = struct.unpack(
            ">" + data_type.variable_type, bytes.fromhex(text_representation)
        )[0]

        return converted_number

    def convert_data_type_to_registers(float_number, data_type, swap_mode):
        if float_number is None:
            return None

        raw_int_representation = DataTypesHelper.decimal_to_int(float_number, data_type)

        if swap_mode in [
            DataTypesHelper.swap_modes.byte_and_word_swipe,
            DataTypesHelper.swap_modes.byte_swap,
        ]:
            raw_int_representation = (
                DataTypesHelper.swap_integer_bytes_and_word_with_bytes_number(
                    raw_int_representation, data_type
                )
            )

        if data_type.variable_bytes_number == 2:
            r1 = raw_int_representation
            return [r1]

        if data_type.variable_bytes_number == 4:
            r1, r2 = [
                x
                for x in DataTypesHelper.split_integer_by_bytes(
                    raw_int_representation, data_type
                )
            ]

            if swap_mode in [
                DataTypesHelper.swap_modes.byte_swap,
                DataTypesHelper.swap_modes.word_swap,
            ]:
                r1, r2 = r2, r1

            return [r1, r2]

        if data_type.variable_bytes_number == 8:
            intermediate_data_type = DataTypesHelper.data_types.uint_32

            r1, r2, r3, r4 = 0, 0, 0, 0

            first_part, second_part = [
                x
                for x in DataTypesHelper.split_integer_by_bytes(
                    raw_int_representation, data_type
                )
            ]

            if swap_mode in [
                DataTypesHelper.swap_modes.byte_and_word_swipe,
                DataTypesHelper.swap_modes.byte_swap,
            ]:
                first_part, second_part = second_part, first_part

            r1, r2 = [
                x
                for x in DataTypesHelper.split_integer_by_bytes(
                    first_part, intermediate_data_type
                )
            ]

            r3, r4 = [
                x
                for x in DataTypesHelper.split_integer_by_bytes(
                    second_part, intermediate_data_type
                )
            ]

            if swap_mode in [
                DataTypesHelper.swap_modes.byte_swap,
                DataTypesHelper.swap_modes.word_swap,
            ]:
                r1, r2, r3, r4 = r2, r1, r4, r3

            return [r1, r2, r3, r4]

    def append_two_hex(a, b, b_length):
        return (a << b_length * 4) | b

    def convert_to_readeable_characters(result, data_type):
        return [
            DataTypesHelper.hex_string_from_integer(x, data_type, True) for x in result
        ]

    def hex_string_from_integer(int, data_type, testMode=False):

        raw_hex_string = hex(int)[2:]

        current_variable_bytes_number = data_type.variable_bytes_number

        if not testMode:
            current_variable_bytes_number = data_type.variable_bytes_number * 2
        else:
            if data_type.variable_bytes_number == 2:
                current_variable_bytes_number = data_type.variable_bytes_number * 2

            if data_type.variable_bytes_number == 8:
                current_variable_bytes_number = data_type.variable_bytes_number // 2

        result = raw_hex_string.rjust(current_variable_bytes_number, "0")

        return result

    def swap_integer_bytes_and_word_with_bytes_number(integer, data_type):
        return struct.unpack(
            "<" + data_type.integer_type,
            struct.pack(">" + data_type.integer_type, integer),
        )[0]

    def decimal_to_int(decimal, data_type):
        return struct.unpack(
            "<" + data_type.integer_type,
            struct.pack("<" + data_type.variable_type, decimal),
        )[0]

    def split_integer_by_bytes(integer, data_type):
        word_number = data_type.variable_bytes_number // 2

        divisor = 256**word_number
        return [x for x in divmod(integer, divisor)]

    def split_hex_string_by_pairs(hex_string):
        pairs = [
            i + j
            for i, j in zip_longest(hex_string[::2], hex_string[1::2], fillvalue="_")
        ]
        return pairs

    def __init__(self):
        pass
